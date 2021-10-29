def find_first_and_last(the_thing):
    the_new_thing = []
    the_new_thing.append(the_thing[0])
    the_new_thing.append(the_thing[-1])
    the_tuple_thing = tuple(the_new_thing)
    return the_tuple_thing

check_list_thing = [1, 2, 3, 4]
check_tuple_thing = (1, 2, 3, 4)

a = find_first_and_last(check_list_thing)
b = find_first_and_last(check_tuple_thing)

print(a)
print(b)



    
