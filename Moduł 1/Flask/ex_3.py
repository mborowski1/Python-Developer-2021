from flask import Flask
from datetime import datetime

app = Flask(__name__)

@app.route("/current_date")
def date_provider():
    now = datetime.now()
    current_date = datetime.today().strftime("%Y:%m:%d")
    return(current_date)

if __name__ == "__main__":
    app.run(debug=True)
