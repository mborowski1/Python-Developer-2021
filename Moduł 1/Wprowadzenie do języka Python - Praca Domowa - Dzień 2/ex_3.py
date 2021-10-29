def format_date(day, month, year):
    if month < 1 or month > 12:
        return None

    month_28_numbers_aux = [i for i in range(1,28)]
    month_30_numbers_aux = [i for i in range(1,30)]
    month_31_numbers_aux = [i for i in range(1,31)]
    
    month_28 = [2]
    month_30 = [4, 6, 9, 11]
    month_31 = [1, 3, 5, 7, 8, 10, 12]

    if month in month_28 and day not in month_28_numbers_aux or month in month_30 and day not in month_30_numbers_aux or month in month_31 and day not in month_31_numbers_aux:
        return None

    months_dictionary = {1 : 'stycznia', 2 : 'lutego', 3 : 'marca', 4 : 'kwietnia', 5 : 'maja', 6 : 'czerwca', 7 : 'lipca', 8 : 'sierpnia', 9 : 'września', 10 : 'października', 11 : 'listopada', 12 : 'grudnia'}

    day_string = str(day)
    year_string = str(year)

    final = day_string + ' ' + months_dictionary[month] + ' ' + year_string

    return final

check = format_date(1, 1, 2020)
print(check)

check_2 = format_date(1, 20, 2020)
print(check_2)
