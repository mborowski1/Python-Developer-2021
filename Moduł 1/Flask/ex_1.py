from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "Witaj użytkowniku!"

@app.route("/hello/<imie>")
def hello_name(imie):
    return imie

if __name__ == "__main__":
    app.run(debug=True)

