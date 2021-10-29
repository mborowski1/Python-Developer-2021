def validate_pesel(pesel):
    pesel_string = str(pesel)
    pesel_list = list(pesel_string)
    no_1 = int(pesel_list[0])
    no_2 = int(pesel_list[1])
    no_3 = int(pesel_list[2])
    no_4 = int(pesel_list[3])
    no_5 = int(pesel_list[4])
    no_6 = int(pesel_list[5])
    no_7 = int(pesel_list[6])
    no_8 = int(pesel_list[7])
    no_9 = int(pesel_list[8])
    no_10 = int(pesel_list[9])
    no_11 = int(pesel_list[10])

    check_1 = no_1 * 1
    check_2 = no_2 * 3
    check_3 = no_3 * 7
    check_4 = no_4 * 9
    check_5 = no_5 * 1
    check_6 = no_6 * 3
    check_7 = no_7 * 7
    check_8 = no_8 * 9
    check_9 = no_9 * 1
    check_10 = no_10 * 3

    sum_of_checks = check_1 + check_2 + check_3 + check_4 + check_5 + check_6 + check_7 + check_8 + check_9 + check_10

    sum_of_checks_divided_by_modulo = sum_of_checks % 10

    the_check_thing = 10 - sum_of_checks_divided_by_modulo

    if the_check_thing == 10:
        the_check_thing = 0

    if the_check_thing == no_11:
        return True
    else:
        return False

the_function_check = validate_pesel(12345678901)
print(the_function_check)
