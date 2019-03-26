#!/home/wizard/anaconda3/bin/python

#Глобална променлива (в целия скрипт)
portNumber = 3000 
#1.декларация
def sumNumbers(a,b):
    # c - локална променлива (вижда се само тук)
    c = a + b
    return c #връща стойността там е извикана фунцията

if __name__ == '__main__':
    #2. извикване
    x, y = 4,8
    s = sumNumbers(x,y)
    print(f'{x} + {y} = {s}')
