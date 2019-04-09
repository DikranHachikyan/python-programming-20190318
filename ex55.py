#!/home/wizard/anaconda3/bin/python

# def foo():
#     return x

def suma(a,b):
        return a + b

if __name__ == '__main__':
    action = {
        '+':suma
    }

    try:
        a = int(input('value of a(int):'))
        op = input('Enter +, -, *, /:')
        b = int(input('value of b(int):'))
        print(f'{a} + {b} = {action[op](a,b)}')

    except KeyError as e1:
        print('Key error:', e1)
    except Exception as e1:
        print('Exception:',e1)
    else:
        print('else part')
    finally:
        print('finally (clean up)')