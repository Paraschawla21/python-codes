import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from keras.preprocessing import sequence
a = pd.DataFrame(pd.read_csv("C:/Users/PARAS/Downloads/DCOILBRENTEU.csv"))
a = a[a.DCOILBRENTEU != '.']
#setting learning parameters
batch_size = 64
epochs = 20
time_steps = 20
def get_train_length(dataset, batch_size, test_percent):
    # substract test_percent to be excluded from training, reserved for testset
    length = len(dataset)
    length *= 1 - test_percent
    train_length_values = []
    for x in range(int(length) - 100,int(length)): 
        modulo=x%batch_size
        if (modulo == 0):
            train_length_values.append(x)
            print(x)
    return (max(train_length_values))
length = get_train_length(a, batch_size, 0.08)
print(length)
training_set = a.iloc[:,1:2]
from sklearn.preprocessing import MinMaxScaler
sc = MinMaxScaler(feature_range = (0, 1))
training_set_scaled = sc.fit_transform(np.float64(training_set))
training_set_scaled.shape
xtrain = []
ytrain = []
xtest = []
ytest = []
for i in range(time_steps,len(a)-1):
    if(i<length-1):
        xtrain.append(training_set_scaled[i-time_steps:i])
        ytrain.append(training_set_scaled[i-time_steps+1:i+1])
    else:
        xtest.append(training_set_scaled[i-time_steps:i])
        ytest.append(training_set_scaled[i-time_steps+1:i+1])

xtrain = np.array(xtrain)
ytrain = np.array(ytrain)
xtest = np.array(xtest[0:640])
ytest = np.array(ytest[0:640])
xtrain = xtrain[0:7168]
ytrain = ytrain[0:7168]
from keras.layers import LSTM,Dense,Input,Bidirectional
from keras.models import Model
input_layer = Input(batch_shape=(batch_size,time_steps,1))
lstm1 = Bidirectional(LSTM(units=time_steps,stateful=True,return_sequences=True))(input_layer)
lstm2 = Bidirectional(LSTM(time_steps,stateful=True,return_sequences=True))(lstm1)
l1 = Dense(units=10)(lstm2)
out = Dense(units=1)(l1)

model = Model(inputs=input_layer,outputs=out)
model.compile(optimizer='adam',loss = 'mae')
model.summary()
#model.reset_states()
model.fit(xtrain,ytrain,shuffle=False,epochs=epochs,batch_size=batch_size)
per = model.predict(xtest,batch_size=batch_size)
p = sc.inverse_transform(per[:,9])
y = sc.inverse_transform(ytest[:,9])
plt.plot(p-y, color = 'red')
plt.show()