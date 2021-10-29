import random



game_list = ['1', '2', '3']

player_choice = input('Please enter: 1 - paper, 2 - rock or 3 - scissors.')

computer_choice = random.choice(game_list)

if player_choice == '1' and computer_choice == '1' or player_choice == '2' and computer_choice == '2' or player_choice == '3' and computer_choice == '3':
    print("It's a tie!")

elif player_choice == '1' and computer_choice == '3' or player_choice == '2' and computer_choice == '1' or player_choice == '3' and computer_choice == '2':
   print("Computer won!")

elif player_choice == '3' and computer_choice == '1' or player_choice == '1' and computer_choice == '2' or player_choice == '2' and computer_choice == '3':
   print("You won!")
