class Employee:

    def __init__(self, id_number, first_name, last_name):
        self.id = id_number
        self.first_name = first_name
        self.last_name = last_name
        self._salary = 0.0
    
    def set_salary(self, salary):
        if isinstance(salary, int) == True or isinstance(salary, float) == True:
            if salary >= 0.0:
                 self._salary = salary

a = Employee(1, 'Jan', 'Kowalski')
a.set_salary(20000)
print(a._salary)
print(a.first_name)

