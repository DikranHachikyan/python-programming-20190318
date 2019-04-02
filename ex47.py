#!/home/wizard/anaconda3/bin/python

from functools import wraps

def capitalLetters(func):
    @wraps(func)
    def wrapper(sep,*args):
        args = [ v.upper() for v in args]
        return func(sep, *args)
    return wrapper    

def brackets(func):
    @wraps(func)
    def wrapper(sep,*args):
        args = [ '[{}]'.format(v) for v in args]
        return func(sep,*args)
    return wrapper    

@capitalLetters
@brackets
def concat(sep,*args):
    """Join args with sep"""
    return sep.join(args)

if __name__ == '__main__':
    langs = ['python','c++','java','c']

    print(concat('|', 'john','anna','maria'))
    print(concat('::', *langs))