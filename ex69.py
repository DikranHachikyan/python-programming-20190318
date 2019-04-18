#!/home/wizard/anaconda3/bin/python

from draw import Point
from draw import Rectangle
from math import sqrt

class ShapeUtils:

    @staticmethod
    def distance(p1,p2):
        if not isinstance(p1,Point) or not isinstance(p2,Point):
            raise TypeError('params must be instances of Point')
        dx = p1.x - p2.x
        dy = p1.y - p2.y
        return sqrt( dx**2 + dy**2)

if __name__ == '__main__':
    p1 = Point(9,8)
    p2 = Point(6,4)

    print(f'dist: {p1} and {p2} -> {ShapeUtils.distance(p1,p2)}')

    rc1 = Rectangle(40,20,120,304)
    rc2 = Rectangle(30,21,340,500)

    print(f'{rc1} {rc2} -> {ShapeUtils.distance(rc1,rc2)}')
