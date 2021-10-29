def find_boundaries(the_list):
    
    final_list = []

    if len(the_list) < 1:
        return None

    for i in the_list:
        if isinstance(i, int) == False and isinstance(i, float) == False:
            the_list.remove(i)

    sorted_list = sorted(the_list)
    final_list.append(sorted_list[0])
    final_list.append(sorted_list[-1])
    final_tuple = tuple(final_list)

    return final_tuple

check_list = [1, 'drzewo', 15, 10]

check = find_boundaries(check_list)
print(check)
    
    
