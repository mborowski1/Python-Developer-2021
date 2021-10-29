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

shape_1 = Shape(1, 2, 'zielony')
shape_2 = Shape(5, 10, 'niebieski')
print(shape_1.distance(shape_2))

shape_1.describe()

print(shape_1)


