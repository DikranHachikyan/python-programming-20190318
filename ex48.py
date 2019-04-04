#!/home/wizard/anaconda3/bin/python


def factorial(n):
    if not hasattr(factorial,'cache'):
        factorial.cache = {}
    elif factorial.cache.get(n) is not None:
        print('return from cache')
        return factorial.cache[n]
    result = 1
    for i in range(2,n+1):
        result *= i
    factorial.cache[n] = result
    return result

if __name__ == '__main__':
    print(factorial(3))
    print(factorial(5))
    print(factorial(3))
    print(factorial(5))
    print(factorial(6))