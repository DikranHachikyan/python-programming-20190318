#!/home/wizard/anaconda3/bin/python

#Клас
class Point:
    # Конструктор на класа- инициализира данните на класа
    def __init__(self, x=0, y=0, *args, **kwargs):
        #данни на обекта
        self.x = x
        self.y = y
    
    # специални методи

    def __add__(self, other):
        ''' p1 = p1 + p2'''
        #1
        #assert isinstance(other,Point), 'operand must be isnt. of Point'
        #1.1 за конкретен атрибут
        #assert hasattr(other,'_x'), 'operand must have attr _x'
        #2.
        if not isinstance(other,Point):
            #raise TypeError('operand must be isnt. of Point)
            return NotImplemented
        return Point(self.x + other.x, self.y + other.y)
    
    def __iadd__(self, other):
        ''' p1 = p1 + p2'''
        if not isinstance(other,Point):
            #raise TypeError('operand must be isnt. of Point)
            return NotImplemented
        self.x += other.x
        self.y += other.y
        return self

    def __str__(self):
        '''str(obj)->string'''
        return f'({self.x},{self.y})'

    def __repr__(self):
        '''Point representation
           eval(repr(obj))'''
        return f'Point({self.x},{self.y})'

    def __eq__(self,other):
        ''' if ob1 == ob2: ...'''
        if not isinstance(other, Point):
            return NotImplemented
        return self.x == other.x and self.y == other.y

    #методи за достъп до данните

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self,x):
        assert x >= 0, 'x must be positive'
        self._x = x
    #алтернативен подход
    #x = property(x)


    @property
    def y(self):
        return self._y

    @y.setter
    def y(self,y):
        assert y >= 0, 'y must be positive'
        self._y = y

    # методи на класа 
    def moveTo(self,dx,dy):
        self.x += dx
        self.y += dy

    def draw(self):
        print(f'Draw Point: ({self.x},{self.y})')
        

if __name__ == '__main__':
    p1 = Point(3, 4)
    
    p1.x = 10
    p1.y = 12
    print(f'P1:{p1}')