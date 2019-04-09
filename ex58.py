#!/home/wizard/anaconda3/bin/python

# def foo():
#     return x

def suma(a,b):
        return a + b

def calctulate():
    action = {
        '+':suma
    }

    try:
        a = int(input('value of a(int):'))
        op = input('Enter +, -, *, /:')
        b = int(input('value of b(int):'))
        return action[op](a,b)
    except ValueError:
        return 0 
    except KeyError:
        return 0
    finally:
        print('finally (clean up)')

if __name__ == '__main__':
    res = calctulate()
    print(f'result:{res}')