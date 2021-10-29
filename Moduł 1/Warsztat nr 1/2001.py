import random

player_points = 0
computer_points = 0

input('Press enter.')

player_throw_1 = random.randint(1, 6)
player_throw_2 = random.randint(1, 6)

computer_throw_1 = random.randint(1, 6)
computer_throw_2 = random.randint(1, 6)

player_points += player_throw_1
player_points += player_throw_2

computer_points += computer_throw_1
computer_points += computer_throw_2

print(f'You have {player_points} points.')
print(f'Computer has {computer_points} points.')

while player_points < 2001 and computer_points < 2001:

    input('Press enter.')

    player_throw_1 = random.randint(1, 6)
    player_throw_2 = random.randint(1, 6)

    computer_throw_1 = random.randint(1, 6)
    computer_throw_2 = random.randint(1, 6)

    if player_throw_1 + player_throw_2 == 7:

        player_points //= 7


    if computer_throw_1 + computer_throw_2 == 7:

        computer_points //= 7

    if player_throw_1 + player_throw_2 == 11:

        player_points *= 11

    if computer_throw_1 + computer_throw_2 == 11:

        computer_points *= 11

    if player_throw_1 + player_throw_2 != 7 and player_throw_1 + player_throw_2 != 11:

        player_points += player_throw_1
        player_points += player_throw_2

    if computer_throw_1 + computer_throw_2 != 7 and computer_throw_1 + computer_throw_2 != 11:
        
        computer_points += computer_throw_1
        computer_points += computer_throw_2

    print(f'You have {player_points} points.')
    print(f'Computer has {computer_points} points.')

if player_points >= 2001:

    print('Player won!')

if computer_points >= 2001:

    print('Computer won!')

























