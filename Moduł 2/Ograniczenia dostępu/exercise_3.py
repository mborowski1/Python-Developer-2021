class Employee:

    def __init__(self, id_number, first_name, last_name):
        self.id_number = id_number
        self.first_name = first_name
        self.last_name = last_name
        self._salary = 0.0
    
    def set_salary(self, salary):
        if isinstance(salary, int) == True or isinstance(salary, float) == True:
            if salary >= 0.0:
                 self._salary = salary

class HourlyEmployee(Employee):
    
    def __init__(self, id_number, first_name, last_name):
        super().__init__(id_number, first_name, last_name)
        
    def compute_payment(self, hours):
        return hours * self._salary


a = HourlyEmployee(1, 'Jan','Kowalski')
a.set_salary(500)
print(a.compute_payment(4))







