#!/home/wizard/anaconda3/bin/python

def sumNumbers(a, b, d = 0):
    c = a + b + d
    return c
    

if __name__ == '__main__':
    x,y = 10,2
    res = sumNumbers(x,y)
    print(f'{x} + {y} = {res}')

    z = 7
    res = sumNumbers(x,y,z)
    print(f'{x}+{y}+{z} = {res}')