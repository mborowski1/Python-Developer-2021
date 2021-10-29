def message(input_dict):
    if "name" not in input_dict or "role" not in input_dict.keys() or "movie" not in input_dict:
        return None
    else:
        the_sentence = 'In %(movie)s, %(name)s is a %(role)s.' % input_dict
        return the_sentence

the_dictionary_thing = {

    "name" : "Han Solo",

    "role" : "smuggler",

    "movie" : "Star Wars"

}

check = message(the_dictionary_thing)
print(check)
    
