#!/home/wizard/anaconda3/bin/python

def main():
    lst = [ x ** 2 for x in range(10)]   

    print(lst)

    letters = [ v for v in 'hello python']

    print(letters)

    print('#'.join(letters))
main()