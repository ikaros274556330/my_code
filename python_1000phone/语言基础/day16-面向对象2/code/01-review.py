"""__author__=吴佩隆"""


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance(self, other):
        return ((self.x - other.x) ** 2 + (self.y - other.y) ** 2) ** 0.5


class Circle:
    pi = 3.141592653

    def __init__(self, r, point):
        self.point = point
        self.r = r

    def area(self):
        return Circle.pi * self.r ** 2

    def zhouchang(self):
        return Circle.pi * 2 * self.r

    def center_distance(self, other):
        return self.point.distance(other.point)


c1 = Circle(5, Point(0, 0))

c2 = Circle(3, Point(10, 10))

print(c1.center_distance(c2))

print(c1.r)
