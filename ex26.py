#!/home/wizard/anaconda3/bin/python

value = 10

def main():
    global value
    value = 1
    print(f'value:{value}')   

def show():
    print(f'value:{value}')   

if __name__ == '__main__':
    main()
    show()