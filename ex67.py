#!/home/wizard/anaconda3/bin/python

from draw import Point

#Клас

class Rectangle(Point):
    
    def __init__(self, x = 0, y = 0, width = 0, height = 0):
        super().__init__(x,y)
        self.width = width
        self.height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, width):
        assert width >= 0, 'width must be >= 0'
        self.__width = width

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self,height):
        assert height >= 0, 'height must be >= 0'
        self.__height = height

    def __eq__(self, other):
        if not isinstance(other, Rectangle):
            return NotImplemented
        p = super().__eq__(other)
        return self.width == other.width and self.height == other.height and p

    def __str__(self):
        return super().__str__() + f'[{self.width}x{self.height}]'

    def draw(self):
        super().draw()
        print(f'Draw Rectangle [{self.width}x{self.height}]')

if __name__ == '__main__':
    rc1 = Rectangle(10,20,450,500)

    rc1.x = 1
    rc1.y = 3
    print(f'Rectangle:{rc1}')

    rc2 = Rectangle(4,5,100,200)

    if rc1 != rc2:
        print(f'{rc1} != {rc2}')

    rc2.draw()