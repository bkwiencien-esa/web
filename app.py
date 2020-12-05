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
    user="comm",
    database="fw_telemetry")
	msg = buildDropDown(conn)
	view = buildViewView(conn)
	return render_template('index.html',messo="",frm=msg,frmv=view)
	def dropo():
		return render_template('index.html',messo='done')
def buildDropDown(c):
	c1 = c.cursor()
	c1.execute("select tablename from pg_tables where tablename like 'fw_%' order by tablename")
	tabrec = c1.fetchall()
	command = '<center><form action="/dropo" method="get"> '
	command = command + '<label for="tabs">Choose a table:</label> '
	command = command + '<select name="tabs" id="tabs"> '
	for tabo in tabrec:
		command = command + '<option value='+tabo[0]+'>'+tabo[0]+'</option>'
	command = command + '</select> '
	command = command + '<br><br> '
	command = command + '<input type="submit" value="Submit"> '
	command = command + '</form></center>'
	return(command)
def buildViewView(conn):
	return("<center><b>not done yet<b></center>")	
def getTables(c):
	listo = []
	return(listo)	
def getColumns(c,l):
	listo = []
	return(listo)	
if __name__=='__main__':
    app.run(debug=True)    


