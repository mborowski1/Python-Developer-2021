import random

def roll_the_dice(n):
    while n >= 1:
        n -= 1
        yield random.randint(1, 6)

for throw in roll_the_dice(5):
    print(throw)





