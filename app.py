#! /Users/bobkwiencien/anaconda/bin/python
from flask import Flask, render_template
import psycopg2 as pg

app = Flask(__name__)

@app.route("/")
def index():
	msg="What would you like to do?"
	return render_template('index.html',messo=msg)

if __name__=='__main__':
    app.run(debug=True)    


