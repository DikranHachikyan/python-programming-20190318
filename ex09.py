#!/home/wizard/anaconda3/bin/python

def main():
    # 1 + 2 + 3 + ... + 99 + 100
    i = 101
    suma = 0

    while i <= 100:
        suma += i
        i += 1
    else:
        print('...else...')

    print(f'1 + 2 + ... + 99 + 100 = {{{suma}}}')

main()