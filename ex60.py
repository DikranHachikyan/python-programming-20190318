#!/home/wizard/anaconda3/bin/python

#Клас
class Point:
    # Конструктор на класа- инициализира данните на класа
    def __init__(self):
        print('Object Constructor')
        self.x = 10
        self.y = 12

if __name__ == '__main__':
    #p - обект, представител на класа
    p1 = Point()
    p2 = Point()

    print(f'Point 1:({p1.x},{p1.y})')
    print(f'Point 2:({p2.x},{p2.y})')
    print(type(p1))