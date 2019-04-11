#!/home/wizard/anaconda3/bin/python

#Клас
class Point:
    # Конструктор на класа- инициализира данните на класа
    def __init__(self, x=0, y=0, *args, **kwargs):
        #данни на обекта
        self._x = x
        self._y = y
    
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
        return Point(self._x + other._x, self._y + other._y)
    
    def __iadd__(self, other):
        ''' p1 = p1 + p2'''
        if not isinstance(other,Point):
            #raise TypeError('operand must be isnt. of Point)
            return NotImplemented
        self._x += other._x
        self._y += other._y
        return self

    def __str__(self):
        '''str(obj)->string'''
        return f'({self._x},{self._y})'

    def __repr__(self):
        '''Point representation
           eval(repr(obj))'''
        return f'Point({self._x},{self._y})'

    def __eq__(self,other):
        ''' if ob1 == ob2: ...'''
        if not isinstance(other, Point):
            return NotImplemented
        return self._x == other._x and self._y == other._y

    # методи на класа 
    def moveTo(self,dx,dy):
        self._x += dx
        self._y += dy

    def draw(self):
        print(f'Draw Point: ({self._x},{self._y})')
        

if __name__ == '__main__':
    p1 = Point(3, 4)
    p2 = Point(5, 6)

    p = p1 + p2
    print(f'New Point 1:{p}')

    p1 += p2
    print('P1:' + str(p1))
    # x = 10
    # p1 = p1 + x

    p = eval(repr(p1))
    if p == p1:
        print(f'New Point 2:{p}')

    p3 = Point(8,10)
    if p1 == p3:
        print(f'{p1} is eql to {p3}')
    
    if p1 != p2:
        print(f'{p1} is not eql to {p2}')