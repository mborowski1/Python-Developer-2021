from flask import Flask, request
from datetime import datetime
import random, requests

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def game_thing():
    
    
    
    if request.method == "GET":
        
        form_thing = '''
    <html>
    <form action="/" method="POST">
    <label>
    Pomyśl liczbę od 0 do 1000, a ja ją zgadnę w max. 10 próbach.
    </label>
    <label>
    <button id="submit_thing_thing" type="submit" name="submit_thing_thing" value="submit_thing_thing_1">
    Pomyślałem liczbę.
    </button>
    </label>
    <label>
    <input type="hidden" id="min" name="min" value="0">
    </label>
    <label>
    <input type="hidden" id="max" name="max" value="1000">
    </label>
    </form>
    </html>
    '''

        
        
        return form_thing

    if request.method == "POST":

        submit_thing_thing = request.form["submit_thing_thing"]

        if submit_thing_thing == "submit_thing_thing_1":

            min = 0
            max = 1000

            guess = int((max-min) / 2) + min

            form_thing_another = f'''
    <html>
    <form action="/" method="POST">
    <label>
    Zgaduję: {guess}.
    Czy zgadłem?
    </label>
    <label>
    <input type="hidden" id="min" name="min" value="0">
    </label>
    <label>
    <input type="hidden" id="max" name="max" value="1000">
    </label>
    <label>
    <input type="hidden" id="alt_min" name="alt_min" value="{guess}">
    </label>
    <label>
    <input type="hidden" id="alt_max" name="alt_max" value="{guess}">
    </label>
    <label>
    <button id="Zgadłeś." type="submit" name="question_thing" value="Zgadłeś.">Zgadłeś.</button>
    </label>
    <label>
    <button id="Za dużo!" type="submit" name="question_thing" value="Za dużo!">Za dużo!</button>
    </label>
    <label>
    <button id="Za mało!" type="submit" name="question_thing" value="Za mało!">Za mało!</button>
    </label>
    <label>
    <input type="hidden" id="min" name="submit_thing_thing" value="submit_thing_thing_2">
    </label>
    </form>
    </html>
    '''

            return form_thing_another

        

        the_submit_thing = request.form["question_thing"]
        
        if the_submit_thing == "Zgadłeś.":
    
            I_won = '''
        <html>
        <label>
        Wygrałem!
        </label>
        </html>
        '''
        
            return I_won

        if the_submit_thing == "Za dużo!":
        
            min = request.form["min"]
            max = request.form["alt_max"]

            int_min = int(min)
            int_max = int(max)

            guess = int((int_max-int_min) / 2) + int_min

            form_thing_another = f'''
    <html>
    <form action="/" method="POST">
    <label>
    Zgaduję: {guess}.
    Czy zgadłem?
    </label>
    <label>
    <input type="hidden" id="min" name="min" value="{min}">
    </label>
    <label>
    <input type="hidden" id="max" name="max" value="{max}">
    </label>
    <label>
    <input type="hidden" id="alt_min" name="alt_min" value="{guess}">
    </label>
    <label>
    <input type="hidden" id="alt_max" name="alt_max" value="{guess}">
    </label>
    <label>
    <button id="Zgadłeś." type="submit" name="question_thing" value="Zgadłeś.">Zgadłeś.</button>
    </label>
    <label>
    <button id="Za dużo!" type="submit" name="question_thing" value="Za dużo!">Za dużo!</button>
    </label>
    <label>
    <button id="Za mało!" type="submit" name="question_thing" value="Za mało!">Za mało!</button>
    </label>
    <label>
    <input type="hidden" id="min" name="submit_thing_thing" value="submit_thing_thing_2">
    </label>
    </form>
    </html>
    '''

            return form_thing_another

        if the_submit_thing == "Za mało!":
        
            min = request.form["alt_min"]
            max = request.form["max"]

            int_min = int(min)
            int_max = int(max)

            guess = int((int_max-int_min) / 2) + int_min

            form_thing_another = f'''
    <html>
    <form action="/" method="POST">
    <label>
    Zgaduję: {guess}.
    Czy zgadłem?
    </label>
    <label>
    <input type="hidden" id="min" name="min" value="{min}">
    </label>
    <label>
    <input type="hidden" id="max" name="max" value="{max}">
    </label>
    <label>
    <input type="hidden" id="alt_min" name="alt_min" value="{guess}">
    </label>
    <label>
    <input type="hidden" id="alt_max" name="alt_max" value="{guess}">
    </label>
    <label>
    <button id="Zgadłeś." type="submit" name="question_thing" value="Zgadłeś.">Zgadłeś.</button>
    </label>
    <label>
    <button id="Za dużo!" type="submit" name="question_thing" value="Za dużo!">Za dużo!</button>
    </label>
    <label>
    <button id="Za mało!" type="submit" name="question_thing" value="Za mało!">Za mało!</button>
    </label>
    <label>
    <input type="hidden" id="min" name="submit_thing_thing" value="submit_thing_thing_2">
    </label>
    </form>
    </html>
    '''
        
            return form_thing_another
        
        
        


if __name__ == "__main__":
    app.run(debug=True)
