#!/home/wizard/anaconda3/bin/python

def gen_squares(start,end):
    yield from ( x ** 2 for x in range(start,end))

if __name__ == '__main__':
    ls = list(gen_squares(5,10))
    print(f'ls:{ls}')