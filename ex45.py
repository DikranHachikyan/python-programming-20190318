#!/home/wizard/anaconda3/bin/python

from time import time, sleep
from functools import wraps

def mesure(func):
    @wraps(func)
    def wrapper(*args,**kwargs):
        """wrapper function"""
        t = time()
        result = func(*args,**kwargs)
        print(f'{func.__name__} time:{ time() - t}, doc:{func.__doc__}')
        return result
    return wrapper

@mesure
def foo(sleep_time=0.3):
    """function foo, sleeps sleep_time seconds"""
    sleep(sleep_time)

@mesure
def get_squares(n):
    """Generates squares """
    return [ x ** 2 for x in range(1,n)]    

if __name__ == '__main__':
    foo(0.5)
    print(f'{foo.__name__} doc:{foo.__doc__}')

    ls = get_squares(5)
    print(f'ls:{ls}')