def histogram(the_list):
    the_result = ''
    
    for i in the_list:
        if isinstance(i, int) == False and isinstance(i, int) == False:
            return None
        while i > 0:
            the_result += '#'
            i -= 1
        if i == 0:
            the_result += '\n'
    return the_result

check = histogram([5, 8, 10])
print(check)



            


