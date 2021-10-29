from flask import Flask
from datetime import datetime

app = Flask(__name__)

@app.route("/current_time")
def clock():
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    return(current_time)




if __name__ == "__main__":
    app.run(debug=True)
