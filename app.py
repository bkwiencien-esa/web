#! /Users/bobkwiencien/anaconda/bin/python
from flask import Flask, render_template
from flask import request
import psycopg2 as pg
conn = ""
app = Flask(__name__)

@app.route("/")
def index():
	conn = getConnection()
	msg = buildDropDown(conn)
	view = buildViewView(conn)
	return render_template('index.html',messo="<center><h4>What table's data would you like to examine?</h1></center>",frm=msg,frmv=view)	
@app.route("/dropo")	
def dropo():
	conn = getConnection()
	tabname=request.args.get('tabs')
	limit=request.args.get('limito')
	results = getTableHTML(conn,tabname)
	return render_template('tabledata.html',tdata='done')
def buildDropDown(c):
	c1 = c.cursor()
	c1.execute("select tablename from pg_tables where tablename like 'fw_%' order by tablename")
	tabrec = c1.fetchall()
	command = '<center><form action="/dropo" method="get"> '
	command = command + '<label for="tabs">Choose a table:</label> '
	command = command + '<select name="tabs" id="tabs"> '
	for tabo in tabrec:
		command = command + '<option value='+tabo[0]+'>'+tabo[0]+'</option>\n'
	command = command + '</select> '
	command = command + '<br><br> '
	command = command + '<label for="limito">Choose limit:</label>'
	command = command + '<select name="limito" id="limit">'
	command = command + '<option value="10">10</option>'
	command = command + '<option value="100">100</option>'
	command = command + '<option value="unlimited">unlimited</option>'
	command = command + '</select>'
	command = command + '<br><br> '
	command = command + '<input type="submit" value="submit">'
	command = command + '</form></center>'
	return(command)
def getTableHTML(c,tname):
	ll = getColumns(c,tname)
	selectstmt=buildSelect(tname,ll)
	tabhtml='<table id="tab1">'
	return("xoxox")	
def buildViewView(conn):
	return("<center><b>not done yet<b></center>")	
def getColumns(c,l):
	c1 = c.cursor()
	c1.execute("select column_name from information_schema.columns where table_name='{}' order by ordinal_position".format(l))
	colrec= c1.fetchall()
	listo =[xx for xx in colrec]
	for j in listo:
		print(j[0])
	return(listo)
def buildSelect(t,l):
	return('not done')	
def getConnection():
	conn = pg.connect(
	host="localhost",
	user="comm",
	database="fw_telemetry")
	return(conn)	
if __name__=='__main__':
    app.run(debug=True)    


