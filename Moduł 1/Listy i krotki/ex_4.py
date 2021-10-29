def suma(numbers):
    sum_of_numbers = 0
    for i in numbers:
        sum_of_numbers += i
    return sum_of_numbers

the_list_of_numbers = [10, 15, 20]
check = suma(the_list_of_numbers)
print(check)

