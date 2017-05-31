from sklearn.linear_model import SGDRegressor, SGDClassifier
import pickle

def fun(line):
        a = line.strip().split()
        for i in range(len(a)):
                a[i] = float(a[i])
        return a[3:]



f = open('Train','r')
g = open('TrainTrue','r')
X = []
Y = []
for line in f.readlines():
        line2 = g.readline()
        if (('--' not in line) and ('--' not in line2)):
                X.append(fun(line))
                Y.append(float(line2.strip().split()[-1])+273.16)
                #print fun(line)


print ('Reading Done')
f.close()


clf = SGDRegressor(eta0=0.000001) #SGDClassifier(loss="hinge", penalty="l2")
#print (X)
#print (Y:10])
clf.fit(X, Y)

pickle.dump(clf, open('Model','wb'))