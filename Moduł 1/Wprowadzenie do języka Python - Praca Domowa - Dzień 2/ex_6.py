def check_palindrome(word):
    word_as_list = list(word)
    changed_list = word_as_list[::-1]
    if word_as_list == changed_list:
        return True
    else:
        return False

check = 'kajak'
check_2 = check_palindrome(check)
print(check_2)
