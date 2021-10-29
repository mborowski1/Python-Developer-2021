def censor(text_thing):
    list_of_words = text_thing.split()
    forbidden_words = ['Java', 'C#', 'Ruby', 'PHP']
    
    for i in list_of_words:
        if i in forbidden_words:
            index_thing = list_of_words.index(i)
            list_of_words[index_thing] = '****'


    final_list_of_words = ' '.join(list_of_words)

    return final_list_of_words

check = 'To Ruby i PHP oraz Java'
check_2 = censor(check)
print(check_2)
