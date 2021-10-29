import random

player_points = 0
computer_points = 0
available_dice = [3, 4, 6, 8, 10, 12, 20, 100]

player_die_1 = input('Select your first die. The dice you can choose from: D3, D4, D6, D8, D10, D12, D20, D100.')
player_die_2 = input('Select your second die. The dice you can choose from: D3, D4, D6, D8, D10, D12, D20, D100.')

player_die_1_list = list(player_die_1)
player_die_1_list.remove('D')
player_die_1_joined = ''.join(player_die_1_list)
player_die_1_int = int(player_die_1_joined)
player_result_1 = random.randint(1, player_die_1_int)


player_die_2_list = list(player_die_2)
player_die_2_list.remove('D')
player_die_2_joined = ''.join(player_die_2_list)
player_die_2_int = int(player_die_2_joined)
player_result_2 = random.randint(1, player_die_2_int)


computer_die_1 = available_dice[random.randint(0, 7)]
computer_die_2 = available_dice[random.randint(0, 7)]

computer_result_1 = random.randint(1, computer_die_1)
computer_result_2 = random.randint(1, computer_die_2)

player_points += player_result_1
player_points += player_result_2
computer_points += computer_result_1
computer_points += computer_result_2



print(f'You have {player_points} points.')
print(f'Computer has {computer_points} points.')


while player_points != 2001 and computer_points != 2001:

    player_die_1 = input('Select your first die. The dice you can choose from: D3, D4, D6, D8, D10, D12, D20, D100.')
    player_die_2 = input('Select your second die. The dice you can choose from: D3, D4, D6, D8, D10, D12, D20, D100.')

    player_die_1_list = list(player_die_1)
    player_die_1_list.remove('D')
    player_die_1_joined = ''.join(player_die_1_list)
    player_die_1_int = int(player_die_1_joined)
    player_result_1 = random.randint(1, player_die_1_int)


    player_die_2_list = list(player_die_2)
    player_die_2_list.remove('D')
    player_die_2_joined = ''.join(player_die_2_list)
    player_die_2_int = int(player_die_2_joined)
    player_result_2 = random.randint(1, player_die_2_int)


    computer_die_1 = available_dice[random.randint(0, 7)]
    computer_die_2 = available_dice[random.randint(0, 7)]

    computer_result_1 = random.randint(1, computer_die_1)
    computer_result_2 = random.randint(1, computer_die_2)

    player_points += player_result_1
    player_points += player_result_2
    computer_points += computer_result_1
    computer_points += computer_result_2

    if player_result_1 + player_result_2 == 7:

        player_points //= 7

    if player_result_1 + player_result_2 == 11:

        player_points *= 11

    if computer_result_1 + computer_result_2 == 7:

        computer_points //= 7

    if computer_result_1 + computer_result_2 == 11:

        computer_points *= 11

    print(f'You have {player_points} points.')
    print(f'Computer has {computer_points} points.')

if player_points == 2001 and computer_points == 2001:

    print("It's a tie!")

if player_points == 2001 and computer_points != 2001:

    print('Player won!')


if player_points != 2001 and computer_points == 2001:

    print('Computer won!')








