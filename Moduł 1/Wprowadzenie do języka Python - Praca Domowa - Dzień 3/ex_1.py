import random

def random_average(n):
    
    numbers_list = []
    sum_of_numbers = 0
    n_used = n
    
    while n_used > 0:
        random_number = random.randint(1, 100)
        numbers_list.append(random_number)
        n_used -= 1

    for i in numbers_list:
        sum_of_numbers += i

    the_average = sum_of_numbers / n

    return the_average

check_1 = random_average(10)
print(check_1)
