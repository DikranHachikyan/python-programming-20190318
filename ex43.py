#!/home/wizard/anaconda3/bin/python

from time import time, sleep

def foo():
    sleep(0.3)

def bar():
    sleep(0.5)

def mesure(func):
    t = time()
    func()
    print(f'{func.__name__} time:{time()-t}')

if __name__ == '__main__':
    mesure(foo)
    mesure(bar)