import matplotlib.pyplot as plt
import numpy as np
import sys

a = []
for i in range(129):
        b = []
        for j in range(135):
                b.append(0)
        a.append(b)

f = open('errors','r')
for i in f.readlines():
        if (i[:3] == str(sys.argv[1])):
                a[int(i.split()[1])][int(i.split()[2])] = float(i.strip().split()[-1])

#a = np.random.random((129, 135))

plt.imshow(a, cmap='hot', interpolation='nearest')
plt.show()
