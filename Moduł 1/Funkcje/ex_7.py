def is_even(number):
    if number % 2 == 0:
        return True
    if number % 2 != 0:
        return False

a = is_even(2)
b = is_even(3)

print(a)
print(b)

def iterate_through(number):
    while number > 0:
        print(is_even(number))
        number -= 1

iterate_through(5)
