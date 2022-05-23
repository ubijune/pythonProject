import matplotlib.pyplot as plt
import numpy as np

from sklearn.datasets import load_agaricus-lepiota

file=open("agaricus-lepiota.data","r")

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(
    agaricus-lepiota_dataset['data'], agaricus-lepiota_dataset['target'], random_state=0)
print("X_train: {}".format(X_train.shape))
print("y_train: {}".format(y_train.shape))
print("X_test: {}".format(X_test.shape))
print("y_test: {}".format(y_test.shape))

from sklearn.neighbors import KNeighborsClassifier

knn = KNeighborsClassifier(n_neighbors=10)

knn.fit(X_train,y_train)

import numpy as np

X_new = np.array([])

prediction = knn.predict(X_new)

print("name: {}".format(iris_dataset['target_names'][prediction]))

y_prediction = knn.predict(X_test)

for i in range(0, len(y_prediction)):
    y = y_prediction[i]
    print("{} : {}".format(X_test[i], agaricus-lepiota_dataset['target_names'][y_pred]))