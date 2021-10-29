def dogs_age(age_thing):
    if age_thing <= 2:
        result_thing = age_thing * 10.5
    else:
        result_thing = 2 * 10.5 + 4 * (age_thing - 2)
    return result_thing

check = dogs_age(3)
print(check)
