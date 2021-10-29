import random

class Dice:
    
    TYPES_OF_DICE = [3, 4, 6, 8, 10, 12, 20, 100]
    
    def __init__(self, dice_type, number_of_rolls):
        if dice_type in Dice.TYPES_OF_DICE:
            self.dice_type = dice_type
        else:
            raise ValueError
        self.number_of_rolls = number_of_rolls

    def roll(self):
        result = random.randint( 1, self.dice_type)
        return result

    def __iter__(self):
        self.counter = self.number_of_rolls
        return self

    def __next__(self):
        if self.counter == 0:
            raise StopIteration
        self.counter -= 1
        return random.randint( 1, self.dice_type)

for throw in Dice(4, 2):
    print(throw)





