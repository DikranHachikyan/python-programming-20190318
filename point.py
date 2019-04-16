class Point:
    count = 0
    # Конструктор на класа- инициализира данните на класа
    def __init__(self, x=0, y=0, *args, **kwargs):
        #данни на обекта
        self.x = x
        self.y = y
        Point.count += 1
    
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

    def __del__(self):
        '''finalize()'''
        Point.count -=1

    #методи за достъп до данните

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self,x):
        assert x >= 0, 'x must be positive'
        self.__x = x
    #алтернативен подход
    #x = property(x)

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self,y):
        assert y >= 0, 'y must be positive'
        self.__y = y

    # методи на класа 
    def moveTo(self,dx,dy):
        self.x += dx
        self.y += dy

    def draw(self):
        print(f'Draw Point: ({self.x},{self.y})')

    @classmethod
    def fromPoint(cls,p):
        
        if not isinstance(p,cls):
            raise TypeError(f'param must be {cls}')
        return cls(p.x,p.y)

    # @staticmethod
    # def foo():
    #     draw()