from flask import Flask, request
from datetime import datetime
import random, requests

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def name_thing():
    
    
    
    if request.method == "GET":
        
        form_thing = '''
    <html>
    <form action="/" method="POST">
    <label>
    Imię:
    <input type="text" name="first_name">
    </label>
    <label>
    Nazwisko:
    <input type="text" name="last_name">
    </label>
    <label>
    <button type="submit">
    Wyślij
    </button>
    </label>
    </form>
    </html>
    '''
        
        return form_thing

    if request.method == "POST":
        
        first_name = request.form["first_name"]
        second_name = request.form["last_name"]
        final = 'Witaj ' + first_name + ' ' + second_name
        
        return final
        
        
        


if __name__ == "__main__":
    app.run(debug=True)
