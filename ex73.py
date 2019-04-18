#!/home/wizard/anaconda3/bin/python

def suma(a: float,b: float)->float:
    return a + b


if __name__ == '__main__':
    print('5 + 6 = ', suma(5,6))
    print('Py + thon = ', suma('Py', 'thon'))

    print(suma.__annotations__)
    