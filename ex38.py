#!/home/wizard/anaconda3/bin/python

if __name__ == '__main__':
    squares1 = [ x ** 2 for x in range(10)]
    print(f'squares:{squares1}')

    squares2 = ( x ** 2 for x in range(10))

    print(next(squares2))
    print(next(squares2))
    print(next(squares2))