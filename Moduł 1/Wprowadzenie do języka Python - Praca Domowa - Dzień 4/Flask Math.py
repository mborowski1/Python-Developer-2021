from flask import Flask, request
from datetime import datetime
import random, requests, math

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def name_thing():
    
    
    
    if request.method == "GET":
        
        form_thing = '''
    <html>
    <form action="/" method="POST">
    <label>
    Wpisz liczbę naturalną n:
    <input type="text" name="n">
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

        str_n = request.form['n']
        n = int(str_n)
        
        n_power = 2 ** n
        n_n = n ** n
        n_factorial = math.factorial(n)
        
        table_thing = f'''
        
        <html>
        <head>
        
        </head>
        <body>
        
        <table border="1">
        <tr>
        <td> %s </td>
        <td> %d </td>
        <td> %f </td>
        </tr>        
        </table>
        </body>
        </html>
        ''' % (n_power, n_n, n_factorial)
        
        return table_thing


if __name__ == "__main__":
    app.run(debug=True)
