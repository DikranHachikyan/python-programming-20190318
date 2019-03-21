#!/home/wizard/anaconda3/bin/python

def main():
    # 2 + 4 + ... + 98 + 100
    i = 1
    suma = 0

    while i <= 100:
        i += 1
        if (i % 2) == 0:
            suma += i
    else:
        print('...else...')

    print(f'2 + 4 + ... + 98 + 100 = {{{suma}}}')

main()