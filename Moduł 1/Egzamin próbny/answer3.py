def check_palindrome(word_thing):

    split_word_thing = word_thing.split()
    joined_split_word_thing = ''.join(split_word_thing)
    reversed_joined_split_word_thing = joined_split_word_thing[::-1]
    
    if joined_split_word_thing == reversed_joined_split_word_thing:
        return True

    else:
        return False

test_1 = 'drzewo'
test_2 = 'kobyła ma mały bok'

print(check_palindrome(test_1))
print(check_palindrome(test_2))


