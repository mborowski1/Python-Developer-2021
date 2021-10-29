from flask import Flask, request
from datetime import datetime
import random, requests

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def name_thing():
    
    
    
    if request.method == "GET":
        
        info_GET = "Wysłałeś GET"
        
        return info_GET

    if request.method == "POST":
        
        info_POST = "Wysłałeś POST"
        
        return info_POST
        
        
        


if __name__ == "__main__":
    app.run(debug=True)
