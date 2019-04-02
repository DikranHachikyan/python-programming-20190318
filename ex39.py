#!/home/wizard/anaconda3/bin/python

def gen_squares(start,end):
    yield from ( x ** 2 for x in range(start,end))

if __name__ == '__main__':
    gs = gen_squares(5,10)

    print(next(gs))
    print(next(gs))
    print(next(gs))
    print(next(gs))