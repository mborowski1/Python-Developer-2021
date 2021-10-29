import random

computer_number = (random.randint(1, 100))

while True:
    player_number = input('Guess the natural number.')
    if '.' in list(player_number):
        print("It's not a natural number!")
        continue

    try:
        int_player_number = int(player_number)
    except Exception:
        print("It's not a natural number!")
        continue

    if int_player_number < computer_number:
        print("Too small!")
    elif int_player_number > computer_number:
        print("Too big!")
    else:
        print("You win!")
        break
        
