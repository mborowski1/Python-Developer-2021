from flask import Flask
from datetime import datetime
import random

app = Flask(__name__)

@app.route("/random_thing")
def random_thing():
    number_1 = random.randint(1, 100)
    number_2 = random.randint(1, 100)
    number_3 = random.randint(1, 100)
    str_number_1 = str(number_1)
    str_number_2 = str(number_2)
    str_number_3 = str(number_3)
    final_return = str_number_1 + ', ' + str_number_2 + ', ' + str_number_3
    return final_return

if __name__ == "__main__":
    app.run(debug=True)
