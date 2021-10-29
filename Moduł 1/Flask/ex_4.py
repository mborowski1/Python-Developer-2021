from flask import Flask
from datetime import datetime

app = Flask(__name__)

@app.route("/licz/<liczba1>/<liczba2>")
def adding(liczba1, liczba2):
    int_liczba1 = int(liczba1)
    int_liczba2 = int(liczba2)
    result_thing = int_liczba1 + int_liczba2
    str_result_thing = str(result_thing)
    return str_result_thing

if __name__ == "__main__":
    app.run(debug=True)
