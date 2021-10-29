import exam
from flask import Flask, request
from datetime import datetime
import random, requests

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def film_thing():
    
    
    
    if request.method == "GET":
        
        form_thing = '''
    <html>
    <form action="/" method="POST">
    <label>
    Insert title
    <input type="text" name="title">
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

        title = request.form['title']
        
        if title in exam.movies['favourite']:
            answer = '''
    <html>
    
    <label>
    favourite
    </label>
    
    </html>
    '''

            return answer
            
        if title in exam.movies['hated']:    
            answer = '''
    <html>
    
    <label>
    hated
    </label>
    
    </html>
    '''
        
            return answer

        else:
            answer = '''
    <html>
    
    <label>
    no such movie!
    </label>
    
    </html>
    '''

        return answer

if __name__ == "__main__":
    app.run(debug=True)
