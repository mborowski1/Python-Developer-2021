def create_list(a, b):
    the_list = [a, b]
    the_final_list = the_list + the_list + the_list + the_list
    return the_final_list

check = create_list(1, 2)
print(check)
