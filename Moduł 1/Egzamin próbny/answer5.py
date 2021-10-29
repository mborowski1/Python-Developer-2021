import random

def roll(number_of_dice, die_type=6, modifier=0):
    
    available_dice = [3, 4, 6, 8, 10, 12, 100]

    try:

        available_dice.remove(die_type)

    except Exception:

        return "No such die!"

    final_result = 0

    while number_of_dice > 0:

        roll_result = random.randint(1, die_type)
        final_result += roll_result
        final_result += modifier
        number_of_dice -= 1

    return final_result


    

test = roll(1)
print(test)
