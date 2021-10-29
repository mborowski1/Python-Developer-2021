import math

class Calculator:
	
	def __init__(self):
		self.list_thing = []

	def add(self, num1, num2):
		result = num1 + num2
		self.list_thing.append(f"added {num1} to {num2} got {result}")
		print(f"Wynik: {result}")


	def multiply(self, num1, num2):
		result = num1 * num2
		self.list_thing.append(f"multiplied {num1} by {num2} got {result}")
		print(f"Wynik: {result}")

	def print_operations(self):
		print(self.list_thing)




class Shape:

	def __init__(self, x, y, color):
		self.x = x
		self.y = y
		self.color = color

	def __str__(self):
		return f"Figura koloru {self.color} o środku w punkcie {self.x}, {self.y}."

	def describe(self):
		print(f"{self.x}, {self.y}, {self.color}")
		
	def distance(self, another_shape):
		result_aux = (another_shape.x - self.x) ** 2 + (another_shape.y - self.y) ** 2
		result = math.sqrt(result_aux)
		print(f"The distance between the centres of the shapes = {result}")

shape_thing_1 = Shape(1, 2, "niebieski")
shape_thing_2 = Shape(3, 4, "zielony")

shape_thing_1.distance(shape_thing_2)

print(shape_thing_1)
print(shape_thing_2)

shape_thing_1.describe()
shape_thing_2.describe()
	




