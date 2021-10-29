import math

class Shape:

    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color

    def describe(self):
        print(self.x)
        print(self.y)
        print(self.color)

    def distance(self, other_shape):
        the_distance = math.sqrt((other_shape.x - self.x) ** 2 + (other_shape.y - self.y) **2)
        return the_distance

    def __str__(self):
        return f"Figura koloru {self.color} o środku w punkcie ({self.x}, {self.y})."

class Circle(Shape):

    def __init__(self, x, y, color, radius):
        super().__init__(x, y, color)
        self.radius = radius
        print(f'Stworzono okrąg koloru {self.color} o środku w punkcie ({self.x}, {self.y}), o promieniu {self.radius}.')

    def describe(self):
        print(self.x)
        print(self.y)
        print(self.color)

    def __str__(self):
        return f'Okrąg koloru {self.color} o środku w punkcie ({self.x}, {self.y}), o promieniu {self.radius}.'

    def area(self):
        return math.pi * self.radius ** 2

    def perimeter(self):
        return 2 * math.pi * self.radius

c1 = Circle(2, 4, 'zielony', 5)
c2 = Circle(1, 2, 'szary', 10)
print(c1.distance(c2))
print(c1)
print(c2)
print(c1.area())
print(c1.perimeter())
