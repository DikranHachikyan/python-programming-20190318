#!/home/wizard/anaconda3/bin/python

#Клас
class Point:
    #променлива на класа
    label = 'A'
    # Конструктор на класа- инициализира данните на класа
    def __init__(self, x=0, y=0, *args, **kwargs):
        print('Object Constructor')
        #данни на обекта
        self._x = x
        self._y = y
    
    # методи на класа 
    def moveTo(self,dx,dy):
        self._x += dx
        self._y += dy

    def draw(self):
        print(f'Draw Point: ({self._x},{self._y})')
        

if __name__ == '__main__':
    #p - обект, представител на класа
    p1 = Point(4,5)
    p2 = Point(3,6)

    p1.z = 100

    print(f'p1.z={p1.z}')
    #В p2 няма z. z е динамично "закачена" променлива към обекта
    #print(f'p2.z={p2.z}')