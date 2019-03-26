#!/home/wizard/anaconda3/bin/python

def sumNumbers(n):
    if n > 0:
        return n + sumNumbers(n-1)
    return 0
    

if __name__ == '__main__':
    x = 5
    result = sumNumbers(x)
    print(result)
