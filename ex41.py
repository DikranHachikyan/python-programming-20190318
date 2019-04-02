#!/home/wizard/anaconda3/bin/python

from time import time

n = 5000

values = []
t = time()
for v in range(1,n):
    for s in range(v,n):
        values.append( divmod(v,s))
print('for loop:{:.4f}'.format(time() - t))

t = time()
values2 = [ divmod(v,s) for v in range(1,n) for s in range(v,n) ]
print('for expr:{:.4f}'.format(time() - t))

t = time()
values3 = list( ( divmod(v,s) for v in range(1,n) for s in range(v,n)))
print('gen expr:{:.4f}'.format(time() - t))