#!/home/wizard/anaconda3/bin/python

from time import time, sleep

def foo(sleep_time=0.3):
    """function foo, sleeps sleep_time seconds"""
    sleep(sleep_time)
    

def mesure(func):
    def wrapper(*args,**kwargs):
        """wrapper function"""
        t = time()
        func(*args,**kwargs)
        print(f'{func.__name__} time:{ time() - t}, doc:{func.__doc__}')
    return wrapper


if __name__ == '__main__':
    fn = mesure(foo)

    fn(0.5)

    print(f'{fn.__name__} doc:{fn.__doc__}')

    
