import random

class Dice:
    
    TYPES_OF_DICE = [3, 4, 6, 8, 10, 12, 20, 100]
    
    def __init__(self, dice_type):
        if dice_type in Dice.TYPES_OF_DICE:
            self.dice_type = dice_type
        else:
            raise ValueError

    def roll(self):
        result = random.randint( 1, self.dice_type)
        return result

a = Dice(4)
print(a.roll())
