#!/home/wizard/anaconda3/bin/python

def gen_letters(text):
    for t in text:
        yield t
    

if __name__ == '__main__':
    gn = gen_letters('Lorem ipsum dolor sit amet, consectetur')

    try:
        while True:
            print(next(gn))
    except StopIteration:
        pass