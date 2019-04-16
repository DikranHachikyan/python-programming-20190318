from draw import Point
from draw import Shape
#Клас

class Rectangle(Point,Shape):
    
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