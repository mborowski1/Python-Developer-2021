from flask import Flask, request
from datetime import datetime
import random, requests

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def name_thing():
    
    
    
    
    if request.method == "GET":

        player_points = 0
        computer_points = 0
        available_dice = [3, 4, 6, 8, 10, 12, 20, 100]
        
        form_thing = f'''
    <html>
    <form action="/" method="POST">
    <label>
    Select your first die. The dice you can choose from: D3, D4, D6, D8, D10, D12, D20, D100.
    <input type="text" name="player_die_1">
    </label>
    <label>
    Select your second die. The dice you can choose from: D3, D4, D6, D8, D10, D12, D20, D100.
    <input type="text" name="player_die_2">
    </label>
    <label>
    <button type="submit">
    Wyślij
    </button>
    </label>
    <label>
    <input type="hidden" id="player_points" name="player_points" value="{player_points}">
    </label>
    <label>
    <input type="hidden" id="computer_points" name="computer_points" value="{computer_points}">
    </label>
    <label>
    <input type="hidden" id="available_dice" name="available_dice" value="{available_dice}">
    </label>
    </form>
    </html>
    '''

        return form_thing

    if request.method == "POST":

        player_points = request.form['player_points']
        computer_points = request.form['computer_points']
        available_dice = [3, 4, 6, 8, 10, 12, 20, 100]
        player_points = int(player_points)
        computer_points = int(computer_points)
        


        if player_points == 0 and computer_points == 0:


            available_dice = [3, 4, 6, 8, 10, 12, 20, 100]
            player_die_1 = request.form['player_die_1']
            player_die_2 = request.form['player_die_2']

        
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

            form_thing_2 = f'''
    <html>
    <form action="/" method="POST">
    <label>
    You have {player_points} points.
    </label>
    <label>
    Computer has {computer_points} points.
    </label>
    <label>
    Select your first die. The dice you can choose from: D3, D4, D6, D8, D10, D12, D20, D100.
    <input type="text" name="player_die_1">
    </label>
    <label>
    Select your second die. The dice you can choose from: D3, D4, D6, D8, D10, D12, D20, D100.
    <input type="text" name="player_die_2">
    </label>
    <label>
    <button type="submit">
    Wyślij
    </button>
    </label>
    <label>
    <input type="hidden" id="player_points" name="player_points" value="{player_points}">
    </label>
    <label>
    <input type="hidden" id="computer_points" name="computer_points" value="{computer_points}">
    </label>
    <label>
    <input type="hidden" id="available_dice" name="available_dice" value="{available_dice}">
    </label>
    </form>
    </html>
    '''
 
            return form_thing_2      

        if player_points != 0 and computer_points != 0 and player_points != 2001 and computer_points != 2001:

             

            available_dice = [3, 4, 6, 8, 10, 12, 20, 100]
            
            
            

            

            player_die_1 = request.form['player_die_1']
            player_die_2 = request.form['player_die_2']

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
        
            form_thing_3 = f'''
    <html>
    <form action="/" method="POST">
    <label>
    You have {player_points} points.
    </label>
    <label>
    Computer has {computer_points} points.
    </label>
    <label>
    Select your first die. The dice you can choose from: D3, D4, D6, D8, D10, D12, D20, D100.
    <input type="text" name="player_die_1">
    </label>
    <label>
    Select your second die. The dice you can choose from: D3, D4, D6, D8, D10, D12, D20, D100.
    <input type="text" name="player_die_2">
    </label>
    <label>
    <button type="submit">
    Wyślij
    </button>
    </label>
    <label>
    <input type="hidden" id="player_points" name="player_points" value="{player_points}">
    </label>
    <label>
    <input type="hidden" id="computer_points" name="computer_points" value="{computer_points}">
    </label>
    <label>
    <input type="hidden" id="available_dice" name="available_dice" value="{available_dice}">
    </label>
    </form>
    </html>
    '''

            return form_thing_3

        if player_points == 2001 and computer_points == 2001:

            return "It's a tie!"

        if player_points == 2001:

            return 'You won!'

        if computer_points == 2001:

            return 'Computer won!'

if __name__ == "__main__":
    app.run(debug=True)
