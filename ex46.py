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


def max_result(limit=100):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            result = func(*args,**kwargs)
            if result > limit:
                print(f'Result over limit: {limit} result:{result}')
            return result
        return wrapper
    return decorator

@mesure
@max_result(120)
def cube(n):
    return n ** 3  

if __name__ == '__main__':
    print(cube(2))
    print(cube(5))