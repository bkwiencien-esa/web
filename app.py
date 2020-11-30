#! /Users/bobkwiencien/anaconda/bin/python
from flask import Flask, render_template
import psycopg2 as pg
conn = ""
app = Flask(__name__)

@app.route("/")
def index():
	msg = buildDropDown()
	return render_template('index.html',messo=msg)
def buildDropDown():
	return("<center><h4>What table's data would you like to examine?</h1></center>")
if __name__=='__main__':
    app.run(debug=True)    


