#!/home/wizard/anaconda3/bin/python

def show(a=None, b=None):
    if not a: a = []
    if not b: b = {}
    print(f'a:{a}')
    print(f'b:{b}')
    print('-' * 12)
    a.append(len(a))
    b[len(a)] = len(a)
      

if __name__ == '__main__':
    show()
    show([1,2,3], {'B':100})
    show()