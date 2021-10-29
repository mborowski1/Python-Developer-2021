from flask import Flask, request
from datetime import datetime
import random, requests

app = Flask(__name__)

@app.route("/calculator_thing", methods=["GET", "POST"])
def name_thing():
    form_thing = '''
    <html>
    <form action="/calculator_thing" method="POST">
    <label>
    Wprowadź pierwszą liczbę:
    <input type="text" name="the_first_number_thing">
    </label>
    <label>
    Wprowadź drugą liczbę:
    <input type="text" name="the_second_number_thing">
    </label>
    <label>
    <select name="what" id="what_thing">
    <option value="+">+</option>
    <option value="-">-</option>
    <option value="*">*</option>
    <option value="/">/</option>
    </select>
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
        first_number = request.form["the_first_number_thing"]
        second_number = request.form["the_second_number_thing"]
        the_sign_thing = request.form["what"]
        int_first_number = int(first_number)
        int_second_number = int(second_number)
        if the_sign_thing == "+":
            return str(int_first_number + int_second_number)
        if the_sign_thing == "-":
            return str(int_first_number - int_second_number)
        if the_sign_thing == "*":
            return str(int_first_number * int_second_number)
        if the_sign_thing == "/":
            return str(int_first_number / int_second_number)


if __name__ == "__main__":
    app.run(debug=True)
