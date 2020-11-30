#! /Users/bobkwiencien/anaconda/bin/python
from flask import Flask, render_template
import psycopg2 as pg
conn = ""
app = Flask(__name__)

@app.route("/")
def index():
	conn = pg.connect(
    host="localhost",
    database="fw_telemetry")
	msg = buildDropDown(conn)
	return render_template('index.html',messo=msg)
def buildDropDown(c):
	return("xoxoxo")
if __name__=='__main__':
    app.run(debug=True)    


