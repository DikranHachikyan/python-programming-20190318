#!/home/wizard/anaconda3/bin/python

#Клас
class Point:
    # Конструктор на класа- инициализира данните на класа
    def __init__(self, x=0, y=0, *args, **kwargs):
        print('Object Constructor')
        #данни на класа
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
    p1 = Point()
    p2 = Point(7,8)

    p1.draw()
    p1.moveTo(-5, 15)
    p1.draw()