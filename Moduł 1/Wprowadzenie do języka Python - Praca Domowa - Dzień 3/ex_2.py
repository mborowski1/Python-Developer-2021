def div():
    number_one = input('Podaj pierwszą liczbę.')
    number_two = input('Podaj drugą liczbę.')

    try:
        number_one_int = int(number_one)
        number_two_int = int(number_two)
    except ValueError:
        return 'Można wprowadzać tylko liczby naturalne.'

    try:
        result_thing = number_one_int / number_two_int
    except ZeroDivisionError:
        return 'Nie można dzielić przez zero.'
    
    return result_thing

print(div())
