#!/home/wizard/anaconda3/bin/python

def get_squares(n):
    return [ x**2 for x in range(n+1)]
      
def gen_squares(n):
    for x in range(n+1):
        yield x**2

if __name__ == '__main__':
    ls = get_squares(10)
    print(f'ls:{ls}')

    s = gen_squares(3)

    for x in s:
        print(f'x:{x}')