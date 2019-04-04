#!/home/wizard/anaconda3/bin/python

# def foo():
#     return x

if __name__ == '__main__':
    try:
        a = int(input('value of a(int):'))
        b = int(input('value of b(int):'))
        print(f'{a} + {b} = {a+b}')
    except ValueError as e1:
        print('Exception:',e1)
    else:
        print('else part')
    finally:
        print('finally (clean up)')