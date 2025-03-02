from random import randint
import time

vezir_sayisi = 8

# Veziri rastgele oyun tahtaina yerleştirme
def vezirleriRastgeleYerlestir(oyun_tahtasi, satir):
    for i in range(vezir_sayisi):
        satir[i] = randint(0, vezir_sayisi - 1)
        oyun_tahtasi[satir[i]][i] = 1


def oyunTahtasiniYazdir(oyun_tahtasi):
    for i in range(vezir_sayisi):
        print(oyun_tahtasi[i])


def tahtalariKarsilastir(oyun_tahtasi_bir, oyun_tahtasi_2):
    for i in range(vezir_sayisi):
        if (oyun_tahtasi_bir[i] != oyun_tahtasi_2[i]):
            return False
    return True


def doldur(oyun_tahtasi, deger):
    for i in range(vezir_sayisi):
        for j in range(vezir_sayisi):
            oyun_tahtasi[i][j] = deger



def calculateObjective(oyun_tahtasi, oyun_tahtasi_satir):

    vezir_yeme_puani = 0


    for i in range(vezir_sayisi):
        row = oyun_tahtasi_satir[i]
        col = i - 1
        while (col >= 0 and oyun_tahtasi[row][col] != 1):
            col -= 1

        if (col >= 0 and oyun_tahtasi[row][col] == 1):
            vezir_yeme_puani += 1


        row = oyun_tahtasi_satir[i]
        col = i + 1
        while (col < vezir_sayisi and oyun_tahtasi[row][col] != 1):
            col += 1

        if (col < vezir_sayisi and oyun_tahtasi[row][col] == 1):
            vezir_yeme_puani += 1


        row = oyun_tahtasi_satir[i] - 1
        col = i - 1
        while (col >= 0 and row >= 0 and oyun_tahtasi[row][col] != 1):
            col -= 1
            row -= 1

        if (col >= 0 and row >= 0 and oyun_tahtasi[row][col] == 1):
            vezir_yeme_puani += 1


        row = oyun_tahtasi_satir[i] + 1
        col = i + 1
        while (col < vezir_sayisi and row < vezir_sayisi and oyun_tahtasi[row][col] != 1):
            col += 1
            row += 1

        if (col < vezir_sayisi and row < vezir_sayisi and oyun_tahtasi[row][col] == 1):
            vezir_yeme_puani += 1

        row = oyun_tahtasi_satir[i] + 1
        col = i - 1
        while (col >= 0 and row < vezir_sayisi and oyun_tahtasi[row][col] != 1):
            col -= 1
            row += 1

        if (col >= 0 and row < vezir_sayisi and oyun_tahtasi[row][col] == 1):
            vezir_yeme_puani += 1


        row = oyun_tahtasi_satir[i] - 1
        col = i + 1
        while (col < vezir_sayisi and row >= 0 and oyun_tahtasi[row][col] != 1):
            col += 1
            row -= 1

        if (col < vezir_sayisi and row >= 0 and oyun_tahtasi[row][col] == 1):
            vezir_yeme_puani += 1

    #vezirlerin birbirini yemesi çift olarak alındığı için ikiye bölüyoruz toplam yeme puanını
    return int(vezir_yeme_puani / 2)



def oyunTahtasiOlustur(board, state):
    for i in range(vezir_sayisi):
        for j in range(vezir_sayisi):
            board[i][j] = 0
    for i in range(vezir_sayisi):
        board[state[i]][i] = 1


def satirKopyala(satir1, satir2):
    for i in range(vezir_sayisi):
        satir1[i] = satir2[i]



def getNeighbour(oyun_tahtasi, komsu_oyun_tahtasi_satir):

    opBoard = [[0 for _ in range(vezir_sayisi)] for _ in range(vezir_sayisi)]
    opState = [0 for _ in range(vezir_sayisi)]

    satirKopyala(opState, komsu_oyun_tahtasi_satir)
    oyunTahtasiOlustur(opBoard, opState)
    opObjective = calculateObjective(opBoard, opState)


    NeighbourBoard = [[0 for _ in range(vezir_sayisi)] for _ in range(vezir_sayisi)]

    NeighbourState = [0 for _ in range(vezir_sayisi)]
    satirKopyala(NeighbourState, komsu_oyun_tahtasi_satir)
    oyunTahtasiOlustur(NeighbourBoard, NeighbourState)

    for i in range(vezir_sayisi):
        for j in range(vezir_sayisi):


            if (j != komsu_oyun_tahtasi_satir[i]):

                NeighbourState[i] = j
                NeighbourBoard[NeighbourState[i]][i] = 1
                NeighbourBoard[komsu_oyun_tahtasi_satir[i]][i] = 0


                temp = calculateObjective(NeighbourBoard, NeighbourState)



                if (temp <= opObjective):
                    opObjective = temp
                    satirKopyala(opState, NeighbourState)
                    oyunTahtasiOlustur(opBoard, opState)

                NeighbourBoard[NeighbourState[i]][i] = 0
                NeighbourState[i] = komsu_oyun_tahtasi_satir[i]
                NeighbourBoard[komsu_oyun_tahtasi_satir[i]][i] = 1

    satirKopyala(komsu_oyun_tahtasi_satir, opState)
    doldur(oyun_tahtasi, 0)
    oyunTahtasiOlustur(oyun_tahtasi, komsu_oyun_tahtasi_satir)


def hillClimbing(oyun_tahtasi, oyun_tahtasi_satiri):


    komsu_oyun_tahtasi = []
    for i in range(vezir_sayisi):
        row = []
        for i in range(vezir_sayisi):
            row.append(0)
        komsu_oyun_tahtasi.append(row)

    komsu_oyun_tahtasi_satir = []
    for i in range(vezir_sayisi):
        komsu_oyun_tahtasi_satir.append(0)


    for i in range(vezir_sayisi):
        komsu_oyun_tahtasi_satir[i] = oyun_tahtasi_satiri[i]
    # oyun tahtasının oluşturulması

    for i in range(vezir_sayisi):
        for j in range(vezir_sayisi):
            oyun_tahtasi[i][j] = 0
    for i in range(vezir_sayisi):
        oyun_tahtasi[oyun_tahtasi_satiri[i]][i] = 1

    islem_sayisi = 0
    random_restart_sayisi = 0

    while True:

        islem_sayisi += 1
        print(str(islem_sayisi) +". Adım")
        kontrol_degisken = 0

        satirKopyala(oyun_tahtasi_satiri, komsu_oyun_tahtasi_satir)
        oyunTahtasiOlustur(oyun_tahtasi, oyun_tahtasi_satiri)

        getNeighbour(komsu_oyun_tahtasi, komsu_oyun_tahtasi_satir)

        if (tahtalariKarsilastir(oyun_tahtasi_satiri, komsu_oyun_tahtasi_satir)):
            kontrol_degisken = 1
            tahtaYazdir()
            print("")
            break

        elif (calculateObjective(oyun_tahtasi, oyun_tahtasi_satiri) == calculateObjective(komsu_oyun_tahtasi, komsu_oyun_tahtasi_satir)):
            kontrol_degisken = 1
            random_restart_sayisi += 1
            print("Random Restart Yapıldı")
            oyun_tahtasi_satiri = [0] * vezir_sayisi
            oyun_tahtasi = []
            for _ in range(vezir_sayisi):
                row = []
                for _ in range(vezir_sayisi):
                    row.append(0)
                oyun_tahtasi.append(row)

            vezirleriRastgeleYerlestir(oyun_tahtasi, oyun_tahtasi_satiri)
            komsu_oyun_tahtasi = []
            for i in range(vezir_sayisi):
                row = []
                for i in range(vezir_sayisi):
                    row.append(0)
                komsu_oyun_tahtasi.append(row)

            komsu_oyun_tahtasi_satir = []
            for i in range(vezir_sayisi):
                komsu_oyun_tahtasi_satir.append(0)


            for i in range(vezir_sayisi):
                komsu_oyun_tahtasi_satir[i] = oyun_tahtasi_satiri[i]

            for i in range(vezir_sayisi):
                for j in range(vezir_sayisi):
                    oyun_tahtasi[i][j] = 0
            for i in range(vezir_sayisi):
                oyun_tahtasi[oyun_tahtasi_satiri[i]][i] = 1
            tahtaYazdir()
            print("")

        if(kontrol_degisken == 0):
            tahtaYazdir()
            print("")
        kontrol_degisken = 0

    print("Toplam random restart sayisi: " + str(random_restart_sayisi))
    print("Toplam yapılan adım sayisi: " + str(islem_sayisi))


def tahtaYazdir():
    harfListesi = ['A', "B", "C", "D", "E", "F", "G", "H"]
    print("   A B C D E F G H")
    for i in range(vezir_sayisi):
        print(harfListesi[i], end="  ")
        print(*oyun_tahtasi[i])



oyun_tahtasi_satiri = [0] * vezir_sayisi
oyun_tahtasi = []
for _ in range(vezir_sayisi):
    row = []
    for _ in range(vezir_sayisi):
        row.append(0)
    oyun_tahtasi.append(row)


vezirleriRastgeleYerlestir(oyun_tahtasi, oyun_tahtasi_satiri)
start_time = time.perf_counter()
hillClimbing(oyun_tahtasi, oyun_tahtasi_satiri)
last_time = time.perf_counter()
gecen_sure = last_time - start_time


print("Toplam geçen süre(ms): " + str("{:.2f}".format(gecen_sure * 1000)))

