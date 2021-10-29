def shorten(text_thing):
    
    first_letters = []
    text_thing_words = text_thing.split()

    for i in text_thing_words:

        a = list(i)
        first_letters.append(a[0])

    
    first_letters_as_one_word = ''.join(first_letters)
    final = first_letters_as_one_word.upper()

    return final

test = 'Dzień dobry.'
print(shorten(test))
