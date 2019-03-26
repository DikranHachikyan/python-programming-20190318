#!/home/wizard/anaconda3/bin/python

def sumNumbers(a, b, *args ):
    c = a + b
    for v in args:
        c += v
    return c

def foo(ls):
    print(ls)    

if __name__ == '__main__':
    x,y = 10,2
    res = sumNumbers(x,y)
    print(f'{x} + {y} = {res}')

    res = sumNumbers(x,y,4,5,6,7,8)
    print(f'Result 1:{res}')

    l1 = [ v for v in range(1,15)]
    res = sumNumbers( x,y, *l1)
    print(f'{x} + {y}' + ' + '.join( str(v) for v in l1) + f' = {res}' )
    print(f'{x} + {y}' + ' + '.join( map(str,l1)) + f' = {res}' )

    #foo(l1)