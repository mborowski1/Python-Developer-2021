def mean(numbers):
    the_sum_of_numbers = 0
    the_number_of_elements_in_the_list = len(numbers)
    for i in numbers:
        the_sum_of_numbers += i
    the_mean = the_sum_of_numbers / the_number_of_elements_in_the_list
    return the_mean

the_list = [10, 20, 30]
check = mean(the_list)
print(check)
