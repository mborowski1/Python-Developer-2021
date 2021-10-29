from flask import Flask, request
from datetime import datetime
import random, requests

app = Flask(__name__)

@app.route("/name_thing", methods=["GET", "POST"])
def name_thing():
    form_thing = '''
    <html>
    <form action="/name_thing" method="POST">
    <label>
    Podaj imię:
    <input type="text" name="the_name_thing">
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
        user_name = request.form["the_name_thing"]
        return "Witaj " + user_name

if __name__ == "__main__":
    app.run(debug=True)
