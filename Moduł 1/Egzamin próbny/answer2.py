def name_sorter(list_of_names_thing):
    
    final_dict = {}
    male_names_list = []
    female_names_list = []

    for i in list_of_names_thing:

        word_as_list = list(i)
        last_letter = word_as_list[-1]

        if last_letter != 'a':
            male_names_list.append(i)

        else:
            female_names_list.append(i)

    final_dict['female'] = female_names_list
    final_dict['male'] = male_names_list

    return final_dict

test = ['Jan', 'Anna', 'Ewa', 'Elżbieta', 'Stefan', 'Aleksander']
print(name_sorter(test))
