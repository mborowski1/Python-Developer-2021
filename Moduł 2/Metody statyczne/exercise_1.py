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

class AdvancedCalculator(Calculator):
    PI = 3.14159265

    def __init__(self):
        super().__init__()

    @staticmethod
    def compute_circle_area(r):
        return 2 * AdvancedCalculator.PI * r

print(AdvancedCalculator.compute_circle_area(1))

# Metoda computer_circle_area nie może dodać wpisu do listy list_of_operations, ponieważ nie wykorzystuje self.
