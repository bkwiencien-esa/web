#! /Users/bobkwiencien/anaconda/bin/python
from flask import Flask, render_template
import psycopg2 as pg
conn = ""
app = Flask(__name__)

@app.route("/")
@app.route("/dropo")
def index():
	conn = pg.connect(
    host="localhost",
    database="fw_telemetry")
	msg = buildDropDown(conn)
	return render_template('index.html',messo="",frm=msg)
	def dropo():
		return render_template('index.html',mess='done')
def buildDropDown(c):
	command = '<center><form action="/dropo"> '
	command = command + '<label for="tabs">Choose a table:</label> '
	command = command + '<select name="tabs" id="tabs"> '
	command = command + '<option value="fw_asset">fw_asset</option> '
	command = command + '<option value="fw_channel_state">fw_channel_state</option> '
	command = command + '</select> '
	command = command + '<br><br> '
	command = command + '<input type="submit" value="Submit"> '
	command = command + '</form></center>'
	return(command)
if __name__=='__main__':
    app.run(debug=True)    


