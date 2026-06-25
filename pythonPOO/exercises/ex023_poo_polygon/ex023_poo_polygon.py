from math import sqrt
from abc import ABC, abstractmethod


class Polygon(ABC):
    def __init__(self, sides: int):
        self.sides = sides

    @abstractmethod
    def perimeter(self):
        pass

    @abstractmethod
    def area(self):
        pass


class Square(Polygon):
    def __init__(self, side_length):
        super().__init__(sides = 4)
        self.side_length = side_length

    def perimeter(self):
        return self.sides * self.side_length

    def area(self):
        return self.side_length**2


class Circle(Polygon):
    def __init__(self, radius):
        super().__init__(sides = 0)
        self.radius = radius

    def diameter(self):
        return self.radius*2

    def perimeter(self):
        return 3.14 * (self.diameter())

    def area(self):
        return 3.14 * self.radius


class Triangle(Polygon):
    def __init__(self, a, b, c):
        super().__init__(sides=3)
        self.a = a
        self.b = b
        self.c = c

    def perimeter(self):
        return self.a + self.b + self.c

    def area(self):
        sp = self.perimeter()/2
        return sqrt(sp*(sp-self.a)*(sp-self.b)*(sp-self.c))


