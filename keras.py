# 모듈 읽기
from keras.models import Sequential
from keras.layers.core import Dense, Dropout, Activation
from keras.callbacks import EarlyStopping
import pandas as pd, numpy as np

# 데이터 가공

csv = pd.read_csv("bmi.csv")
csv["weight"]/=100
csv["height"]/=200

bmi_class={
    "thin":[1,0,0],
    "normal":[0,1,0],
    "fat":[0,0,1]
}

y = np.empty((20000,3))
for i,v in enumerate(csv["label"]):
    y[i] = bmi_class[v]

x = csv[["weight","height"]].as_matrix()

x_train, y_train = x[1:15000], y[1:15000]
x_test,y_test = x[15001:20000],y[15001:20000]

# 모델 만들기
model = Sequential()

# 레이블 형성
model = Sequential()
model.add(Dense(512, input_shape=(2,)))
model.add(Activation('relu'))
model.add(Dropout(0.1))
model.add(Dense(512))
model.add(Activation('relu'))
model.add(Dropout(0.1))
model.add(Dense(3))
model.add(Activation('softmax'))
model.compile("rmsprop","categorical_crossentropy",metrics=['accuracy'])
# 학습
model.fit(x_train,y_train)

# 예측

# 정답률
score = model.evaluate(x_test,y_test)
print(score)