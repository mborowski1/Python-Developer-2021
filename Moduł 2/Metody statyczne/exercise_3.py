import datetime

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return "{} is {} years old.".format(self.name, self.age)

    @classmethod
    def create_person(cls, name, year_of_birth):
        now = datetime.datetime.now()
        current_year = now.year
        age = current_year - year_of_birth
        new_person = Person(name, age)
        return new_person

a = Person('Jerry', 20)
print(a)
b = a.create_person('Steve', 1980)
print(b)
