def divide(a, b):

    try:
        a_int = int(a)
        b_int = int(b)
        string_a = str(a)
        list_a = list(string_a)
        first_list = list_a[0]
        first_list_int = int(first_list)
    except Exception:
        return None

    try:
        result_thing = a / b
        return result_thing
    except ZeroDivisionError:
        return None
        
check_1 = divide(20, 5)
print(check_1)

check_2 = divide('lol', 5)
print(check_2)

check_3 = divide(10, 'lol')
print(check_3)

check_4 = divide(10, 0)
print(check_4)


