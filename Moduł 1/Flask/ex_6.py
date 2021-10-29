from flask import Flask
from datetime import datetime
import random

app = Flask(__name__)

@app.route("/lotek")
def lotek_thing():
    random_list = [ x for x in range(1, 50)]
    random.shuffle(random_list)
    final_list = random_list[0:6]
    string_1 = str(final_list[0])
    string_2 = str(final_list[1])
    string_3 = str(final_list[2])
    string_4 = str(final_list[3])
    string_5 = str(final_list[4])
    string_6 = str(final_list[5])

    final_return = string_1 + ", " + string_2 + ", " + string_3 + ", " + string_4 + ", " + string_5 + ", " + string_6

    return final_return

if __name__ == "__main__":
    app.run(debug=True)
