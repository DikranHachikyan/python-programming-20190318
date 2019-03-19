#!/home/wizard/anaconda3/bin/python

def main():
    x = int(input('x='))

    if x < 10:
        print('{} < 10'.format(x))
    else:
        print('{} >= 10'.format(x))

main()