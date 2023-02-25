import random

import pandas as pd
from keras.layers import InputLayer
from keras.layers import Dense
from keras.models import Sequential
from keras.losses import MAE
from keras.optimizers import SGD
from sklearn.preprocessing import MinMaxScaler, Normalizer
from sklearn.model_selection import train_test_split

df = pd.read_csv('diabetes.csv')
# print(df.describe())
random.seed(123)

scaler = MinMaxScaler()  # 0 - 1

X = df.drop(columns="Outcome")  # all input
for c in X.columns:  # c = Pregnancies
    df[c] = scaler.fit_transform(df[c].values.reshape(-1, 1))
# print(df.describe())

train, test = train_test_split(df, test_size=0.15)
train = pd.DataFrame(train)
train_x = train.drop(columns=['Outcome'])
train_y = train['Outcome']
print(train_x.shape)
