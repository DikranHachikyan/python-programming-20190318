#!/home/wizard/anaconda3/bin/python

def gen_letters(txt):
    for t in txt:
        yield t

if __name__ == '__main__':
    gt = gen_letters('hello python')

    print(next(gt))
    print(next(gt))
    print(next(gt))