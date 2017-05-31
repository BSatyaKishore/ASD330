from keras.models import Model, Sequential
from keras.layers import Input, Dense
#import h5py
#from keras.models import load_model
#a = Input(shape=(32,))
#b = Dense(32)(a)
#model = Model(inputs=a, outputs=b)

model = Sequential()
model.add(Dense(16, input_dim=27))
model.add(Dense(1, activation='linear'))
model.compile(optimizer='rmsprop',loss='mse') #,metrics=['accuracy'])

# model.compile(optimizer='rmsprop',
#              loss='mse')

def my_float(a):
	if a == '--':
		return 0
	else:
		return float(a)

def ReadLine(line):
	a = line.split()[3:]
	a = [my_float(i) for i in a]
	return a

f = open('Train')

data = []
labels = []
g = open('TrainTrue')

for i in f.readlines():
	j = ReadLine(i)
	data.append(j)
	labels.append(my_float(g.readline().strip().split()[-1])+273.15)

g.close()
f.close()
	#print len(data[0])
	#break 
# data = [list(i) for i in zip(*data)]
'''
import numpy as np
data = np.random.random((1000, 100))
labels = np.random.randint(2, size=(1000, 1))
print len(data)
print len(data[0])
'''
# for 
# Train the model, iterating on the data in batches of 32 samples
model.fit(data, labels, batch_size=128) 
import h5py

'''
import cPickle
f = open('SimpleNeuralNetwork.m','wb')
cPickle.dump(model,f)
'''
model.save('SimpleNeuralNetwork.m')
