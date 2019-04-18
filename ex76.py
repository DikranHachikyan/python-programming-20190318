#!/home/wizard/anaconda3/bin/python

from collections import namedtuple

if __name__ == '__main__':
    Const = namedtuple('Const',['PORT','HOST'])

    const = Const(3000,'localhost')

    print(f'Address:{const.HOST}:{const.PORT}')