import random

lotto_numbers = [x for x in range(1, 50)]
entered_numbers = []

while True:
    
    first_number = input('Enter the first number.')
    
    if '.' in list(first_number):
        print('It has to be a natural number.')
        continue

    try:
        int_first_number = int(first_number)
    except Exception:
        print('It has to be a natural number.')
        continue

    if int_first_number not in lotto_numbers:
        print('Enter the number larger than 0 and smaller than 50.')
        continue
    else:
        entered_numbers.append(int_first_number)
        break


while True:
    
    second_number = input('Enter the second number.')
    
    if '.' in list(first_number):
        print('It has to be a natural number.')
        continue

    try:
        int_second_number = int(second_number)
    except Exception:
        print('It has to be a natural number.')
        continue

    if int_second_number not in lotto_numbers:
        print('Enter the number larger than 0 and smaller than 50.')
        continue
    
    if int_second_number in entered_numbers:
        print('You have already entered that number.')
        continue
    else:
        entered_numbers.append(int_second_number)
        break

while True:
    
    third_number = input('Enter the third number.')
    
    if '.' in list(third_number):
        print('It has to be a natural number.')
        continue

    try:
        int_third_number = int(third_number)
    except Exception:
        print('It has to be a natural number.')
        continue

    if int_third_number not in lotto_numbers:
        print('Enter the number larger than 0 and smaller than 50.')
        continue
    
    if int_third_number in entered_numbers:
        print('You have already entered that number.')
        continue
    else:
        entered_numbers.append(int_third_number)
        break

while True:
    
    fourth_number = input('Enter the fourth number.')
    
    if '.' in list(fourth_number):
        print('It has to be a natural number.')
        continue

    try:
        int_fourth_number = int(fourth_number)
    except Exception:
        print('It has to be a natural number.')
        continue

    if int_fourth_number not in lotto_numbers:
        print('Enter the number larger than 0 and smaller than 50.')
        continue
    
    if int_fourth_number in entered_numbers:
        print('You have already entered that number.')
        continue
    else:
        entered_numbers.append(int_fourth_number)
        break

while True:
    
    fifth_number = input('Enter the fifth number.')
    
    if '.' in list(fifth_number):
        print('It has to be a natural number.')
        continue

    try:
        int_fifth_number = int(fifth_number)
    except Exception:
        print('It has to be a natural number.')
        continue

    if int_fifth_number not in lotto_numbers:
        print('Enter the number larger than 0 and smaller than 50.')
        continue
    
    if int_fifth_number in entered_numbers:
        print('You have already entered that number.')
        continue
    else:
        entered_numbers.append(int_fifth_number)
        break

while True:
    
    sixth_number = input('Enter the sixth number.')
    
    if '.' in list(sixth_number):
        print('It has to be a natural number.')
        continue

    try:
        int_sixth_number = int(sixth_number)
    except Exception:
        print('It has to be a natural number.')
        continue

    if int_sixth_number not in lotto_numbers:
        print('Enter the number larger than 0 and smaller than 50.')
        continue
    
    if int_sixth_number in entered_numbers:
        print('You have already entered that number.')
        continue
    else:
        entered_numbers.append(int_sixth_number)
        break

sorted_entered_numbers = sorted(entered_numbers)


print("Your numbers: ", sorted_entered_numbers)

winning_numbers = []
the_drawing = 6
while the_drawing > 0:
    x = random.randint(1, 49)
    winning_numbers.append(x)
    the_drawing -= 1

print(winning_numbers)

final_comment_number = 0

for i in entered_numbers:
    if i in winning_numbers:
        final_comment_number += 1

final_comment = f'You entered {final_comment_number} number(s) identical to the numbers selected at random by the computer.'

print(final_comment)




