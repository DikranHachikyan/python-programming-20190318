#!/home/wizard/anaconda3/bin/python

from functools import wraps 

def memoize(func):
    cache = {}
    @wraps(func)
    def wrapper(*args,**kwargs):
        if args in cache:
            print('return from cache')
            return cache[args]
        result = func(*args,**kwargs)
        cache[args] = result
        return result
    return wrapper


def factorial(n):
    print('execute factorial')
    result = 1
    for i in range(2,n+1):
        result *= i
    return result

if __name__ == '__main__':
    factorial = memoize(factorial)
    print(factorial(3))
    print(factorial(5))
    print(factorial(3))
    print(factorial(5))
    print(factorial(6))