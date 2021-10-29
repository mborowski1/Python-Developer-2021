class Calculator:
    
    def __init__(self):
        self.list_of_operations = []
        
    def add(self, num1, num2):
        result = num1 + num2
        self.list_of_operations.append(f"added {num1} to {num2} got {result}")
        return result

    def multiply(self, num1, num2):
        result = num1 * num2
        self.list_of_operations.append(f"multiplied {num1} by {num2} got {result}")
        return result

    def print_operations(self):
        print(self.list_of_operations)




a = Calculator()
print(a.add(2, 2))
print(a.add(5, 10))
a.print_operations()

b = Calculator()
print(b.multiply(2, 2))
print(b.multiply(5, 10))
b.print_operations()

c = Calculator()
print(c.add(2, 8))
print(c.multiply(5, 10))
c.print_operations()

