#!/home/wizard/anaconda3/bin/python

def main():
    #1 + 2 + 4 + ... + 98 + 100
    i = 1
    suma = 0

    while i <= 100:
        suma += i
        if i == 3: break
        i += 1
    else:
        print('...else...')

    print(f'2 + 4 + ... + 98 + 100 = {{{suma}}}')

main()