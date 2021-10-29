def find_short_words(the_list):
    the_final_list = []
    for i in the_list:
        if len(i) < 5:
            the_final_list.append(i)
    return the_final_list

the_list_thing = ['Co', 'tam', 'człowieku']
check = find_short_words(the_list_thing)
print(check)
