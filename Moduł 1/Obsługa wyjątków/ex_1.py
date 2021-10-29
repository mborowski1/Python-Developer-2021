def safe_get(l, index):

    if type(l) != list:
        return 'l nie jest listą.'

    if type(index) != int:
        return 'index nie jest liczbą całkowitą.'
    
    try:
        return l[index]
    except IndexError:
        return None

check_1 = 'lol'
check_2 = 'lol_2'
check_3 = ['Hyzio', 'Dyzio', 'Zyzio']
check_4 = 2
check_wrong_number = 10

check_5 = safe_get(check_1, check_3)
print(check_5)

check_6 = safe_get(check_3, check_2)
print(check_6)

check_7 = safe_get(check_3, check_wrong_number)
print(check_7)

check_8 = safe_get(check_3, check_4)
print(check_8)





