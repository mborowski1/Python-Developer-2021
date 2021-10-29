

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

calculator_1 = Calculator()
calculator_1.add(2, 2)
calculator_1.multiply(2, 5)
calculator_1.print_operations()

calculator_2 = Calculator()
calculator_2.add(5, 5)
calculator_2.multiply(4, 5)
calculator_2.print_operations()

calculator_3 = Calculator()
calculator_3.add(10, 20)
calculator_3.multiply(500, 1000)
calculator_3.print_operations()

