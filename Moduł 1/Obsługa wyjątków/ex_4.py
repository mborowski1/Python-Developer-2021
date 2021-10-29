def phone(number):

    try:
        numbers_list = [111111111, 222222222, 333333333]
        index = numbers_list.index(number)
    except Exception:
        return "Nie ma takiego numeru!"

    return "Dobry numer."

check_1 = phone(2)
print(check_1)

check_2 = phone(111111111)
print(check_2)
