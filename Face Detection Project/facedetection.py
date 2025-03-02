import threading
from tkinter import messagebox
import cv2
import tkinter as tk
from deepface import DeepFace

goruntu = cv2.VideoCapture(0)
goruntu.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
goruntu.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

sayac = 0
eslesme = False
eslesme_sayisi = 0


# Karşılaştırılacak görüntünün yüklenmesi
ref_img = cv2.imread("ref.jpg")

tespit_edilen_duygu = ""

def check_face_emotion(taslak):
    global eslesme, tespit_edilen_duygu, eslesme_sayisi

    try:
        # Yüz eşleşmesini doğrulama işlemi
        if DeepFace.verify(taslak, ref_img.copy())['verified']:
            eslesme = True

        else:
            eslesme = False

        # Duygu analizini gerçekleştir
        analiz_sonucu = DeepFace.analyze(taslak, actions=['emotion'])

        if isinstance(analiz_sonucu, list):
            analiz_sonucu = analiz_sonucu[0]

        tespit_edilen_duygu = analiz_sonucu['dominant_emotion']
    except ValueError:
        eslesme = False
        tespit_edilen_duygu = ""
    except Exception as e:
        print(f"Hata: {e}")
        eslesme = False
        tespit_edilen_duygu = ""

def show_alert():
    root = tk.Tk()
    root.withdraw()
    messagebox.showwarning("Uyarı", "Yabancı Algılandı!")
    root.destroy()

while True:
    eslesme_sayisi += 1
    print(eslesme_sayisi)
    r, taslak = goruntu.read()
    if r:
        if sayac % 38 == 8:
            try:
                threading.Thread(target=check_face_emotion, args=(taslak.copy(),)).start()
            except ValueError:
                pass
        sayac += 1

        # Eşleşme durumu ve eşleşme sayısını kontrol etme
        if not eslesme and eslesme_sayisi >= 500:

            show_alert()
            eslesme_sayisi = 0

        # Yüz karşılaştırılmasının yapılması
        if eslesme:
            cv2.putText(taslak, "ESLESIYOR!", (20, 400), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 255, 0), 3)
        else:
            cv2.putText(taslak, "ESLESMIYOR!", (20, 400), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 3)

        # Duygu durumunu kontrol etme
        if tespit_edilen_duygu:
            cv2.putText(taslak, f"DUYGU: {tespit_edilen_duygu.upper()}", (20, 450), cv2.FONT_HERSHEY_SIMPLEX, 2,
                        (66, 185, 245), 3)

        cv2.imshow("video", taslak)

    key = cv2.waitKey(1)
    if key == ord("q"):
        break

cv2.destroyAllWindows()
