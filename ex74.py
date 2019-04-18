#!/home/wizard/anaconda3/bin/python

class Number:
    def __getattr__(self,attr):
        ch = attr[0]
        s = int(attr[1::])

        if ch == 'b':
            return bin(s)
        elif ch == 'o':
            return oct(s)
        elif ch == 'x':
            return hex(s)
        raise AttributeError('Valid prefixes b|o|x')


if __name__ == '__main__':
    num = Number()

    print(num.b7)
    print(num.o8)
    print(num.x10)