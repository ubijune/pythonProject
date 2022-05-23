import tensorflow as tf
import pandas as pd

파일경로 = 'https://raw.githubusercontent.com/blackdew/tensorflow1/master/csv/lemonade.csv'
레모네이드 = pd.read_csv(파일경로)
레모네이드.head()

독립 = 레모네이드[['온도']]
종속 = 레모네이드[['판매량']]
print(독립.shape, 종속.shape)

X = tf.keras.layers.Input(shape=[1])
Y = tf.keras.layers.Dense(1) (X)
model = tf.keras.models.Model(X, Y)
model.compile(loss='mse')

model.fit(독립, 종속, epochs=1000, verbose=1)
model.fit(독립, 종속, epochs=10)

print(model.predict(독립))
print(model.predict([[15]]))