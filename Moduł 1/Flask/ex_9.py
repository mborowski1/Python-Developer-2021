from flask import Flask, request
from datetime import datetime
import random, requests

app = Flask(__name__)

@app.route("/zgadywanka_thing", methods=["GET", "POST"])
def name_thing():
    the_correct_answer = random.randint(1, 10)
    form_thing = '''
    <html>
    <form action="/zgadywanka_thing" method="POST">
    <label>
    Spróbuj zgadnąć liczbę:
    <input type="text" name="the_chosen_number">
    </label>
    <label>
    <button type="submit">
    Wyślij
    </button>
    </label>
    </form>
    </html>
    '''
    
    
    if request.method == "GET":
        
        return form_thing

    if request.method == "POST":
        
        the_chosen_number = request.form["the_chosen_number"]
        if int(the_chosen_number) < the_correct_answer:
            return "Za mało!" + form_thing
        if int(the_chosen_number) > the_correct_answer:
            return "Za dużo!" + form_thing
        if int(the_chosen_number) == the_correct_answer:
            return "Gratulacje, udało Ci się!" + form_thing
        


if __name__ == "__main__":
    app.run(debug=True)
