from flask import Flask, request
from datetime import datetime
import random, requests, math

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def postcode_thing():
    
    
    
    if request.method == "GET":
        
        form_thing = '''
    <html>
    <form action="/" method="POST">
    <label>
    Podaj kod pocztowy:
    <input type="text" name="code">
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

        check_list = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        postcode = request.form["code"]
        postcode_list = list(postcode)
        
        if postcode_list[0] in check_list and postcode_list[1] in check_list and postcode_list[3] in check_list and postcode_list[4] in check_list and postcode_list[2] == '-' and len(postcode_list) == 6:
            message = 'Kod poprawny'
        else:
            message = 'Kod niepoprawny'
        
        return_thing = f'''
        
        <html>
        <head>
        
        </head>
        <body>
        %s
        </body>
        </html>
        ''' % (message)
        
        return return_thing


if __name__ == "__main__":
    app.run(debug=True)
