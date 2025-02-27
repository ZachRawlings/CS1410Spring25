from abc import ABC, abstractmethod

class Shape(ABC):
    def __init__(self, side):
        self.side = side

    @abstractmethod
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side ** 2

class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2
    
r = Rectangle(5, 4)
t = Triangle(3, 6)
s = Square(4)
c = Circle(3)

shapes = []
shapes.append(r)
shapes.append(t)
shapes.append(s)
shapes.append(c)

for shape in shapes:
    print(shape.area())