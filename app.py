#! /Users/bobkwiencien/anaconda/bin/python
from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "Hello Lizard Lips!!"

if __name__=='__main__':
    app.run(debuf=True)    


