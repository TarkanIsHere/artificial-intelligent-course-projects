import numpy as np
from matplotlib import pyplot as plt
from sklearn.datasets import load_wine
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split, cross_validate
from sklearn.metrics import confusion_matrix
from sklearn import svm
wine = load_wine()
X = wine.data
y = wine.target
class_names=wine.target_names
clf = DecisionTreeClassifier(random_state=0)
X_train, X_test, y_train, y_test = train_test_split(X,y, train_size = 0.7, test_size = 0.3, random_state = 0, stratify = y)
clf.fit(X_train,y_train)
test_sonuc = clf.predict(X_test)
print(test_sonuc)
cm = confusion_matrix(y_test, test_sonuc)
print(cm)
plt.matshow(cm)
plt.title('Confusion matrix')
plt.colorbar()
plt.ylabel('True label')
plt.xlabel('Predicted label')
plt.show()


classifier = svm.SVC(kernel='linear', C=0.01)
y_pred = classifier.fit(X_train, y_train).predict(X_test)
# Confusion Matrix
confusion_m = confusion_matrix(y_test,y_pred)
print(confusion_m)
plt.matshow(confusion_m)
plt.title('Confusion matrix')
plt.colorbar()
plt.ylabel('True label')
plt.xlabel('Predicted label')
plt.show()

new_data = [14.37,1.95,2.5,16.8,113,3.85,3.49,.24,2.18,7.8,.86,3.45,1480],[13.73,4.36,2.26,22.5,88,1.28,.47,.52,1.15,6.62,.78,1.75,120]
predicted_class_svm = clf.predict(new_data)
predicted_class_tree = classifier.predict(new_data)
print("DENEME GIRDISI:13.73,4.36,2.26,22.5,88,1.28,.47,.52,1.15,6.62,.78,1.75,120")
print("DECISION TREE ILE TAHMIN :", predicted_class_tree[1])
print("DENEME GIRDISI:13.73,4.36,2.26,22.5,88,1.28,.47,.52,1.15,6.62,.78,1.75,120")
print("SWM ILE TAHMIN :", predicted_class_svm[1])

scoring = ['accuracy', 'precision_macro', 'recall_macro']

cv_results = cross_validate(clf, X, y, cv=10, scoring=scoring)

# Sonuçları tabloya kaydetme
results_table = np.zeros((3, 10))
for i, metric in enumerate(scoring):
    results_table[i] = cv_results['test_' + metric]

# Tabloyu yazdırma
print("\n10-Fold Cross Validation Results(BINARY TREE):")
print("Accuracy\tPrecision\tRecall")
for i in range(10):
    print("{:.4f}\t\t{:.4f}\t\t{:.4f}".format(results_table[0, i], results_table[1, i], results_table[2, i]))
cv_results = cross_validate(classifier, X, y, cv=10, scoring=scoring)
results_table = np.zeros((3, 10))
for i, metric in enumerate(scoring):
    results_table[i] = cv_results['test_' + metric]

# Tabloyu yazdırma
print("\n10-Fold Cross Validation Results(SWM):")
print("Accuracy\tPrecision\tRecall")
for i in range(10):
    print("{:.4f}\t\t{:.4f}\t\t{:.4f}".format(results_table[0, i], results_table[1, i], results_table[2, i]))





