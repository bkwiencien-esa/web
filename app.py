#! /Users/bobkwiencien/anaconda/bin/python
from flask import Flask, render_template
from flask import request
import psycopg2 as pg
import pdb
conn = ""
app = Flask(__name__)

@app.route("/")
def index():
	conn = getConnection()
	msg = buildDropDown(conn)
	return render_template('index.html',messo="<center><h4>What table's/view's data would you like to examine?</h1></center>",frm=msg)	
@app.route("/dropo")	
def dropo():
	conn = getConnection()  
	tabname=request.args.get('tabs')
	limit=request.args.get('limito')
	results = getTableHTML(conn,tabname,limit)
	return render_template('tabledata.html',tablename=tabname,tdata=results)
def buildDropDown(c):
	c1 = c.cursor()
	c1.execute("select tablename from pg_tables where tablename like 'fw_%' "
		+ "	union select viewname as tablename from pg_views where viewname  like 'fw%'order by tablename")
	tabrec = c1.fetchall()
	command = '<center><form action="/dropo" method="get"> '
	command = command + '<label for="tabs">Choose a table:</label> '
	command = command + '<select name="tabs" id="tabs"> '
	for tabo in tabrec:
		command = command + '<option value='+tabo[0]+'>'+tabo[0]+'</option>\n'
	command = command + '</select> '
	command = command + '<br><br> '
	command = command + '<label  for="limito">Choose limit:</label>'
	command = command + '<select name="limito" id="limit">'
	command = command + '<option value="10">10</option>'
	command = command + '<option value="100">100</option>'
	command = command + '<option value="unlimited">unlimited</option>'
	command = command + '</select>'
	command = command + '<br><br> '
	command = command + '<input type="submit" value="submit">'
	command = command + '</form></center>'
	return(command)
def getTableHTML(c,tname,limito):
	ll = getColumns(c,tname)
	selectstmt=buildSelect(tname,ll,limito)
	c1 = c.cursor()
	c1.execute(selectstmt)
	xoxo = c1.fetchall()
	tabhtml='<table id="tab1"> '
	tabhtml=tabhtml+'<tr> '
	for cn in ll:
		tabhtml=tabhtml+'<th>'+cn[0]+'</th> '	
	for x in xoxo:
		tabhtml=tabhtml+"<tr> "
		for j in x:
			tabhtml=tabhtml + "<td> " + str(j) + "</td> "	
		tabhtml=tabhtml+" </tr> "   	
	tabhtml=tabhtml+'</tr></table>' 	
	return(tabhtml)	
def getColumns(c,l):
	c1 = c.cursor()
	c1.execute("select column_name from information_schema.columns where table_name='{}' order by ordinal_position".format(l))
	colrec= c1.fetchall()
	listo =[xx for xx in colrec]
	return(listo)
def buildSelect(t,l,lim):
	limdic = {"10": "limit 10","100":"limit 100","unlimited": ""}
	llx = limdic[lim]
	selectlist=""
	for c in l:
		selectlist = selectlist +"\"" + c[0]+ "\"" +", "
	selectlist = selectlist[:-2]	
	query = "select " + selectlist + " from " + t + " " + llx
	print(query)
	return(query)	
def getConnection():
	conn = pg.connect(
	host="localhost",
	user="comm",
	database="fw_telemetry")
	return(conn)	
if __name__=='__main__':
    app.run(debug=True)    


