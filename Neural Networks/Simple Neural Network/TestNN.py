from keras.models import load_model


model = load_model('SimpleNeuralNetwork.m')

def fun(line):
        a = line.strip().split()
        for i in range(len(a)):
                a[i] = float(a[i])
        #return MonthArray(int(a[0])%12)+
        return a[3:]

f = open('Test','r')
g = open('TestTrue','r')

X = []
Y = []
for line in f.readlines():
        #line2 = g.readline()
        if ('--' not in line): # and ('--' not in line2)):
                X.append(fun(line))
                # Y.append(float(line2.strip().split()[-1])+273.16)
                # print fun(line)


#print ('Reading Done') 
f.close()
# g.close()

#clf.predict(X)

def mod(a):
        if a > 0: return a
        return a
#clf = SGDRegressor() #SGDClassifier(loss="hinge", penalty="l2")
# print (X)
Y = model.predict(X)
	
for i in range(len(Y)):
        li = g.readline()
        if '--' not in li:
                print li.strip(),Y[i][0], mod(float(li.strip().split()[-1])+273.16-Y[i][0]-25.9)
        #pass

#print Y[0]
g.close()



#pickle.dump(clf, open('Model','wb'))
