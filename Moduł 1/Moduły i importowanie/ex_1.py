from random import randint

def d6(num):
    the_roll = randint(1, 6)
    the_final_thing = the_roll * num
    return the_final_thing

check = d6(2)
print(check)
