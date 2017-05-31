f = open('nohup.out')
err = 0
for i in f.readlines():
        err += float(i.split()[-1])
print err