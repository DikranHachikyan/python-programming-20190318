#!/home/wizard/anaconda3/bin/python

from collections import namedtuple

if __name__ == '__main__':
    Const = namedtuple('_',['PORT','HOST'])(3000,'localhost')

    

    print(f'Address:{Const.HOST}:{Const.PORT}')