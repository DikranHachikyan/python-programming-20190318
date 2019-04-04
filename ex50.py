#!/home/wizard/anaconda3/bin/python

from functools import wraps 

def brackets(left,right):
    def decorator(func):
        @wraps(func)
        def wrapper(lst,*args,**kwargs):
            lst = [ f'{left}{val}{right}' for val in lst]
            return func(lst,*args,**kwargs) # wrapper
        return wrapper # decorator
    return decorator   # brackets

@brackets('<','>')
def concat(lst):
    return ','.join(lst)


if __name__ == '__main__':
    nm = ['anna','john','maria','markus']
    print(concat(nm))   

    list = brackets('[',']')(list)

    nums = [1,2,3,4,5]

    print(list(nums))
