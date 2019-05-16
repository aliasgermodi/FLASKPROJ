from flask import Flask, url_for, redirect, render_template, request, abort, session
from flask import Flask, render_template, render_template, redirect, url_for, request,g
from pymongo import MongoClient
import json
import datetime
from flask_pymongo import PyMongo
from flask import jsonify
from bson.json_util import dumps
import os


client = MongoClient('localhost:27017')
db = client.TaskDB
app = Flask(__name__)
app.secret_key = os.urandom(24)

#first page for feedabck
@app.route('/')
def hello_world():
   return render_template("index.html")

#login page and session management
@app.route('/login', methods=['GET', 'POST'])
def sess():

	error = None
	if request.method == 'POST':
		session.pop('user',None)
		if request.form['username'] =='admin' or request.form['password'] =='admin':
			session['user'] = request.form['username']
			return redirect(url_for('protected'))

	return render_template('login.html', error=error)

@app.route('/protected')
def protected():
	if g.user:
		return redirect(url_for('get_total_today'))

	return render_template('login.html')

@app.before_request
def before_request():
	g.user = None
	if 'user' in session:
		g.user = session['user']

@app.route('/getsession')
def getsession():
	if 'user' in session:
		return session['user']

	return 'User not logged in'

@app.route('/dropsession')
def dropsession():
	session.pop('user', None)
	return redirect(url_for('sess'))


#Service page to select the services.
@app.route('/ser_en')
def services_en():
   return render_template("serviceEN.html")

@app.route('/ser_ar')
def services_ar():
	   return render_template("serviceAR.html")


#Restaurant 1 form page-English and arabic

@app.route('/rest1_en')
def rest1_en():
   return render_template("rest1_form_en.html")
@app.route('/rest1_ar')
def rest1_ar():
   return render_template("rest1_form_ar.html")

@app.route('/rest1_en', methods = ['POST'])
def rest1_form_en():
	try:
		#data = json.loads(request.data)
		#country = data['country']
		#project = "project 1"
		#first_name = request.form['firstname']
		#last_name = request.form['lastname']
		#gender = request.form['gender']
		#check = request.form['check']
		dov = datetime.datetime.now().strftime ("%Y-%m-%d")
		rest = "1"
		name = request.form['NAME']
		phone = request.form['PHNO']
		email = request.form['EMAIL']
		dob = request.form['DOB']
		datab=map(int,dob.split('-'))
		dobm=datab[1]
		year=datab[0]
		day=datab[2]
		if (dobm == 1):
			bm = "jan"
		elif(dobm == 2):
			bm = "feb"
		elif(dobm == 3):
			bm = "mar"
		elif(dobm == 4):
			bm = "april"
		elif(dobm == 5):
			bm = "may"
		elif(dobm == 6):
			bm = "june"
		elif(dobm == 7):
			bm = "july"
		elif(dobm == 8):
			bm = "aug"
		elif(dobm == 9):
			bm = "sept"
		elif(dobm == 10):
			bm = "oct"
		elif(dobm == 11):
			bm = "nov"
		elif(dobm == 12):
			bm = "dec"
		print(bm)
		ad = request.form['AD']
		datad=map(int,ad.split('-'))
		doam=datad[1]
		year=datad[0]
		day=datad[2]
		if (doam == 1):
			am = "jan"
		elif(doam == 2):
			am = "feb"
		elif(doam == 3):
			am = "mar"
		elif(doam == 4):
			am = "april"
		elif(doam == 5):
			am = "may"
		elif(doam == 6):
			am = "june"
		elif(doam == 7):
			am = "july"
		elif(doam == 8):
			am = "aug"
		elif(doam == 9):
			am = "sept"
		elif(doam == 10):
			am = "oct"
		elif(doam == 11):
			am = "nov"
		elif(doam == 12):
			am = "dec"
		#dov = request.form['DOV']
		us = request.form['US']
		p = request.form['P']
		meal = request.form['MEAL']
		q1 = request.form['Q1']
		q2 = request.form['Q2']
		q3 = request.form['Q3']
		q4 = request.form['Q4']
		q5 = request.form['Q5']
		q6 = request.form['Q6']
		q7 = request.form['Q7']
		q8 = request.form['Q8']
		q9 = request.form['Q9']
		q10 = request.form['Q10']
		rating = request.form['RATING']
		fr = request.form['FR']
		cm = request.form['CM']
		print(dov)
		db.Task.insert({"rest":rest, "name": name, "phone": phone, "email":email, "dob":dob,"dobm":bm,"doam":am,
			"ad": ad, "dov": dov, "us":us, "p":p, "meal": meal, "q1": q1, "q2":q2, "q3":q3, "q4": q4, "q5":q5, "q6":q6,
			"q7": q7, "q8":q8, "q9":q9, "q10":q10, "rating":rating,"fr":fr, "cm":cm })
		return render_template("ty_en.html")
		#return render_template("service.html", fn = first_name, ln = last_name, gender = gender)
	except Exception:
		return dumps({'error' : str(e)})

@app.route('/rest1_ar', methods = ['POST'])
def rest1_form_ar():
	try:
		#data = json.loads(request.data)
		#country = data['country']
		#project = "project 1"
		#first_name = request.form['firstname']
		#last_name = request.form['lastname']
		#gender = request.form['gender']
		#check = request.form['check']
		dov = datetime.datetime.now().strftime ("%Y-%m-%d")
		rest = "1"
		name = request.form['NAME']
		phone = request.form['PHNO']
		email = request.form['EMAIL']
		dob = request.form['DOB']
		datab=map(int,dob.split('-'))
		dobm=datab[1]
		year=datab[0]
		day=datab[2]
		if (dobm == 1):
			bm = "jan"
		elif(dobm == 2):
			bm = "feb"
		elif(dobm == 3):
			bm = "mar"
		elif(dobm == 4):
			bm = "april"
		elif(dobm == 5):
			bm = "may"
		elif(dobm == 6):
			bm = "june"
		elif(dobm == 7):
			bm = "july"
		elif(dobm == 8):
			bm = "aug"
		elif(dobm == 9):
			bm = "sept"
		elif(dobm == 10):
			bm = "oct"
		elif(dobm == 11):
			bm = "nov"
		elif(dobm == 12):
			bm = "dec"
		print(bm)
		ad = request.form['AD']
		datad=map(int,ad.split('-'))
		doam=datad[1]
		year=datad[0]
		day=datad[2]
		if (doam == 1):
			am = "jan"
		elif(doam == 2):
			am = "feb"
		elif(doam == 3):
			am = "mar"
		elif(doam == 4):
			am = "april"
		elif(doam == 5):
			am = "may"
		elif(doam == 6):
			am = "june"
		elif(doam == 7):
			am = "july"
		elif(doam == 8):
			am = "aug"
		elif(doam == 9):
			am = "sept"
		elif(doam == 10):
			am = "oct"
		elif(doam == 11):
			am = "nov"
		elif(doam == 12):
			am = "dec"
		
		#dov = request.form['DOV']
		us = request.form['US']
		p = request.form['P']
		meal = request.form['MEAL']
		q1 = request.form['Q1']
		q2 = request.form['Q2']
		q3 = request.form['Q3']
		q4 = request.form['Q4']
		q5 = request.form['Q5']
		q6 = request.form['Q6']
		q7 = request.form['Q7']
		q8 = request.form['Q8']
		q9 = request.form['Q9']
		q10 = request.form['Q10']
		rating = request.form['RATING']
		fr = request.form['FR']
		cm = request.form['CM']
		print(dov)
		db.Task.insert({"rest":rest, "name": name, "phone": phone, "email":email, "dob":dob,"dobm":bm,"doam":am, 
			"ad": ad, "dov": dov, "us":us, "p":p, "meal": meal, "q1": q1, "q2":q2, "q3":q3, "q4": q4, "q5":q5, "q6":q6,
			"q7": q7, "q8":q8, "q9":q9, "q10":q10, "rating":rating,"fr":fr, "cm":cm })
		return render_template("ty_en.html")
		#return render_template("service.html", fn = first_name, ln = last_name, gender = gender)

	except Exception:
		return dumps({'error' : str(e)})



#Restaurant 2 form page-English and arabic

@app.route('/rest2_en')
def rest2_en():
   return render_template("rest2_form_en.html")

@app.route('/rest2_ar')
def rest2_ar():
   return render_template("rest2_form_ar.html")

@app.route('/rest2_en', methods = ['POST'])
def rest2_form_en():
	try:
		#data = json.loads(request.data)
		#country = data['country']
		#project = "project 1"
		#first_name = request.form['firstname']
		#last_name = request.form['lastname']
		#gender = request.form['gender']
		#check = request.form['check']
		rest = "2"
		name = request.form['NAME']
		phone = request.form['PHNO']
		email = request.form['EMAIL']
		dob = request.form['DOB']
		datab=map(int,dob.split('-'))
		dobm=datab[1]
		year=datab[0]
		day=datab[2]
		if (dobm == 1):
			bm = "jan"
		elif(dobm == 2):
			bm = "feb"
		elif(dobm == 3):
			bm = "mar"
		elif(dobm == 4):
			bm = "april"
		elif(dobm == 5):
			bm = "may"
		elif(dobm == 6):
			bm = "june"
		elif(dobm == 7):
			bm = "july"
		elif(dobm == 8):
			bm = "aug"
		elif(dobm == 9):
			bm = "sept"
		elif(dobm == 10):
			bm = "oct"
		elif(dobm == 11):
			bm = "nov"
		elif(dobm == 12):
			bm = "dec"
		print(bm)
		ad = request.form['AD']
		datad=map(int,ad.split('-'))
		doam=datad[1]
		year=datad[0]
		day=datad[2]
		if (doam == 1):
			am = "jan"
		elif(doam == 2):
			am = "feb"
		elif(doam == 3):
			am = "mar"
		elif(doam == 4):
			am = "april"
		elif(doam == 5):
			am = "may"
		elif(doam == 6):
			am = "june"
		elif(doam == 7):
			am = "july"
		elif(doam == 8):
			am = "aug"
		elif(doam == 9):
			am = "sept"
		elif(doam == 10):
			am = "oct"
		elif(doam == 11):
			am = "nov"
		elif(doam == 12):
			am = "dec"
		
		dov = datetime.datetime.now().strftime ("%Y-%m-%d")
		#dov = request.form['DOV']
		us = request.form['US']
		p = request.form['P']
		meal = request.form['MEAL']
		q1 = request.form['Q1']
		q2 = request.form['Q2']
		q3 = request.form['Q3']
		q4 = request.form['Q4']
		q5 = request.form['Q5']
		q6 = request.form['Q6']
		q7 = request.form['Q7']
		q8 = request.form['Q8']
		q9 = request.form['Q9']
		q10 = request.form['Q10']
		rating = request.form['RATING']
		fr = request.form['FR']
		cm = request.form['CM']
		print(name)
		db.Task.insert({"rest":rest, "name": name, "phone": phone, "email":email, "dob":dob,"dobm":bm,"doam":am, 
			"ad": ad, "dov": dov, "us":us, "p":p, "meal": meal, "q1": q1, "q2":q2, "q3":q3, "q4": q4, "q5":q5, "q6":q6,
			"q7": q7, "q8":q8, "q9":q9, "q10":q10, "rating":rating,"fr":fr, "cm":cm })
		return render_template("ty_en.html")
		#return render_template("service.html", fn = first_name, ln = last_name, gender = gender)

	except Exception:
		return dumps({'error' : str(e)})


@app.route('/rest2_ar', methods = ['POST'])
def rest2_form_ar():
	try:
		#data = json.loads(request.data)
		#country = data['country']
		#project = "project 1"
		#first_name = request.form['firstname']
		#last_name = request.form['lastname']
		#gender = request.form['gender']
		#check = request.form['check']
		rest = "2"
		name = request.form['NAME']
		phone = request.form['PHNO']
		email = request.form['EMAIL']
		dob = request.form['DOB']
		datab=map(int,dob.split('-'))
		dobm=datab[1]
		year=datab[0]
		day=datab[2]
		if (dobm == 1):
			bm = "jan"
		elif(dobm == 2):
			bm = "feb"
		elif(dobm == 3):
			bm = "mar"
		elif(dobm == 4):
			bm = "april"
		elif(dobm == 5):
			bm = "may"
		elif(dobm == 6):
			bm = "june"
		elif(dobm == 7):
			bm = "july"
		elif(dobm == 8):
			bm = "aug"
		elif(dobm == 9):
			bm = "sept"
		elif(dobm == 10):
			bm = "oct"
		elif(dobm == 11):
			bm = "nov"
		elif(dobm == 12):
			bm = "dec"
		print(bm)
		ad = request.form['AD']
		datad=map(int,ad.split('-'))
		doam=datad[1]
		year=datad[0]
		day=datad[2]
		if (doam == 1):
			am = "jan"
		elif(doam == 2):
			am = "feb"
		elif(doam == 3):
			am = "mar"
		elif(doam == 4):
			am = "april"
		elif(doam == 5):
			am = "may"
		elif(doam == 6):
			am = "june"
		elif(doam == 7):
			am = "july"
		elif(doam == 8):
			am = "aug"
		elif(doam == 9):
			am = "sept"
		elif(doam == 10):
			am = "oct"
		elif(doam == 11):
			am = "nov"
		elif(doam == 12):
			am = "dec"
		
		dov = datetime.datetime.now().strftime ("%Y-%m-%d")
		#dov = request.form['DOV']
		us = request.form['US']
		p = request.form['P']
		meal = request.form['MEAL']
		q1 = request.form['Q1']
		q2 = request.form['Q2']
		q3 = request.form['Q3']
		q4 = request.form['Q4']
		q5 = request.form['Q5']
		q6 = request.form['Q6']
		q7 = request.form['Q7']
		q8 = request.form['Q8']
		q9 = request.form['Q9']
		q10 = request.form['Q10']
		rating = request.form['RATING']
		fr = request.form['FR']
		cm = request.form['CM']
		print(name)
		db.Task.insert({"rest":rest, "name": name, "phone": phone, "email":email, "dob":dob, "dobm":bm,"doam":am,
			"ad": ad, "dov": dov, "us":us, "p":p, "meal": meal, "q1": q1, "q2":q2, "q3":q3, "q4": q4, "q5":q5, "q6":q6,
			"q7": q7, "q8":q8, "q9":q9, "q10":q10, "rating":rating,"fr":fr, "cm":cm })
		return render_template("ty_ar.html")
		#return render_template("service.html", fn = first_name, ln = last_name, gender = gender)

	except Exception:
		return dumps({'error' : str(e)})

#Restaurant 3 form page-English and arabic

@app.route('/rest3_en')
def rest3_en():
   return render_template("rest3_form_en.html")
@app.route('/rest3_ar')
def rest3_ar():
   return render_template("rest3_form_ar.html")

@app.route('/rest3_en', methods = ['POST'])
def rest3_form_en():
	try:
		#data = json.loads(request.data)
		#country = data['country']
		#project = "project 1"
		#first_name = request.form['firstname']
		#last_name = request.form['lastname']
		#gender = request.form['gender']
		#check = request.form['check']
		rest = "3"
		name = request.form['NAME']
		phone = request.form['PHNO']
		email = request.form['EMAIL']
		dob = request.form['DOB']
		datab=map(int,dob.split('-'))
		dobm=datab[1]
		year=datab[0]
		day=datab[2]
		if (dobm == 1):
			bm = "jan"
		elif(dobm == 2):
			bm = "feb"
		elif(dobm == 3):
			bm = "mar"
		elif(dobm == 4):
			bm = "april"
		elif(dobm == 5):
			bm = "may"
		elif(dobm == 6):
			bm = "june"
		elif(dobm == 7):
			bm = "july"
		elif(dobm == 8):
			bm = "aug"
		elif(dobm == 9):
			bm = "sept"
		elif(dobm == 10):
			bm = "oct"
		elif(dobm == 11):
			bm = "nov"
		elif(dobm == 12):
			bm = "dec"
		print(bm)
		ad = request.form['AD']
		datad=map(int,ad.split('-'))
		doam=datad[1]
		year=datad[0]
		day=datad[2]
		if (doam == 1):
			am = "jan"
		elif(doam == 2):
			am = "feb"
		elif(doam == 3):
			am = "mar"
		elif(doam == 4):
			am = "april"
		elif(doam == 5):
			am = "may"
		elif(doam == 6):
			am = "june"
		elif(doam == 7):
			am = "july"
		elif(doam == 8):
			am = "aug"
		elif(doam == 9):
			am = "sept"
		elif(doam == 10):
			am = "oct"
		elif(doam == 11):
			am = "nov"
		elif(doam == 12):
			am = "dec"
		
		dov = datetime.datetime.now().strftime ("%Y-%m-%d")
		#dov = request.form['DOV']
		us = request.form['US']
		p = request.form['P']
		meal = request.form['MEAL']
		q1 = request.form['Q1']
		q2 = request.form['Q2']
		q3 = request.form['Q3']
		q4 = request.form['Q4']
		q5 = request.form['Q5']
		q6 = request.form['Q6']
		q7 = request.form['Q7']
		q8 = request.form['Q8']
		q9 = request.form['Q9']
		q10 = request.form['Q10']
		rating = request.form['RATING']
		fr = request.form['FR']
		cm = request.form['CM']
		print(name)
		db.Task.insert({"rest":rest, "name": name, "phone": phone, "email":email, "dob":dob,"dobm":bm,"doam":am,
			"ad": ad, "dov": dov, "us":us, "p":p, "meal": meal, "q1": q1, "q2":q2, "q3":q3, "q4": q4, "q5":q5, "q6":q6,
			"q7": q7, "q8":q8, "q9":q9, "q10":q10, "rating":rating,"fr":fr, "cm":cm })
		return render_template("ty_en.html")
		#return render_template("service.html", fn = first_name, ln = last_name, gender = gender)

	except Exception:
		return dumps({'error' : str(e)})


@app.route('/rest3_ar', methods = ['POST'])
def rest3_form_ar():
	try:
		#data = json.loads(request.data)
		#country = data['country']
		#project = "project 1"
		#first_name = request.form['firstname']
		#last_name = request.form['lastname']
		#gender = request.form['gender']
		#check = request.form['check']
		rest = "3"
		name = request.form['NAME']
		phone = request.form['PHNO']
		email = request.form['EMAIL']
		dob = request.form['DOB']
		datab=map(int,dob.split('-'))
		dobm=datab[1]
		year=datab[0]
		day=datab[2]
		if (dobm == 1):
			bm = "jan"
		elif(dobm == 2):
			bm = "feb"
		elif(dobm == 3):
			bm = "mar"
		elif(dobm == 4):
			bm = "april"
		elif(dobm == 5):
			bm = "may"
		elif(dobm == 6):
			bm = "june"
		elif(dobm == 7):
			bm = "july"
		elif(dobm == 8):
			bm = "aug"
		elif(dobm == 9):
			bm = "sept"
		elif(dobm == 10):
			bm = "oct"
		elif(dobm == 11):
			bm = "nov"
		elif(dobm == 12):
			bm = "dec"
		print(bm)
		ad = request.form['AD']
		datad=map(int,ad.split('-'))
		doam=datad[1]
		year=datad[0]
		day=datad[2]
		if (doam == 1):
			am = "jan"
		elif(doam == 2):
			am = "feb"
		elif(doam == 3):
			am = "mar"
		elif(doam == 4):
			am = "april"
		elif(doam == 5):
			am = "may"
		elif(doam == 6):
			am = "june"
		elif(doam == 7):
			am = "july"
		elif(doam == 8):
			am = "aug"
		elif(doam == 9):
			am = "sept"
		elif(doam == 10):
			am = "oct"
		elif(doam == 11):
			am = "nov"
		elif(doam == 12):
			am = "dec"
		
		dov = datetime.datetime.now().strftime ("%Y-%m-%d")
		#dov = request.form['DOV']
		us = request.form['US']
		p = request.form['P']
		meal = request.form['MEAL']
		q1 = request.form['Q1']
		q2 = request.form['Q2']
		q3 = request.form['Q3']
		q4 = request.form['Q4']
		q5 = request.form['Q5']
		q6 = request.form['Q6']
		q7 = request.form['Q7']
		q8 = request.form['Q8']
		q9 = request.form['Q9']
		q10 = request.form['Q10']
		rating = request.form['RATING']
		fr = request.form['FR']
		cm = request.form['CM']
		print(name)
		db.Task.insert({"rest":rest, "name": name, "phone": phone, "email":email, "dob":dob,"dobm":bm,"doam":am, 
			"ad": ad, "dov": dov, "us":us, "p":p, "meal": meal, "q1": q1, "q2":q2, "q3":q3, "q4": q4, "q5":q5, "q6":q6,
			"q7": q7, "q8":q8, "q9":q9, "q10":q10, "rating":rating,"fr":fr, "cm":cm })
		return render_template("ty_ar.html")
		#return render_template("service.html", fn = first_name, ln = last_name, gender = gender)

	except Exception:
		return dumps({'error' : str(e)})


#Restaurant 4 form page-English and arabic

@app.route('/rest4_en')
def rest4_en():
   return render_template("rest4_form_en.html")
@app.route('/rest4_ar')
def rest4_ar():
   return render_template("rest4_form_ar.html")

@app.route('/rest4_en', methods = ['POST'])
def rest4_form_en():
	try:
		#data = json.loads(request.data)
		#country = data['country']
		#project = "project 1"
		#first_name = request.form['firstname']
		#last_name = request.form['lastname']
		#gender = request.form['gender']
		#check = request.form['check']
		rest = "4"
		name = request.form['NAME']
		phone = request.form['PHNO']
		email = request.form['EMAIL']
		dob = request.form['DOB']
		datab=map(int,dob.split('-'))
		dobm=datab[1]
		year=datab[0]
		day=datab[2]
		if (dobm == 1):
			bm = "jan"
		elif(dobm == 2):
			bm = "feb"
		elif(dobm == 3):
			bm = "mar"
		elif(dobm == 4):
			bm = "april"
		elif(dobm == 5):
			bm = "may"
		elif(dobm == 6):
			bm = "june"
		elif(dobm == 7):
			bm = "july"
		elif(dobm == 8):
			bm = "aug"
		elif(dobm == 9):
			bm = "sept"
		elif(dobm == 10):
			bm = "oct"
		elif(dobm == 11):
			bm = "nov"
		elif(dobm == 12):
			bm = "dec"
		print(bm)
		ad = request.form['AD']
		datad=map(int,ad.split('-'))
		doam=datad[1]
		year=datad[0]
		day=datad[2]
		if (doam == 1):
			am = "jan"
		elif(doam == 2):
			am = "feb"
		elif(doam == 3):
			am = "mar"
		elif(doam == 4):
			am = "april"
		elif(doam == 5):
			am = "may"
		elif(doam == 6):
			am = "june"
		elif(doam == 7):
			am = "july"
		elif(doam == 8):
			am = "aug"
		elif(doam == 9):
			am = "sept"
		elif(doam == 10):
			am = "oct"
		elif(doam == 11):
			am = "nov"
		elif(doam == 12):
			am = "dec"
		
		dov = datetime.datetime.now().strftime ("%Y-%m-%d")
		#dov = request.form['DOV']
		us = request.form['US']
		p = request.form['P']
		meal = request.form['MEAL']
		q1 = request.form['Q1']
		q2 = request.form['Q2']
		q3 = request.form['Q3']
		q4 = request.form['Q4']
		q5 = request.form['Q5']
		q6 = request.form['Q6']
		q7 = request.form['Q7']
		q8 = request.form['Q8']
		q9 = request.form['Q9']
		q10 = request.form['Q10']
		rating = request.form['RATING']
		fr = request.form['FR']
		cm = request.form['CM']
		print(name)
		db.Task.insert({"rest":rest, "name": name, "phone": phone, "email":email, "dob":dob, "dobm":bm,"doam":am,
			"ad": ad, "dov": dov, "us":us, "p":p, "meal": meal, "q1": q1, "q2":q2, "q3":q3, "q4": q4, "q5":q5, "q6":q6,
			"q7": q7, "q8":q8, "q9":q9, "q10":q10, "rating":rating,"fr":fr, "cm":cm })
		return render_template("ty_en.html")
		#return render_template("service.html", fn = first_name, ln = last_name, gender = gender)

	except Exception:
		return dumps({'error' : str(e)})


@app.route('/rest4_ar', methods = ['POST'])
def rest4_form_ar():
	try:
		#data = json.loads(request.data)
		#country = data['country']
		#project = "project 1"
		#first_name = request.form['firstname']
		#last_name = request.form['lastname']
		#gender = request.form['gender']
		#check = request.form['check']
		rest = "4"
		name = request.form['NAME']
		phone = request.form['PHNO']
		email = request.form['EMAIL']
		dob = request.form['DOB']
		datab=map(int,dob.split('-'))
		dobm=datab[1]
		year=datab[0]
		day=datab[2]
		if (dobm == 1):
			bm = "jan"
		elif(dobm == 2):
			bm = "feb"
		elif(dobm == 3):
			bm = "mar"
		elif(dobm == 4):
			bm = "april"
		elif(dobm == 5):
			bm = "may"
		elif(dobm == 6):
			bm = "june"
		elif(dobm == 7):
			bm = "july"
		elif(dobm == 8):
			bm = "aug"
		elif(dobm == 9):
			bm = "sept"
		elif(dobm == 10):
			bm = "oct"
		elif(dobm == 11):
			bm = "nov"
		elif(dobm == 12):
			bm = "dec"
		print(bm)
		ad = request.form['AD']
		datad=map(int,ad.split('-'))
		doam=datad[1]
		year=datad[0]
		day=datad[2]
		if (doam == 1):
			am = "jan"
		elif(doam == 2):
			am = "feb"
		elif(doam == 3):
			am = "mar"
		elif(doam == 4):
			am = "april"
		elif(doam == 5):
			am = "may"
		elif(doam == 6):
			am = "june"
		elif(doam == 7):
			am = "july"
		elif(doam == 8):
			am = "aug"
		elif(doam == 9):
			am = "sept"
		elif(doam == 10):
			am = "oct"
		elif(doam == 11):
			am = "nov"
		elif(doam == 12):
			am = "dec"
		
		dov = datetime.datetime.now().strftime ("%Y-%m-%d")
		#dov = request.form['DOV']
		us = request.form['US']
		p = request.form['P']
		meal = request.form['MEAL']
		q1 = request.form['Q1']
		q2 = request.form['Q2']
		q3 = request.form['Q3']
		q4 = request.form['Q4']
		q5 = request.form['Q5']
		q6 = request.form['Q6']
		q7 = request.form['Q7']
		q8 = request.form['Q8']
		q9 = request.form['Q9']
		q10 = request.form['Q10']
		rating = request.form['RATING']
		fr = request.form['FR']
		cm = request.form['CM']
		print(name)
		db.Task.insert({"rest":rest, "name": name, "phone": phone, "email":email, "dob":dob, "dobm":bm,"doam":am,
			"ad": ad, "dov": dov, "us":us, "p":p, "meal": meal, "q1": q1, "q2":q2, "q3":q3, "q4": q4, "q5":q5, "q6":q6,
			"q7": q7, "q8":q8, "q9":q9, "q10":q10, "rating":rating,"fr":fr, "cm":cm })
		return render_template("ty_ar.html")
		#return render_template("service.html", fn = first_name, ln = last_name, gender = gender)

	except Exception:
		return dumps({'error' : str(e)})


#Restaurant 5 form page-English and arabic

@app.route('/rest5_en')
def rest5_en():
   return render_template("rest5_form_en.html")
@app.route('/rest5_ar')
def rest5_ar():
   return render_template("rest5_form_ar.html")

@app.route('/rest5_en', methods = ['POST'])
def rest5_form_en():
	try:
		#data = json.loads(request.data)
		#country = data['country']
		#project = "project 1"
		#first_name = request.form['firstname']
		#last_name = request.form['lastname']
		#gender = request.form['gender']
		#check = request.form['check']
		rest = "5"
		name = request.form['NAME']
		phone = request.form['PHNO']
		email = request.form['EMAIL']
		dob = request.form['DOB']
		datab=map(int,dob.split('-'))
		dobm=datab[1]
		year=datab[0]
		day=datab[2]
		if (dobm == 1):
			bm = "jan"
		elif(dobm == 2):
			bm = "feb"
		elif(dobm == 3):
			bm = "mar"
		elif(dobm == 4):
			bm = "april"
		elif(dobm == 5):
			bm = "may"
		elif(dobm == 6):
			bm = "june"
		elif(dobm == 7):
			bm = "july"
		elif(dobm == 8):
			bm = "aug"
		elif(dobm == 9):
			bm = "sept"
		elif(dobm == 10):
			bm = "oct"
		elif(dobm == 11):
			bm = "nov"
		elif(dobm == 12):
			bm = "dec"
		print(bm)
		ad = request.form['AD']
		datad=map(int,ad.split('-'))
		doam=datad[1]
		year=datad[0]
		day=datad[2]
		if (doam == 1):
			am = "jan"
		elif(doam == 2):
			am = "feb"
		elif(doam == 3):
			am = "mar"
		elif(doam == 4):
			am = "april"
		elif(doam == 5):
			am = "may"
		elif(doam == 6):
			am = "june"
		elif(doam == 7):
			am = "july"
		elif(doam == 8):
			am = "aug"
		elif(doam == 9):
			am = "sept"
		elif(doam == 10):
			am = "oct"
		elif(doam == 11):
			am = "nov"
		elif(doam == 12):
			am = "dec"
		
		dov = datetime.datetime.now().strftime ("%Y-%m-%d")
		#dov = request.form['DOV']
		us = request.form['US']
		p = request.form['P']
		meal = request.form['MEAL']
		q1 = request.form['Q1']
		q2 = request.form['Q2']
		q3 = request.form['Q3']
		q4 = request.form['Q4']
		q5 = request.form['Q5']
		q6 = request.form['Q6']
		q7 = request.form['Q7']
		q8 = request.form['Q8']
		q9 = request.form['Q9']
		q10 = request.form['Q10']
		rating = request.form['RATING']
		fr = request.form['FR']
		cm = request.form['CM']
		print(name)
		db.Task.insert({"rest":rest, "name": name, "phone": phone, "email":email, "dob":dob, "dobm":bm,"doam":am,
			"ad": ad, "dov": dov, "us":us, "p":p, "meal": meal, "q1": q1, "q2":q2, "q3":q3, "q4": q4, "q5":q5, "q6":q6,
			"q7": q7, "q8":q8, "q9":q9, "q10":q10, "rating":rating,"fr":fr, "cm":cm })
		return render_template("ty_en.html")
		#return render_template("service.html", fn = first_name, ln = last_name, gender = gender)

	except Exception:
		return dumps({'error' : str(e)})


@app.route('/rest5_ar', methods = ['POST'])
def rest5_form_ar():
	try:
		#data = json.loads(request.data)
		#country = data['country']
		#project = "project 1"
		#first_name = request.form['firstname']
		#last_name = request.form['lastname']
		#gender = request.form['gender']
		#check = request.form['check']
		rest = "5"
		name = request.form['NAME']
		phone = request.form['PHNO']
		email = request.form['EMAIL']
		dob = request.form['DOB']
		datab=map(int,dob.split('-'))
		dobm=datab[1]
		year=datab[0]
		day=datab[2]
		if (dobm == 1):
			bm = "jan"
		elif(dobm == 2):
			bm = "feb"
		elif(dobm == 3):
			bm = "mar"
		elif(dobm == 4):
			bm = "april"
		elif(dobm == 5):
			bm = "may"
		elif(dobm == 6):
			bm = "june"
		elif(dobm == 7):
			bm = "july"
		elif(dobm == 8):
			bm = "aug"
		elif(dobm == 9):
			bm = "sept"
		elif(dobm == 10):
			bm = "oct"
		elif(dobm == 11):
			bm = "nov"
		elif(dobm == 12):
			bm = "dec"
		print(bm)
		ad = request.form['AD']
		datad=map(int,ad.split('-'))
		doam=datad[1]
		year=datad[0]
		day=datad[2]
		if (doam == 1):
			am = "jan"
		elif(doam == 2):
			am = "feb"
		elif(doam == 3):
			am = "mar"
		elif(doam == 4):
			am = "april"
		elif(doam == 5):
			am = "may"
		elif(doam == 6):
			am = "june"
		elif(doam == 7):
			am = "july"
		elif(doam == 8):
			am = "aug"
		elif(doam == 9):
			am = "sept"
		elif(doam == 10):
			am = "oct"
		elif(doam == 11):
			am = "nov"
		elif(doam == 12):
			am = "dec"
		
		dov = datetime.datetime.now().strftime ("%Y-%m-%d")
		#dov = request.form['DOV']
		us = request.form['US']
		p = request.form['P']
		meal = request.form['MEAL']
		q1 = request.form['Q1']
		q2 = request.form['Q2']
		q3 = request.form['Q3']
		q4 = request.form['Q4']
		q5 = request.form['Q5']
		q6 = request.form['Q6']
		q7 = request.form['Q7']
		q8 = request.form['Q8']
		q9 = request.form['Q9']
		q10 = request.form['Q10']
		rating = request.form['RATING']
		fr = request.form['FR']
		cm = request.form['CM']
		print(name)
		db.Task.insert({"rest":rest, "name": name, "phone": phone, "email":email, "dob":dob, "dobm":bm,"doam":am,
			"ad": ad, "dov": dov, "us":us, "p":p, "meal": meal, "q1": q1, "q2":q2, "q3":q3, "q4": q4, "q5":q5, "q6":q6,
			"q7": q7, "q8":q8, "q9":q9, "q10":q10, "rating":rating,"fr":fr, "cm":cm })
		return render_template("ty_ar.html")
		#return render_template("service.html", fn = first_name, ln = last_name, gender = gender)

	except Exception:
		return dumps({'error' : str(e)})

#Restaurant 6 form page-English and arabic

@app.route('/rest6_en')
def rest6_en():
   return render_template("rest6_form_en.html")
@app.route('/rest1_ar')
def rest6_ar():
   return render_template("rest6_form_ar.html")

@app.route('/rest6_en', methods = ['POST'])
def rest6_form_en():
	try:
		#data = json.loads(request.data)
		#country = data['country']
		#project = "project 1"
		#first_name = request.form['firstname']
		#last_name = request.form['lastname']
		#gender = request.form['gender']
		#check = request.form['check']
		rest = "6"
		name = request.form['NAME']
		phone = request.form['PHNO']
		email = request.form['EMAIL']
		dob = request.form['DOB']
		datab=map(int,dob.split('-'))
		dobm=datab[1]
		year=datab[0]
		day=datab[2]
		if (dobm == 1):
			bm = "jan"
		elif(dobm == 2):
			bm = "feb"
		elif(dobm == 3):
			bm = "mar"
		elif(dobm == 4):
			bm = "april"
		elif(dobm == 5):
			bm = "may"
		elif(dobm == 6):
			bm = "june"
		elif(dobm == 7):
			bm = "july"
		elif(dobm == 8):
			bm = "aug"
		elif(dobm == 9):
			bm = "sept"
		elif(dobm == 10):
			bm = "oct"
		elif(dobm == 11):
			bm = "nov"
		elif(dobm == 12):
			bm = "dec"
		print(bm)
		ad = request.form['AD']
		datad=map(int,ad.split('-'))
		doam=datad[1]
		year=datad[0]
		day=datad[2]
		if (doam == 1):
			am = "jan"
		elif(doam == 2):
			am = "feb"
		elif(doam == 3):
			am = "mar"
		elif(doam == 4):
			am = "april"
		elif(doam == 5):
			am = "may"
		elif(doam == 6):
			am = "june"
		elif(doam == 7):
			am = "july"
		elif(doam == 8):
			am = "aug"
		elif(doam == 9):
			am = "sept"
		elif(doam == 10):
			am = "oct"
		elif(doam == 11):
			am = "nov"
		elif(doam == 12):
			am = "dec"
		
		dov = datetime.datetime.now().strftime ("%Y-%m-%d")
		#dov = request.form['DOV']
		us = request.form['US']
		p = request.form['P']
		meal = request.form['MEAL']
		q1 = request.form['Q1']
		q2 = request.form['Q2']
		q3 = request.form['Q3']
		q4 = request.form['Q4']
		q5 = request.form['Q5']
		q6 = request.form['Q6']
		q7 = request.form['Q7']
		q8 = request.form['Q8']
		q9 = request.form['Q9']
		q10 = request.form['Q10']
		rating = request.form['RATING']
		fr = request.form['FR']
		cm = request.form['CM']
		print(name)
		db.Task.insert({"rest":rest, "name": name, "phone": phone, "email":email, "dob":dob, "dobm":bm,"doam":am,
			"ad": ad, "dov": dov, "us":us, "p":p, "meal": meal, "q1": q1, "q2":q2, "q3":q3, "q4": q4, "q5":q5, "q6":q6,
			"q7": q7, "q8":q8, "q9":q9, "q10":q10, "rating":rating,"fr":fr, "cm":cm })
		return render_template("ty_en.html")
		#return render_template("service.html", fn = first_name, ln = last_name, gender = gender)

	except Exception:
		return dumps({'error' : str(e)})


@app.route('/rest6_ar', methods = ['POST'])
def rest6_form_ar():
	try:
		#data = json.loads(request.data)
		#country = data['country']
		#project = "project 1"
		#first_name = request.form['firstname']
		#last_name = request.form['lastname']
		#gender = request.form['gender']
		#check = request.form['check']
		rest = "6"
		name = request.form['NAME']
		phone = request.form['PHNO']
		email = request.form['EMAIL']
		dob = request.form['DOB']
		datab=map(int,dob.split('-'))
		dobm=datab[1]
		year=datab[0]
		day=datab[2]
		if (dobm == 1):
			bm = "jan"
		elif(dobm == 2):
			bm = "feb"
		elif(dobm == 3):
			bm = "mar"
		elif(dobm == 4):
			bm = "april"
		elif(dobm == 5):
			bm = "may"
		elif(dobm == 6):
			bm = "june"
		elif(dobm == 7):
			bm = "july"
		elif(dobm == 8):
			bm = "aug"
		elif(dobm == 9):
			bm = "sept"
		elif(dobm == 10):
			bm = "oct"
		elif(dobm == 11):
			bm = "nov"
		elif(dobm == 12):
			bm = "dec"
		print(bm)
		ad = request.form['AD']
		datad=map(int,ad.split('-'))
		doam=datad[1]
		year=datad[0]
		day=datad[2]
		if (doam == 1):
			am = "jan"
		elif(doam == 2):
			am = "feb"
		elif(doam == 3):
			am = "mar"
		elif(doam == 4):
			am = "april"
		elif(doam == 5):
			am = "may"
		elif(doam == 6):
			am = "june"
		elif(doam == 7):
			am = "july"
		elif(doam == 8):
			am = "aug"
		elif(doam == 9):
			am = "sept"
		elif(doam == 10):
			am = "oct"
		elif(doam == 11):
			am = "nov"
		elif(doam == 12):
			am = "dec"
		
		dov = datetime.datetime.now().strftime ("%Y-%m-%d")
		#dov = request.form['DOV']
		us = request.form['US']
		p = request.form['P']
		meal = request.form['MEAL']
		q1 = request.form['Q1']
		q2 = request.form['Q2']
		q3 = request.form['Q3']
		q4 = request.form['Q4']
		q5 = request.form['Q5']
		q6 = request.form['Q6']
		q7 = request.form['Q7']
		q8 = request.form['Q8']
		q9 = request.form['Q9']
		q10 = request.form['Q10']
		rating = request.form['RATING']
		fr = request.form['FR']
		cm = request.form['CM']
		print(name)
		db.Task.insert({"rest":rest, "name": name, "phone": phone, "email":email, "dob":dob, "dobm":bm,"doam":am,
			"ad": ad, "dov": dov, "us":us, "p":p, "meal": meal, "q1": q1, "q2":q2, "q3":q3, "q4": q4, "q5":q5, "q6":q6,
			"q7": q7, "q8":q8, "q9":q9, "q10":q10, "rating":rating,"fr":fr, "cm":cm })
		return render_template("ty_ar.html")
		#return render_template("service.html", fn = first_name, ln = last_name, gender = gender)

	except Exception:
		return dumps({'error' : str(e)})


#SPA english form page-English and arabic

@app.route('/spa_en')
def spa_en():
   return render_template("spa_form_en.html")

@app.route('/spa_ar')
def spa_ar():
   return render_template("spa_form_ar.html")

#list of restaurants
@app.route('/restaurant')
def restaurant():
   return render_template("restaurant.html")

@app.route('/spa_en', methods = ['POST'])
def spa_form_en():
	try:
		#data = json.loads(request.data)
		#country = data['country']
		#project = "project 1"
		#first_name = request.form['firstname']
		#last_name = request.form['lastname']
		#gender = request.form['gender']
		#check = request.form['check']
		spa = "spa"
		name = request.form['NAME']
		phone = request.form['PHNO']
		email = request.form['EMAIL']
		dob = request.form['DOB']
		datab=map(int,dob.split('-'))
		dobm=datab[1]
		year=datab[0]
		day=datab[2]
		if (dobm == 1):
			bm = "jan"
		elif(dobm == 2):
			bm = "feb"
		elif(dobm == 3):
			bm = "mar"
		elif(dobm == 4):
			bm = "april"
		elif(dobm == 5):
			bm = "may"
		elif(dobm == 6):
			bm = "june"
		elif(dobm == 7):
			bm = "july"
		elif(dobm == 8):
			bm = "aug"
		elif(dobm == 9):
			bm = "sept"
		elif(dobm == 10):
			bm = "oct"
		elif(dobm == 11):
			bm = "nov"
		elif(dobm == 12):
			bm = "dec"
		print(bm)
		ad = request.form['AD']
		datad=map(int,ad.split('-'))
		doam=datad[1]
		year=datad[0]
		day=datad[2]
		if (doam == 1):
			am = "jan"
		elif(doam == 2):
			am = "feb"
		elif(doam == 3):
			am = "mar"
		elif(doam == 4):
			am = "april"
		elif(doam == 5):
			am = "may"
		elif(doam == 6):
			am = "june"
		elif(doam == 7):
			am = "july"
		elif(doam == 8):
			am = "aug"
		elif(doam == 9):
			am = "sept"
		elif(doam == 10):
			am = "oct"
		elif(doam == 11):
			am = "nov"
		elif(doam == 12):
			am = "dec"
		
		dov = datetime.datetime.now().strftime ("%Y-%m-%d")
		#dov = request.form['DOV']
		us = request.form['US']
		p = request.form['P']
		q1 = request.form['Q1']
		q2 = request.form['Q2']
		q3 = request.form['Q3']
		q4 = request.form['Q4']
		q5 = request.form['Q5']
		q6 = request.form['Q6']
		q7 = request.form['Q7']
		q8 = request.form['Q8']
		q9 = request.form['Q9']
		q10 = request.form['Q10']
		q11 = request.form['Q11']
		name_spa = request.form['SPA']
		cm = request.form['CM']
		print(name)
		db.Task.insert({"spa":spa, "sname": name, "sphone": phone, "email":email, "dob":dob, "dobm":bm,"doam":am,
			"ad": ad, "dov": dov, "us":us, "sp":p, "sq1": q1, "sq2":q2, "sq3":q3, "sq4": q4, "sq5":q5, "sq6":q6,
			"sq7": q7, "sq8":q8, "sq9":q9, "sq10":q10, "sq11":q11, "name_spa":name_spa, "scm":cm })
		return render_template("ty_en.html")
		#return render_template("service.html", fn = first_name, ln = last_name, gender = gender)

	except Exception:
		return dumps({'error' : str(e)})


@app.route('/spa_ar', methods = ['POST'])
def spa_form_ar():
	try:
		#data = json.loads(request.data)
		#country = data['country']
		#project = "project 1"
		#first_name = request.form['firstname']
		#last_name = request.form['lastname']
		#gender = request.form['gender']
		#check = request.form['check']
		spa = "spa"
		name = request.form['NAME']
		phone = request.form['PHNO']
		email = request.form['EMAIL']
		dob = request.form['DOB']
		datab=map(int,dob.split('-'))
		dobm=datab[1]
		year=datab[0]
		day=datab[2]
		if (dobm == 1):
			bm = "jan"
		elif(dobm == 2):
			bm = "feb"
		elif(dobm == 3):
			bm = "mar"
		elif(dobm == 4):
			bm = "april"
		elif(dobm == 5):
			bm = "may"
		elif(dobm == 6):
			bm = "june"
		elif(dobm == 7):
			bm = "july"
		elif(dobm == 8):
			bm = "aug"
		elif(dobm == 9):
			bm = "sept"
		elif(dobm == 10):
			bm = "oct"
		elif(dobm == 11):
			bm = "nov"
		elif(dobm == 12):
			bm = "dec"
		print(bm)
		ad = request.form['AD']
		datad=map(int,ad.split('-'))
		doam=datad[1]
		year=datad[0]
		day=datad[2]
		if (doam == 1):
			am = "jan"
		elif(doam == 2):
			am = "feb"
		elif(doam == 3):
			am = "mar"
		elif(doam == 4):
			am = "april"
		elif(doam == 5):
			am = "may"
		elif(doam == 6):
			am = "june"
		elif(doam == 7):
			am = "july"
		elif(doam == 8):
			am = "aug"
		elif(doam == 9):
			am = "sept"
		elif(doam == 10):
			am = "oct"
		elif(doam == 11):
			am = "nov"
		elif(doam == 12):
			am = "dec"
		
		dov = datetime.datetime.now().strftime ("%Y-%m-%d")
		#dov = request.form['DOV']
		us = request.form['US']
		p = request.form['P']
		q1 = request.form['Q1']
		q2 = request.form['Q2']
		q3 = request.form['Q3']
		q4 = request.form['Q4']
		q5 = request.form['Q5']
		q6 = request.form['Q6']
		q7 = request.form['Q7']
		q8 = request.form['Q8']
		q9 = request.form['Q9']
		q10 = request.form['Q10']
		q11 = request.form['Q11']
		name_spa = request.form['SPA']
		cm = request.form['CM']
		print(name)
		db.Task.insert({"spa":spa, "sname": name, "sphone": phone, "email":email, "dob":dob, "dobm":bm,"doam":am,
			"ad": ad, "dov": dov, "us":us, "sp":p, "sq1": q1, "sq2":q2, "sq3":q3, "sq4": q4, "sq5":q5, "sq6":q6,
			"sq7": q7, "sq8":q8, "sq9":q9, "sq10":q10, "sq11":q11, "name_spa":name_spa, "scm":cm })
		return render_template("ty_en.html")
		#return render_template("service.html", fn = first_name, ln = last_name, gender = gender)

	except Exception:
		return dumps({'error' : str(e)})



@app.route('/next', methods = ['POST'])
def move_forward():
    #Moving forward code
    return render_template("service.html")

@app.route('/users', methods = ['GET'])
def get_users():
    #Moving forward code
    return render_template("users.html")

#Date of Biths of restaurnat
@app.route('/user_rest_dob', methods = ['GET','POST'])
def get_users_rest_dob():
    #Moving forward code
    #get month from form.
    #check the month and start and end time from 1st of the month to 1st of the next month.
    #sdate = "2019-05-08"\
    #enddate

    if(request.form['month'] == 'jan'):
    	month = 'jan'
    	print(month)
    elif(request.form['month'] == 'feb'):
    	month = 'feb'
    elif(request.form['month'] == 'mar'):
    	month = 'mar'
    elif(request.form['month'] == 'apr'):
    	month = 'april'
    	print(month)
    elif(request.form['month'] == 'may'):
    	month = 'may'
    	print(month)
    elif(request.form['month'] == 'june'):
    	month = 'june'
    elif(request.form['month'] == 'july'):
    	month = 'july'
    elif(request.form['month'] == 'aug'):
    	month = 'aug'
    	print(month)
    elif(request.form['month'] == 'sept'):
    	month = 'sept'
    elif(request.form['month'] == 'oct'):
    	month = 'oct'
    elif(request.form['month'] == 'nov'):
    	month = 'nov'
    elif(request.form['month'] == 'dec'):
    	month = 'dec'

    user = db.Task.find({'dobm':month})
    return render_template("birthdayrest.html", user= user)

#Date of Biths of restaurnat
@app.route('/user_spa_dob', methods = ['GET','POST'])
def get_users_spa_dob():
    #Moving forward code
    #get month from form.
    #check the month and start and end time from 1st of the month to 1st of the next month.
    #sdate = "2019-05-08"\
    #enddate
    
    if(request.form['month'] == 'jan'):
    	month = 'jan'
    elif(request.form['month'] == 'feb'):
    	month = 'feb'
    elif(request.form['month'] == 'mar'):
    	month = 'mar'
    elif(request.form['month'] == 'apr'):
    	month = 'april'
    elif(request.form['month'] == 'may'):
    	month = 'may'
    elif(request.form['month'] == 'june'):
    	month = 'june'
    elif(request.form['month'] == 'july'):
    	month = 'july'
    elif(request.form['month'] == 'aug'):
    	month = 'aug'
    elif(request.form['month'] == 'sept'):
    	month = 'sept'
    elif(request.form['month'] == 'oct'):
    	month = 'oct'
    elif(request.form['month'] == 'nov'):
    	month = 'nov'
    elif(request.form['month'] == 'dec'):
    	month = 'dec'

    user = db.Task.find({'spa':'spa','dobm':month})
    return render_template("birthdayspa.html", user= user)


#Date of anniversary
@app.route('/user_rest_doa', methods = ['GET','POST'])
def get_users_rest_doa():
    #Moving forward code
    #get month from form.
    #check the month and start and end time from 1st of the month to 1st of the next month.
    #sdate = "2019-05-08"\
    #enddate
    if(request.form['month'] == 'jan'):
    	month = 'jan'
    elif(request.form['month'] == 'feb'):
    	month = 'feb'
    elif(request.form['month'] == 'mar'):
    	month = 'mar'
    elif(request.form['month'] == 'apr'):
    	month = 'april'
    elif(request.form['month'] == 'may'):
    	month = 'may'
    elif(request.form['month'] == 'june'):
    	month = 'june'
    elif(request.form['month'] == 'july'):
    	month = 'july'
    elif(request.form['month'] == 'aug'):
    	month = 'aug'
    elif(request.form['month'] == 'sept'):
    	month = 'sept'
    elif(request.form['month'] == 'oct'):
    	month = 'oct'
    elif(request.form['month'] == 'nov'):
    	month = 'nov'
    elif(request.form['month'] == 'dec'):
    	month = 'dec'

    user = db.Task.find({'doam':month})
    return render_template("anniversaryrest.html",user=user)

#Date of anniversary
@app.route('/user_spa_doa', methods = ['GET','POST'])
def get_users_spa_doa():
    #Moving forward code
    #get month from form.
    #check the month and start and end time from 1st of the month to 1st of the next month.
    #sdate = "2019-05-08"\
    #enddate
    if(request.form['month'] == 'jan'):
    	month = 'jan'
    elif(request.form['month'] == 'feb'):
    	month = 'feb'
    elif(request.form['month'] == 'mar'):
    	month = 'mar'
    elif(request.form['month'] == 'apr'):
    	month = 'april'
    elif(request.form['month'] == 'may'):
    	month = 'may'
    elif(request.form['month'] == 'june'):
    	month = 'june'
    elif(request.form['month'] == 'july'):
    	month = 'july'
    elif(request.form['month'] == 'aug'):
    	month = 'aug'
    elif(request.form['month'] == 'sept'):
    	month = 'sept'
    elif(request.form['month'] == 'oct'):
    	month = 'oct'
    elif(request.form['month'] == 'nov'):
    	month = 'nov'
    elif(request.form['month'] == 'dec'):
    	month = 'dec'

    user = db.Task.find({'spa':'spa','doam':month})
    return render_template("anniversaryspa.html",user=user)



#get all the users json
@app.route('/get_all', methods = ['GET'])
def get_all():
	try:
		tasks = db.Task.find()
		#return render_template("users_rest.html", tasks = tasks)
		return dumps(tasks)
	except Exception:
		return dumps({'error' : str(e)})


#Most visited restaurant
@app.route('/get_visited_rest_today', methods = ['GET','POST'])
def get_visited_rest_today():
	if 'user' in session:
		dov = datetime.datetime.now().strftime ("%Y-%m-%d")
		rest1 = db.Task.find({'rest':'1', 'dov':dov}).count()
		rest2 = db.Task.find({'rest':'2','dov':dov}).count()
		rest3 = db.Task.find({'rest':'3','dov':dov}).count()
		rest4 = db.Task.find({'rest':'4','dov':dov}).count()
		rest5 = db.Task.find({'rest':'5','dov':dov}).count()
		rest6 = db.Task.find({'rest':'6','dov':dov}).count()


		return render_template("mvr.html", rest1 = rest1, rest2 = rest2, rest3 = rest3, rest4 = rest4, rest5 = rest5, rest6 = rest6)
		#return dumps(tasks)
	return redirect(url_for('sess'))

#Most visited restaurant
@app.route('/get_visited_rest_on', methods = ['GET','POST'])
def get_visited_rest_on():
	if 'user' in session:
		startdate = request.form['startdate']
		rest1 = db.Task.find({'rest':'1','dov':startdate}).count()
		rest2 = db.Task.find({'rest':'2','dov':startdate}).count()
		rest3 = db.Task.find({'rest':'3','dov':startdate}).count()
		rest4 = db.Task.find({'rest':'4','dov':startdate}).count()
		rest5 = db.Task.find({'rest':'5','dov':startdate}).count()
		rest6 = db.Task.find({'rest':'6','dov':startdate}).count()


		return render_template("mvr.html", rest1 = rest1, rest2 = rest2, rest3 = rest3, rest4 = rest4, rest5 = rest5, rest6 = rest6)
		#return dumps(tasks)
	return redirect(url_for('sess'))
#Most visited restaurant
@app.route('/get_visited_rest_from', methods = ['GET','POST'])
def get_visited_rest_from():
	if 'user' in session:
		startdate = request.form['startdate']
		enddate = request.form['enddate']
		rest1 = db.Task.find({'rest':'1','dov': {"$gte": startdate,"$lt":enddate}}).count()
		rest2 = db.Task.find({'rest':'2','dov': {"$gte": startdate,"$lt":enddate}}).count()
		rest3 = db.Task.find({'rest':'3','dov': {"$gte": startdate,"$lt":enddate}}).count()
		rest4 = db.Task.find({'rest':'4','dov': {"$gte": startdate,"$lt":enddate}}).count()
		rest5 = db.Task.find({'rest':'5','dov': {"$gte": startdate,"$lt":enddate}}).count()
		rest6 = db.Task.find({'rest':'6','dov': {"$gte": startdate,"$lt":enddate}}).count()


		return render_template("mvr.html", rest1 = rest1, rest2 = rest2, rest3 = rest3, rest4 = rest4, rest5 = rest5, rest6 = rest6)
		#return dumps(tasks)
	return redirect(url_for('sess'))

#Most visited restaurant
@app.route('/get_meal', methods = ['GET','POST'])
def get_meal():
	if 'user' in session:

		startdate = request.form['startdate']
		enddate = request.form['enddate']
		print(request.form['rest'])
		if(request.form['rest'] == '1'):
			name = "Les Delicates"
			meal = db.Task.find({'rest':'1', 'meal':'Meal', 'dov': {"$gte": startdate,"$lt":enddate}}).count()
			breakfast = db.Task.find({'rest':'1', 'meal':'Breakfast', 'dov': {"$gte": startdate,"$lt":enddate}}).count()
			lunch = db.Task.find({'rest':'1', 'meal':'Lunch', 'dov': {"$gte": startdate,"$lt":enddate}}).count()
			dinner = db.Task.find({'rest':'1', 'meal':'Dinner', 'dov': {"$gte": startdate,"$lt":enddate}}).count()

		elif(request.form['rest'] == '2'):
			name = "Cucina"
			meal = db.Task.find({'rest':'1', 'meal':'Meal', 'dov': {"$gte": startdate,"$lt":enddate}}).count()
			breakfast = db.Task.find({'rest':'1', 'meal':'Breakfast', 'dov': {"$gte": startdate,"$lt":enddate}}).count()
			lunch = db.Task.find({'rest':'1', 'meal':'Lunch', 'dov': {"$gte": startdate,"$lt":enddate}}).count()
			dinner = db.Task.find({'rest':'1', 'meal':'Dinner', 'dov': {"$gte": startdate,"$lt":enddate}}).count()

		elif(request.form['rest'] == '3'):
			name = "Chococafe"
			meal = db.Task.find({'rest':'1', 'meal':'Meal', 'dov': {"$gte": startdate,"$lt":enddate}}).count()
			breakfast = db.Task.find({'rest':'1', 'meal':'Breakfast', 'dov': {"$gte": startdate,"$lt":enddate}}).count()
			lunch = db.Task.find({'rest':'1', 'meal':'Lunch', 'dov': {"$gte": startdate,"$lt":enddate}}).count()
			dinner = db.Task.find({'rest':'1', 'meal':'Dinner', 'dov': {"$gte": startdate,"$lt":enddate}}).count()

		elif(request.form['rest'] == '4'):
			name = "Luna"
			meal = db.Task.find({'rest':'1', 'meal':'Meal','dov': {"$gte": startdate,"$lt":enddate}}).count()
			breakfast = db.Task.find({'rest':'1', 'meal':'Breakfast','dov': {"$gte": startdate,"$lt":enddate}}).count()
			lunch = db.Task.find({'rest':'1', 'meal':'Lunch','dov': {"$gte": startdate,"$lt":enddate}}).count()
			dinner = db.Task.find({'rest':'1', 'meal':'Dinner','dov': {"$gte": startdate,"$lt":enddate}}).count()

		elif(request.form['rest'] == '5'):
			meal = db.Task.find({'rest':'1', 'meal':'Meal','dov': {"$gte": startdate,"$lt":enddate}}).count()
			breakfast = db.Task.find({'rest':'1', 'meal':'Breakfast','dov': {"$gte": startdate,"$lt":enddate}}).count()
			lunch = db.Task.find({'rest':'1', 'meal':'Lunch','dov': {"$gte": startdate,"$lt":enddate}}).count()
			dinner = db.Task.find({'rest':'1', 'meal':'Dinner','dov': {"$gte": startdate,"$lt":enddate}}).count()

		elif(request.form['rest'] == '6'):
			meal = db.Task.find({'rest':'1', 'meal':'Meal'}).count()
			breakfast = db.Task.find({'rest':'1', 'meal':'Breakfast'}).count()
			lunch = db.Task.find({'rest':'1', 'meal':'Lunch'}).count()
			dinner = db.Task.find({'rest':'1', 'meal':'Dinner'}).count()


		return render_template("mmr.html", name = name , meal = meal, breakfast = breakfast, lunch = lunch, dinner = dinner)
		#return dumps(tasks)
	return redirect(url_for('sess'))


#Promotional event users options
@app.route('/get_rpe', methods = ['GET','POST'])
def get_rpe_yes():
	if 'user' in session:
		if(request.form['pe'] == 'yes'):
			pe = db.Task.find({'p':'Yes'})
			name = "Restaurant-Yes"

		elif(request.form['pe'] == 'no'):
			pe = db.Task.find({'p':'No'})
			name = "Restaurant-No"

		return render_template("perest.html", pe = pe, name = name)
		#return dumps(tasks)
	return redirect(url_for('sess'))

#Promotional event users options
@app.route('/get_spe', methods = ['GET','POST'])
def get_spe():
	if 'user' in session:
		if(request.form['pe'] == 'yes'):
			pe = db.Task.find({'sp':'Yes'})
			name = "Spa-Yes"

		elif(request.form['pe'] == 'no'):
			pe = db.Task.find({'sp':'No'})
			name = "Spa-No"

		return render_template("pespa.html", pe = pe, name = name)
		#return dumps(tasks)
	return redirect(url_for('sess'))


#get all the users for rest
@app.route('/get_all_rest', methods = ['GET'])
def get_all_rest():
	if 'user' in session:
		rest1 = db.Task.find({'rest':'1'})
		rest2 = db.Task.find({'rest':'2'})
		rest3 = db.Task.find({'rest':'3'})
		rest4 = db.Task.find({'rest':'4'})
		rest5 = db.Task.find({'rest':'5'})
		rest6 = db.Task.find({'rest':'6'})
		return render_template("users_rest.html", rest1 = rest1, rest2 = rest2, rest3 = rest3, rest4 = rest4, rest5 = rest5, rest6 = rest6)
		#return dumps(tasks)
	return redirect(url_for('sess'))

#get all the users for rest for today
@app.route('/get_all_rest_today', methods = ['GET','POST'])
def get_all_today():
	if 'user' in session:

		dov = datetime.datetime.now().strftime ("%Y-%m-%d")

		rest1 = db.Task.find({'rest':'1','dov':dov})
		rest2 = db.Task.find({'rest':'2','dov':dov})
		rest3 = db.Task.find({'rest':'3','dov':dov})
		rest4 = db.Task.find({'rest':'4','dov':dov})
		rest5 = db.Task.find({'rest':'5','dov':dov})
		rest6 = db.Task.find({'rest':'6','dov':dov})
		return render_template("users_rest.html", rest1 = rest1, rest2 = rest2, rest3 = rest3, rest4 = rest4, rest5 = rest5, rest6 = rest6)
		#return dumps(tasks)
	return redirect(url_for('sess'))

#get all the users for rest dateon
@app.route('/get_all_dateon', methods = ['GET','POST'])
def get_all_dateon():
	if 'user' in session:
		startdate = request.form['startdate']
		rest1 = db.Task.find({'rest':'1','dov':startdate})
		rest2 = db.Task.find({'rest':'2','dov':startdate})
		rest3 = db.Task.find({'rest':'3','dov':startdate})
		rest4 = db.Task.find({'rest':'4','dov':startdate})
		rest5 = db.Task.find({'rest':'5','dov':startdate})
		rest6 = db.Task.find({'rest':'6','dov':startdate})
		return render_template("users_rest.html", rest1 = rest1, rest2 = rest2, rest3 = rest3, rest4 = rest4, rest5 = rest5, rest6 = rest6)
		#return dumps(tasks)
	return redirect(url_for('sess'))

#get all the users for rest fromto
@app.route('/get_all_fromto', methods = ['GET','POST'])
def get_all_fromto():
	if 'user' in session:
		startdate = request.form['startdate']
		enddate = request.form['enddate']
		rest1 = db.Task.find({'rest':'1','dov': {"$gte": startdate,"$lt":enddate}})
		rest2 = db.Task.find({'rest':'2','dov': {"$gte": startdate,"$lt":enddate}})
		rest3 = db.Task.find({'rest':'3','dov': {"$gte": startdate,"$lt":enddate}})
		rest4 = db.Task.find({'rest':'4','dov': {"$gte": startdate,"$lt":enddate}})
		rest5 = db.Task.find({'rest':'5','dov': {"$gte": startdate,"$lt":enddate}})
		rest6 = db.Task.find({'rest':'6','dov': {"$gte": startdate,"$lt":enddate}})
		return render_template("users_rest.html", rest1 = rest1, rest2 = rest2, rest3 = rest3, rest4 = rest4, rest5 = rest5, rest6 = rest6)
		#return dumps(tasks)
	return redirect(url_for('sess'))

#get all the users for spa
@app.route('/get_all_spa', methods = ['GET'])
def get_all_spa():
	if 'user' in session:
		tasks = db.Task.find({'spa':'spa'})
		return render_template("users_spa.html", tasks = tasks)
		#return dumps(tasks)
	return redirect(url_for('sess'))

#get all the users for spa today
@app.route('/get_spa_today', methods = ['GET','POST'])
def get_spa_today():
	if 'user' in session:
		dov = datetime.datetime.now().strftime ("%Y-%m-%d")
		tasks = db.Task.find({'spa':'spa','dov':dov})
		return render_template("users_spa.html", tasks = tasks)
		#return dumps(tasks)
	return redirect(url_for('sess'))

#get all the users for spa on particular date
@app.route('/get_spa_dateon', methods = ['GET','POST'])
def get_spa_dateon():
	if 'user' in session:
		startdate = request.form['startdate']
		tasks = db.Task.find({'spa':'spa','dov':startdate})
		return render_template("users_spa.html", tasks = tasks)
		#return dumps(tasks)
	return redirect(url_for('sess'))

#get all the users for spa range
@app.route('/get_spa_fromto', methods = ['GET','POST'])
def get_spa_fromto():
	if 'user' in session:
		startdate = request.form['startdate']
		enddate = request.form['enddate']
		tasks = db.Task.find({'spa':'spa','dov': {"$gte": startdate,"$lt":enddate}})
		return render_template("users_spa.html", tasks = tasks)
		#return dumps(tasks)
	return redirect(url_for('sess'))


#Data of each visitors
@app.route('/get_all_<name>', methods = ['GET'])
def get_single(name):
	if 'user' in session:
		single = db.Task.find({'name':name})
		return render_template("single_table.html", single = single)
		#return render_template("display.html", tasks = tasks)
	return redirect(url_for('sess'))
	
#Data of each visitors for restaurant
@app.route('/get_rest_<name>', methods = ['GET'])
def get_rest_details(name):
	if 'user' in session:
		single = db.Task.find({'name':name})
		return render_template("details_restaurant.html", single = single)
		#return render_template("display.html", tasks = tasks)
	return redirect(url_for('sess'))

#Data of each visitors for spa
@app.route('/get_spa_<name>', methods = ['GET'])
def get_spa_details(name):
	if 'user' in session:
		single = db.Task.find({'sname':name})
		return render_template("details_spa.html", single = single)
		#return render_template("display.html", tasks = tasks)
	return redirect(url_for('sess'))

#Data of visitors per restaurant
@app.route('/get_visitor_<rest>', methods = ['GET'])
def get_rest_visit(rest):
	if 'user' in session:
		single = db.Task.find({'rest':rest})
		return render_template("users_rest_list.html", single = single)
		#return render_template("display.html", tasks = tasks)
	return redirect(url_for('sess'))

#Data of visitors per restaurant
@app.route('/get_visitor_spa', methods = ['GET'])
def get_spa_visit():
	if 'user' in session:
		single = db.Task.find({'spa':'spa'})
		return render_template("users_spa_list.html", single = single)
		#return render_template("display.html", tasks = tasks)
	return redirect(url_for('sess'))

#report of visitors per restaurant
@app.route('/get_report_<no>', methods = ['POST'])
def get_report(no):
	if 'user' in session:
		if no == "1":
			logo = "les.png"
		elif no == "2":
			logo = "cucina.png"
		elif no == "3":
			logo = "chococafe.png"
		elif no == "4":
			logo = "luna.png"
		
		startdate = request.form['startdate']
		enddate = request.form['enddate']
		#single = db.Task.find({'rest':no})

		single = db.Task.find({'rest':no, 'dov': {"$gte": startdate,"$lt":enddate}})
		total = db.Task.find({'rest':no,'dov': {"$gte": startdate,"$lt":enddate}}).count()
		q1_1 = db.Task.find({'rest':no,'dov': {"$gte": startdate,"$lt":enddate},'q1':'1'}).count()
		q1_2 = db.Task.find({'rest':no,'dov': {"$gte": startdate,"$lt":enddate},'q1':'2'}).count()
		q1_3 = db.Task.find({'rest':no,'dov': {"$gte": startdate,"$lt":enddate},'q1':'3'}).count()
		q1_4 = db.Task.find({'rest':no,'dov': {"$gte": startdate,"$lt":enddate},'q1':'4'}).count()
		q1_5 = db.Task.find({'rest':no,'dov': {"$gte": startdate,"$lt":enddate},'q1':'5'}).count()
		q2_1 = db.Task.find({'rest':no,'dov': {"$gte": startdate,"$lt":enddate},'q2':'1'}).count()
		q2_2 = db.Task.find({'rest':no,'dov': {"$gte": startdate,"$lt":enddate},'q2':'2'}).count()
		q2_3 = db.Task.find({'rest':no,'dov': {"$gte": startdate,"$lt":enddate},'q2':'3'}).count()
		q2_4 = db.Task.find({'rest':no,'dov': {"$gte": startdate,"$lt":enddate},'q2':'4'}).count()
		q2_5 = db.Task.find({'rest':no,'dov': {"$gte": startdate,"$lt":enddate},'q2':'5'}).count()
		q3_1 = db.Task.find({'rest':no,'dov': {"$gte": startdate,"$lt":enddate},'q3':'1'}).count()
		q3_2 = db.Task.find({'rest':no,'dov': {"$gte": startdate,"$lt":enddate},'q3':'2'}).count()
		q3_3 = db.Task.find({'rest':no,'dov': {"$gte": startdate,"$lt":enddate},'q3':'3'}).count()
		q3_4 = db.Task.find({'rest':no,'dov': {"$gte": startdate,"$lt":enddate},'q3':'4'}).count()
		q3_5 = db.Task.find({'rest':no,'dov': {"$gte": startdate,"$lt":enddate},'q3':'5'}).count()
		q4_1 = db.Task.find({'rest':no,'dov': {"$gte": startdate,"$lt":enddate},'q4':'1'}).count()
		q4_2 = db.Task.find({'rest':no,'dov': {"$gte": startdate,"$lt":enddate},'q4':'2'}).count()
		q4_3 = db.Task.find({'rest':no,'dov': {"$gte": startdate,"$lt":enddate},'q4':'3'}).count()
		q4_4 = db.Task.find({'rest':no,'dov': {"$gte": startdate,"$lt":enddate},'q4':'4'}).count()
		q4_5 = db.Task.find({'rest':no,'dov': {"$gte": startdate,"$lt":enddate},'q4':'5'}).count()
		q5_1 = db.Task.find({'rest':no,'dov': {"$gte": startdate,"$lt":enddate},'q5':'1'}).count()
		q5_2 = db.Task.find({'rest':no,'dov': {"$gte": startdate,"$lt":enddate},'q5':'2'}).count()
		q5_3 = db.Task.find({'rest':no,'dov': {"$gte": startdate,"$lt":enddate},'q5':'3'}).count()
		q5_4 = db.Task.find({'rest':no,'dov': {"$gte": startdate,"$lt":enddate},'q5':'4'}).count()
		q5_5 = db.Task.find({'rest':no,'dov': {"$gte": startdate,"$lt":enddate},'q5':'5'}).count()
		q6_1 = db.Task.find({'rest':no,'dov': {"$gte": startdate,"$lt":enddate},'q6':'1'}).count()
		q6_2 = db.Task.find({'rest':no,'dov': {"$gte": startdate,"$lt":enddate},'q6':'2'}).count()
		q6_3 = db.Task.find({'rest':no,'dov': {"$gte": startdate,"$lt":enddate},'q6':'3'}).count()
		q6_4 = db.Task.find({'rest':no,'dov': {"$gte": startdate,"$lt":enddate},'q6':'4'}).count()
		q6_5 = db.Task.find({'rest':no,'dov': {"$gte": startdate,"$lt":enddate},'q6':'5'}).count()
		q7_1 = db.Task.find({'rest':no,'dov': {"$gte": startdate,"$lt":enddate},'q7':'1'}).count()
		q7_2 = db.Task.find({'rest':no,'dov': {"$gte": startdate,"$lt":enddate},'q7':'2'}).count()
		q7_3 = db.Task.find({'rest':no,'dov': {"$gte": startdate,"$lt":enddate},'q7':'3'}).count()
		q7_4 = db.Task.find({'rest':no,'dov': {"$gte": startdate,"$lt":enddate},'q7':'4'}).count()
		q7_5 = db.Task.find({'rest':no,'dov': {"$gte": startdate,"$lt":enddate},'q7':'5'}).count()
		q8_1 = db.Task.find({'rest':no,'dov': {"$gte": startdate,"$lt":enddate},'q8':'1'}).count()
		q8_2 = db.Task.find({'rest':no,'dov': {"$gte": startdate,"$lt":enddate},'q8':'2'}).count()
		q8_3 = db.Task.find({'rest':no,'dov': {"$gte": startdate,"$lt":enddate},'q8':'3'}).count()
		q8_4 = db.Task.find({'rest':no,'dov': {"$gte": startdate,"$lt":enddate},'q8':'4'}).count()
		q8_5 = db.Task.find({'rest':no,'dov': {"$gte": startdate,"$lt":enddate},'q8':'5'}).count()
		q9_1 = db.Task.find({'rest':no,'dov': {"$gte": startdate,"$lt":enddate},'q9':'1'}).count()
		q9_2 = db.Task.find({'rest':no,'dov': {"$gte": startdate,"$lt":enddate},'q9':'2'}).count()
		q9_3 = db.Task.find({'rest':no,'dov': {"$gte": startdate,"$lt":enddate},'q9':'3'}).count()
		q9_4 = db.Task.find({'rest':no,'dov': {"$gte": startdate,"$lt":enddate},'q9':'4'}).count()
		q9_5 = db.Task.find({'rest':no,'dov': {"$gte": startdate,"$lt":enddate},'q9':'5'}).count()
		
		print (startdate)
		#return dumps(single)
		return render_template("report_rest.html",logo = logo,no = no , total = total, single = single, q1_1=q1_1, q1_2=q1_2, q1_3=q1_3,q1_4=q1_4,q1_5=q1_5,q2_1=q2_1, q2_2=q2_2, q2_3=q2_3,q2_4=q2_4,q2_5=q2_5,
		q3_1=q3_1, q3_2=q3_2, q3_3=q3_3,q3_4=q3_4,q3_5=q3_5,q4_1=q4_1, q4_2=q4_2, q4_3=q4_3,q4_4=q4_4,q4_5=q4_5,q5_1=q5_1, q5_2=q5_2, q5_3=q5_3,q5_4=q5_4,q5_5=q5_5,
		q6_1=q6_1, q6_2=q6_2, q6_3=q6_3,q6_4=q6_4,q6_5=q6_5,q7_1=q7_1, q7_2=q7_2, q7_3=q7_3,q7_4=q7_4,q7_5=q7_5,q8_1=q8_1, q8_2=q8_2, q8_3=q8_3,q8_4=q8_4,q8_5=q8_5,
		q9_1=q9_1, q9_2=q9_2, q9_3=q9_3,q9_4=q9_4,q9_5=q9_5, startdate = startdate, enddate=enddate)
		#return render_template("display.html", tasks = tasks)
	return redirect(url_for('sess'))

#report of visitors per restaurant
@app.route('/get_report_rest', methods = ['GET','POST'])
def get_report_rest():
	if 'user' in session:
		if(request.form['rest'] == '1'):
			no = '1'
		elif(request.form['rest'] == '2'):
			no = '2'
		elif(request.form['rest'] == '3'):
			no = '3'
		elif(request.form['rest'] == '4'):
			no = '4'
		elif(request.form['rest'] == '5'):
			no = '5'
		elif(request.form['rest'] == '6'):
			no = '6'
		
		startdate = request.form['startdate']
		enddate = request.form['enddate']
		#single = db.Task.find({'rest':no})

		single = db.Task.find({'rest':no, 'dov': {"$gte": startdate,"$lt":enddate}})
		total = db.Task.find({'rest':no,'dov': {"$gte": startdate,"$lt":enddate}}).count()
		q1_1 = db.Task.find({'rest':no,'dov': {"$gte": startdate,"$lt":enddate},'q1':'1'}).count()
		q1_2 = db.Task.find({'rest':no,'dov': {"$gte": startdate,"$lt":enddate},'q1':'2'}).count()
		q1_3 = db.Task.find({'rest':no,'dov': {"$gte": startdate,"$lt":enddate},'q1':'3'}).count()
		q1_4 = db.Task.find({'rest':no,'dov': {"$gte": startdate,"$lt":enddate},'q1':'4'}).count()
		q1_5 = db.Task.find({'rest':no,'dov': {"$gte": startdate,"$lt":enddate},'q1':'5'}).count()
		q2_1 = db.Task.find({'rest':no,'dov': {"$gte": startdate,"$lt":enddate},'q2':'1'}).count()
		q2_2 = db.Task.find({'rest':no,'dov': {"$gte": startdate,"$lt":enddate},'q2':'2'}).count()
		q2_3 = db.Task.find({'rest':no,'dov': {"$gte": startdate,"$lt":enddate},'q2':'3'}).count()
		q2_4 = db.Task.find({'rest':no,'dov': {"$gte": startdate,"$lt":enddate},'q2':'4'}).count()
		q2_5 = db.Task.find({'rest':no,'dov': {"$gte": startdate,"$lt":enddate},'q2':'5'}).count()
		q3_1 = db.Task.find({'rest':no,'dov': {"$gte": startdate,"$lt":enddate},'q3':'1'}).count()
		q3_2 = db.Task.find({'rest':no,'dov': {"$gte": startdate,"$lt":enddate},'q3':'2'}).count()
		q3_3 = db.Task.find({'rest':no,'dov': {"$gte": startdate,"$lt":enddate},'q3':'3'}).count()
		q3_4 = db.Task.find({'rest':no,'dov': {"$gte": startdate,"$lt":enddate},'q3':'4'}).count()
		q3_5 = db.Task.find({'rest':no,'dov': {"$gte": startdate,"$lt":enddate},'q3':'5'}).count()
		q4_1 = db.Task.find({'rest':no,'dov': {"$gte": startdate,"$lt":enddate},'q4':'1'}).count()
		q4_2 = db.Task.find({'rest':no,'dov': {"$gte": startdate,"$lt":enddate},'q4':'2'}).count()
		q4_3 = db.Task.find({'rest':no,'dov': {"$gte": startdate,"$lt":enddate},'q4':'3'}).count()
		q4_4 = db.Task.find({'rest':no,'dov': {"$gte": startdate,"$lt":enddate},'q4':'4'}).count()
		q4_5 = db.Task.find({'rest':no,'dov': {"$gte": startdate,"$lt":enddate},'q4':'5'}).count()
		q5_1 = db.Task.find({'rest':no,'dov': {"$gte": startdate,"$lt":enddate},'q5':'1'}).count()
		q5_2 = db.Task.find({'rest':no,'dov': {"$gte": startdate,"$lt":enddate},'q5':'2'}).count()
		q5_3 = db.Task.find({'rest':no,'dov': {"$gte": startdate,"$lt":enddate},'q5':'3'}).count()
		q5_4 = db.Task.find({'rest':no,'dov': {"$gte": startdate,"$lt":enddate},'q5':'4'}).count()
		q5_5 = db.Task.find({'rest':no,'dov': {"$gte": startdate,"$lt":enddate},'q5':'5'}).count()
		q6_1 = db.Task.find({'rest':no,'dov': {"$gte": startdate,"$lt":enddate},'q6':'1'}).count()
		q6_2 = db.Task.find({'rest':no,'dov': {"$gte": startdate,"$lt":enddate},'q6':'2'}).count()
		q6_3 = db.Task.find({'rest':no,'dov': {"$gte": startdate,"$lt":enddate},'q6':'3'}).count()
		q6_4 = db.Task.find({'rest':no,'dov': {"$gte": startdate,"$lt":enddate},'q6':'4'}).count()
		q6_5 = db.Task.find({'rest':no,'dov': {"$gte": startdate,"$lt":enddate},'q6':'5'}).count()
		q7_1 = db.Task.find({'rest':no,'dov': {"$gte": startdate,"$lt":enddate},'q7':'1'}).count()
		q7_2 = db.Task.find({'rest':no,'dov': {"$gte": startdate,"$lt":enddate},'q7':'2'}).count()
		q7_3 = db.Task.find({'rest':no,'dov': {"$gte": startdate,"$lt":enddate},'q7':'3'}).count()
		q7_4 = db.Task.find({'rest':no,'dov': {"$gte": startdate,"$lt":enddate},'q7':'4'}).count()
		q7_5 = db.Task.find({'rest':no,'dov': {"$gte": startdate,"$lt":enddate},'q7':'5'}).count()
		q8_1 = db.Task.find({'rest':no,'dov': {"$gte": startdate,"$lt":enddate},'q8':'1'}).count()
		q8_2 = db.Task.find({'rest':no,'dov': {"$gte": startdate,"$lt":enddate},'q8':'2'}).count()
		q8_3 = db.Task.find({'rest':no,'dov': {"$gte": startdate,"$lt":enddate},'q8':'3'}).count()
		q8_4 = db.Task.find({'rest':no,'dov': {"$gte": startdate,"$lt":enddate},'q8':'4'}).count()
		q8_5 = db.Task.find({'rest':no,'dov': {"$gte": startdate,"$lt":enddate},'q8':'5'}).count()
		q9_1 = db.Task.find({'rest':no,'dov': {"$gte": startdate,"$lt":enddate},'q9':'1'}).count()
		q9_2 = db.Task.find({'rest':no,'dov': {"$gte": startdate,"$lt":enddate},'q9':'2'}).count()
		q9_3 = db.Task.find({'rest':no,'dov': {"$gte": startdate,"$lt":enddate},'q9':'3'}).count()
		q9_4 = db.Task.find({'rest':no,'dov': {"$gte": startdate,"$lt":enddate},'q9':'4'}).count()
		q9_5 = db.Task.find({'rest':no,'dov': {"$gte": startdate,"$lt":enddate},'q9':'5'}).count()
		
		print (startdate)
		#return dumps(single)
		return render_template("report_rest.html",no = no , total = total, single = single, q1_1=q1_1, q1_2=q1_2, q1_3=q1_3,q1_4=q1_4,q1_5=q1_5,q2_1=q2_1, q2_2=q2_2, q2_3=q2_3,q2_4=q2_4,q2_5=q2_5,
		q3_1=q3_1, q3_2=q3_2, q3_3=q3_3,q3_4=q3_4,q3_5=q3_5,q4_1=q4_1, q4_2=q4_2, q4_3=q4_3,q4_4=q4_4,q4_5=q4_5,q5_1=q5_1, q5_2=q5_2, q5_3=q5_3,q5_4=q5_4,q5_5=q5_5,
		q6_1=q6_1, q6_2=q6_2, q6_3=q6_3,q6_4=q6_4,q6_5=q6_5,q7_1=q7_1, q7_2=q7_2, q7_3=q7_3,q7_4=q7_4,q7_5=q7_5,q8_1=q8_1, q8_2=q8_2, q8_3=q8_3,q8_4=q8_4,q8_5=q8_5,
		q9_1=q9_1, q9_2=q9_2, q9_3=q9_3,q9_4=q9_4,q9_5=q9_5, startdate = startdate, enddate=enddate)
		#return render_template("display.html", tasks = tasks)
	return redirect(url_for('sess'))


#report of visitors per spa
@app.route('/get_report_spa', methods = ['GET','POST'])
def get_report_spa():
	if 'user' in session:
		
		startdate = request.form['startdate']
		enddate = request.form['enddate']
		#single = db.Task.find({'rest':no})

		#single = db.Task.find({'spa':'spa','dov': {"$gte": startdate,"$lt":enddate}})
		single = db.Task.find({'spa':'spa','dov': {"$gte": startdate,"$lt":enddate}}).count()
		sq1_1 = db.Task.find({'spa':'spa','dov': {"$gte": startdate,"$lt":enddate},'sq1':'1'}).count()
		sq1_2 = db.Task.find({'spa':'spa','dov': {"$gte": startdate,"$lt":enddate},'sq1':'2'}).count()
		sq1_3 = db.Task.find({'spa':'spa','dov': {"$gte": startdate,"$lt":enddate},'sq1':'3'}).count()
		sq1_4 = db.Task.find({'spa':'spa','dov': {"$gte": startdate,"$lt":enddate},'sq1':'4'}).count()
		sq1_5 = db.Task.find({'spa':'spa','dov': {"$gte": startdate,"$lt":enddate},'sq1':'5'}).count()
		sq2_1 = db.Task.find({'spa':'spa','dov': {"$gte": startdate,"$lt":enddate},'sq2':'1'}).count()
		sq2_2 = db.Task.find({'spa':'spa','dov': {"$gte": startdate,"$lt":enddate},'sq2':'2'}).count()
		sq2_3 = db.Task.find({'spa':'spa','dov': {"$gte": startdate,"$lt":enddate},'sq2':'3'}).count()
		sq2_4 = db.Task.find({'spa':'spa','dov': {"$gte": startdate,"$lt":enddate},'sq2':'4'}).count()
		sq2_5 = db.Task.find({'spa':'spa','dov': {"$gte": startdate,"$lt":enddate},'sq2':'5'}).count()
		sq3_1 = db.Task.find({'spa':'spa','dov': {"$gte": startdate,"$lt":enddate},'sq3':'1'}).count()
		sq3_2 = db.Task.find({'spa':'spa','dov': {"$gte": startdate,"$lt":enddate},'sq3':'2'}).count()
		sq3_3 = db.Task.find({'spa':'spa','dov': {"$gte": startdate,"$lt":enddate},'sq3':'3'}).count()
		sq3_4 = db.Task.find({'spa':'spa','dov': {"$gte": startdate,"$lt":enddate},'sq3':'4'}).count()
		sq3_5 = db.Task.find({'spa':'spa','dov': {"$gte": startdate,"$lt":enddate},'sq3':'5'}).count()
		sq4_1 = db.Task.find({'spa':'spa','dov': {"$gte": startdate,"$lt":enddate},'sq4':'1'}).count()
		sq4_2 = db.Task.find({'spa':'spa','dov': {"$gte": startdate,"$lt":enddate},'sq4':'2'}).count()
		sq4_3 = db.Task.find({'spa':'spa','dov': {"$gte": startdate,"$lt":enddate},'sq4':'3'}).count()
		sq4_4 = db.Task.find({'spa':'spa','dov': {"$gte": startdate,"$lt":enddate},'sq4':'4'}).count()
		sq4_5 = db.Task.find({'spa':'spa','dov': {"$gte": startdate,"$lt":enddate},'sq4':'5'}).count()
		sq5_1 = db.Task.find({'spa':'spa','dov': {"$gte": startdate,"$lt":enddate},'sq5':'1'}).count()
		sq5_2 = db.Task.find({'spa':'spa','dov': {"$gte": startdate,"$lt":enddate},'sq5':'2'}).count()
		sq5_3 = db.Task.find({'spa':'spa','dov': {"$gte": startdate,"$lt":enddate},'sq5':'3'}).count()
		sq5_4 = db.Task.find({'spa':'spa','dov': {"$gte": startdate,"$lt":enddate},'sq5':'4'}).count()
		sq5_5 = db.Task.find({'spa':'spa','dov': {"$gte": startdate,"$lt":enddate},'sq5':'5'}).count()
		sq6_1 = db.Task.find({'spa':'spa','dov': {"$gte": startdate,"$lt":enddate},'sq6':'1'}).count()
		sq6_2 = db.Task.find({'spa':'spa','dov': {"$gte": startdate,"$lt":enddate},'sq6':'2'}).count()
		sq6_3 = db.Task.find({'spa':'spa','dov': {"$gte": startdate,"$lt":enddate},'sq6':'3'}).count()
		sq6_4 = db.Task.find({'spa':'spa','dov': {"$gte": startdate,"$lt":enddate},'sq6':'4'}).count()
		sq6_5 = db.Task.find({'spa':'spa','dov': {"$gte": startdate,"$lt":enddate},'sq6':'5'}).count()
		sq7_1 = db.Task.find({'spa':'spa','dov': {"$gte": startdate,"$lt":enddate},'sq7':'1'}).count()
		sq7_2 = db.Task.find({'spa':'spa','dov': {"$gte": startdate,"$lt":enddate},'sq7':'2'}).count()
		sq7_3 = db.Task.find({'spa':'spa','dov': {"$gte": startdate,"$lt":enddate},'sq7':'3'}).count()
		sq7_4 = db.Task.find({'spa':'spa','dov': {"$gte": startdate,"$lt":enddate},'sq7':'4'}).count()
		sq7_5 = db.Task.find({'spa':'spa','dov': {"$gte": startdate,"$lt":enddate},'sq7':'5'}).count()
		sq8_1 = db.Task.find({'spa':'spa','dov': {"$gte": startdate,"$lt":enddate},'sq8':'1'}).count()
		sq8_2 = db.Task.find({'spa':'spa','dov': {"$gte": startdate,"$lt":enddate},'sq8':'2'}).count()
		sq8_3 = db.Task.find({'spa':'spa','dov': {"$gte": startdate,"$lt":enddate},'sq8':'3'}).count()
		sq8_4 = db.Task.find({'spa':'spa','dov': {"$gte": startdate,"$lt":enddate},'sq8':'4'}).count()
		sq8_5 = db.Task.find({'spa':'spa','dov': {"$gte": startdate,"$lt":enddate},'sq8':'5'}).count()
		sq9_1 = db.Task.find({'spa':'spa','dov': {"$gte": startdate,"$lt":enddate},'sq9':'1'}).count()
		sq9_2 = db.Task.find({'spa':'spa','dov': {"$gte": startdate,"$lt":enddate},'sq9':'2'}).count()
		sq9_3 = db.Task.find({'spa':'spa','dov': {"$gte": startdate,"$lt":enddate},'sq9':'3'}).count()
		sq9_4 = db.Task.find({'spa':'spa','dov': {"$gte": startdate,"$lt":enddate},'sq9':'4'}).count()
		sq9_5 = db.Task.find({'spa':'spa','dov': {"$gte": startdate,"$lt":enddate},'sq9':'5'}).count()
		
		return render_template("report_spa.html",single = single, sq1_1=sq1_1, sq1_2=sq1_2, sq1_3=sq1_3,sq1_4=sq1_4,sq1_5=sq1_5,sq2_1=sq2_1, sq2_2=sq2_2, sq2_3=sq2_3,sq2_4=sq2_4,sq2_5=sq2_5,
		sq3_1=sq3_1, sq3_2=sq3_2, sq3_3=sq3_3,sq3_4=sq3_4,sq3_5=sq3_5,sq4_1=sq4_1, sq4_2=sq4_2, sq4_3=sq4_3,sq4_4=sq4_4,sq4_5=sq4_5,sq5_1=sq5_1, sq5_2=sq5_2, sq5_3=sq5_3,sq5_4=sq5_4,sq5_5=sq5_5,
		sq6_1=sq6_1, sq6_2=sq6_2, sq6_3=sq6_3,sq6_4=sq6_4,sq6_5=sq6_5,sq7_1=sq7_1, sq7_2=sq7_2, sq7_3=sq7_3,sq7_4=sq7_4,sq7_5=sq7_5,sq8_1=sq8_1, sq8_2=sq8_2, sq8_3=sq8_3,sq8_4=sq8_4,sq8_5=sq8_5,
		sq9_1=sq9_1, sq9_2=sq9_2, sq9_3=sq9_3,sq9_4=sq9_4,sq9_5=sq9_5,startdate = startdate, enddate=enddate)
		print (startdate)
		#return dumps(single)

	return redirect(url_for('sess'))

#Data of each rating by each visitor per restaurant
@app.route('/get_rating_<rest>', methods = ['GET'])
def get_rest_rating(rest):
	if 'user' in session:

		if rest == "1":
			logo = "les.png"
		elif rest == "2":
			logo = "cucina.png"
		elif rest == "3":
			logo = "chococafe.png"
		elif rest == "4":
			logo = "luna.png"

		#rest = "1"
		single = db.Task.find({'rest':rest}).count()
		q1_1 = db.Task.find({'rest':rest,'q1':'1'}).count()
		q1_2 = db.Task.find({'rest':rest,'q1':'2'}).count()
		q1_3 = db.Task.find({'rest':rest,'q1':'3'}).count()
		q1_4 = db.Task.find({'rest':rest,'q1':'4'}).count()
		q1_5 = db.Task.find({'rest':rest,'q1':'5'}).count()
		q2_1 = db.Task.find({'rest':rest,'q2':'1'}).count()
		q2_2 = db.Task.find({'rest':rest,'q2':'2'}).count()
		q2_3 = db.Task.find({'rest':rest,'q2':'3'}).count()
		q2_4 = db.Task.find({'rest':rest,'q2':'4'}).count()
		q2_5 = db.Task.find({'rest':rest,'q2':'5'}).count()
		q3_1 = db.Task.find({'rest':rest,'q3':'1'}).count()
		q3_2 = db.Task.find({'rest':rest,'q3':'2'}).count()
		q3_3 = db.Task.find({'rest':rest,'q3':'3'}).count()
		q3_4 = db.Task.find({'rest':rest,'q3':'4'}).count()
		q3_5 = db.Task.find({'rest':rest,'q3':'5'}).count()
		q4_1 = db.Task.find({'rest':rest,'q4':'1'}).count()
		q4_2 = db.Task.find({'rest':rest,'q4':'2'}).count()
		q4_3 = db.Task.find({'rest':rest,'q4':'3'}).count()
		q4_4 = db.Task.find({'rest':rest,'q4':'4'}).count()
		q4_5 = db.Task.find({'rest':rest,'q4':'5'}).count()
		q5_1 = db.Task.find({'rest':rest,'q5':'1'}).count()
		q5_2 = db.Task.find({'rest':rest,'q5':'2'}).count()
		q5_3 = db.Task.find({'rest':rest,'q5':'3'}).count()
		q5_4 = db.Task.find({'rest':rest,'q5':'4'}).count()
		q5_5 = db.Task.find({'rest':rest,'q5':'5'}).count()
		q6_1 = db.Task.find({'rest':rest,'q6':'1'}).count()
		q6_2 = db.Task.find({'rest':rest,'q6':'2'}).count()
		q6_3 = db.Task.find({'rest':rest,'q6':'3'}).count()
		q6_4 = db.Task.find({'rest':rest,'q6':'4'}).count()
		q6_5 = db.Task.find({'rest':rest,'q6':'5'}).count()
		q7_1 = db.Task.find({'rest':rest,'q7':'1'}).count()
		q7_2 = db.Task.find({'rest':rest,'q7':'2'}).count()
		q7_3 = db.Task.find({'rest':rest,'q7':'3'}).count()
		q7_4 = db.Task.find({'rest':rest,'q7':'4'}).count()
		q7_5 = db.Task.find({'rest':rest,'q7':'5'}).count()
		q8_1 = db.Task.find({'rest':rest,'q8':'1'}).count()
		q8_2 = db.Task.find({'rest':rest,'q8':'2'}).count()
		q8_3 = db.Task.find({'rest':rest,'q8':'3'}).count()
		q8_4 = db.Task.find({'rest':rest,'q8':'4'}).count()
		q8_5 = db.Task.find({'rest':rest,'q8':'5'}).count()
		q9_1 = db.Task.find({'rest':rest,'q9':'1'}).count()
		q9_2 = db.Task.find({'rest':rest,'q9':'2'}).count()
		q9_3 = db.Task.find({'rest':rest,'q9':'3'}).count()
		q9_4 = db.Task.find({'rest':rest,'q9':'4'}).count()
		q9_5 = db.Task.find({'rest':rest,'q9':'5'}).count()
		
		return render_template("rest_dash.html",logo = logo, no = rest , single = single, q1_1=q1_1, q1_2=q1_2, q1_3=q1_3,q1_4=q1_4,q1_5=q1_5,q2_1=q2_1, q2_2=q2_2, q2_3=q2_3,q2_4=q2_4,q2_5=q2_5,
		q3_1=q3_1, q3_2=q3_2, q3_3=q3_3,q3_4=q3_4,q3_5=q3_5,q4_1=q4_1, q4_2=q4_2, q4_3=q4_3,q4_4=q4_4,q4_5=q4_5,q5_1=q5_1, q5_2=q5_2, q5_3=q5_3,q5_4=q5_4,q5_5=q5_5,
		q6_1=q6_1, q6_2=q6_2, q6_3=q6_3,q6_4=q6_4,q6_5=q6_5,q7_1=q7_1, q7_2=q7_2, q7_3=q7_3,q7_4=q7_4,q7_5=q7_5,q8_1=q8_1, q8_2=q8_2, q8_3=q8_3,q8_4=q8_4,q8_5=q8_5,
		q9_1=q9_1, q9_2=q9_2, q9_3=q9_3,q9_4=q9_4,q9_5=q9_5,)
		#return render_template("display.html", tasks = tasks)
	return redirect(url_for('sess'))

#Data of each rating by each visitor per restaurant
@app.route('/get_rating_<rest>_today', methods = ['GET','POST'])
def get_rest_rating_today(rest):
	if 'user' in session:

		if rest == "1":
			logo = "les.png"
		elif rest == "2":
			logo = "cucina.png"
		elif rest == "3":
			logo = "chococafe.png"
		elif rest == "4":
			logo = "luna.png"

		#rest = "1"
		dov = datetime.datetime.now().strftime ("%Y-%m-%d")
		single = db.Task.find({'rest':rest,'dov':dov}).count()
		q1_1 = db.Task.find({'rest':rest,'q1':'1','dov':dov}).count()
		q1_2 = db.Task.find({'rest':rest,'q1':'2','dov':dov}).count()
		q1_3 = db.Task.find({'rest':rest,'q1':'3','dov':dov}).count()
		q1_4 = db.Task.find({'rest':rest,'q1':'4','dov':dov}).count()
		q1_5 = db.Task.find({'rest':rest,'q1':'5','dov':dov}).count()
		q2_1 = db.Task.find({'rest':rest,'q2':'1','dov':dov}).count()
		q2_2 = db.Task.find({'rest':rest,'q2':'2','dov':dov}).count()
		q2_3 = db.Task.find({'rest':rest,'q2':'3','dov':dov}).count()
		q2_4 = db.Task.find({'rest':rest,'q2':'4','dov':dov}).count()
		q2_5 = db.Task.find({'rest':rest,'q2':'5','dov':dov}).count()
		q3_1 = db.Task.find({'rest':rest,'q3':'1','dov':dov}).count()
		q3_2 = db.Task.find({'rest':rest,'q3':'2','dov':dov}).count()
		q3_3 = db.Task.find({'rest':rest,'q3':'3','dov':dov}).count()
		q3_4 = db.Task.find({'rest':rest,'q3':'4','dov':dov}).count()
		q3_5 = db.Task.find({'rest':rest,'q3':'5','dov':dov}).count()
		q4_1 = db.Task.find({'rest':rest,'q4':'1','dov':dov}).count()
		q4_2 = db.Task.find({'rest':rest,'q4':'2','dov':dov}).count()
		q4_3 = db.Task.find({'rest':rest,'q4':'3','dov':dov}).count()
		q4_4 = db.Task.find({'rest':rest,'q4':'4','dov':dov}).count()
		q4_5 = db.Task.find({'rest':rest,'q4':'5','dov':dov}).count()
		q5_1 = db.Task.find({'rest':rest,'q5':'1','dov':dov}).count()
		q5_2 = db.Task.find({'rest':rest,'q5':'2','dov':dov}).count()
		q5_3 = db.Task.find({'rest':rest,'q5':'3','dov':dov}).count()
		q5_4 = db.Task.find({'rest':rest,'q5':'4','dov':dov}).count()
		q5_5 = db.Task.find({'rest':rest,'q5':'5','dov':dov}).count()
		q6_1 = db.Task.find({'rest':rest,'q6':'1','dov':dov}).count()
		q6_2 = db.Task.find({'rest':rest,'q6':'2','dov':dov}).count()
		q6_3 = db.Task.find({'rest':rest,'q6':'3','dov':dov}).count()
		q6_4 = db.Task.find({'rest':rest,'q6':'4','dov':dov}).count()
		q6_5 = db.Task.find({'rest':rest,'q6':'5','dov':dov}).count()
		q7_1 = db.Task.find({'rest':rest,'q7':'1','dov':dov}).count()
		q7_2 = db.Task.find({'rest':rest,'q7':'2','dov':dov}).count()
		q7_3 = db.Task.find({'rest':rest,'q7':'3','dov':dov}).count()
		q7_4 = db.Task.find({'rest':rest,'q7':'4','dov':dov}).count()
		q7_5 = db.Task.find({'rest':rest,'q7':'5','dov':dov}).count()
		q8_1 = db.Task.find({'rest':rest,'q8':'1','dov':dov}).count()
		q8_2 = db.Task.find({'rest':rest,'q8':'2','dov':dov}).count()
		q8_3 = db.Task.find({'rest':rest,'q8':'3','dov':dov}).count()
		q8_4 = db.Task.find({'rest':rest,'q8':'4','dov':dov}).count()
		q8_5 = db.Task.find({'rest':rest,'q8':'5','dov':dov}).count()
		q9_1 = db.Task.find({'rest':rest,'q9':'1','dov':dov}).count()
		q9_2 = db.Task.find({'rest':rest,'q9':'2','dov':dov}).count()
		q9_3 = db.Task.find({'rest':rest,'q9':'3','dov':dov}).count()
		q9_4 = db.Task.find({'rest':rest,'q9':'4','dov':dov}).count()
		q9_5 = db.Task.find({'rest':rest,'q9':'5','dov':dov}).count()
		
		return render_template("rest_dash.html",logo = logo, no = rest , single = single, q1_1=q1_1, q1_2=q1_2, q1_3=q1_3,q1_4=q1_4,q1_5=q1_5,q2_1=q2_1, q2_2=q2_2, q2_3=q2_3,q2_4=q2_4,q2_5=q2_5,
		q3_1=q3_1, q3_2=q3_2, q3_3=q3_3,q3_4=q3_4,q3_5=q3_5,q4_1=q4_1, q4_2=q4_2, q4_3=q4_3,q4_4=q4_4,q4_5=q4_5,q5_1=q5_1, q5_2=q5_2, q5_3=q5_3,q5_4=q5_4,q5_5=q5_5,
		q6_1=q6_1, q6_2=q6_2, q6_3=q6_3,q6_4=q6_4,q6_5=q6_5,q7_1=q7_1, q7_2=q7_2, q7_3=q7_3,q7_4=q7_4,q7_5=q7_5,q8_1=q8_1, q8_2=q8_2, q8_3=q8_3,q8_4=q8_4,q8_5=q8_5,
		q9_1=q9_1, q9_2=q9_2, q9_3=q9_3,q9_4=q9_4,q9_5=q9_5,)
		#return render_template("display.html", tasks = tasks)
	return redirect(url_for('sess'))

#Data of each rating by each visitor per restaurant
@app.route('/get_rating_<rest>_dateon', methods = ['GET','POST'])
def get_rest_rating_dateon(rest):
	if 'user' in session:

		if rest == "1":
			logo = "les.png"
		elif rest == "2":
			logo = "cucina.png"
		elif rest == "3":
			logo = "chococafe.png"
		elif rest == "4":
			logo = "luna.png"

		#rest = "1"
		startdate = request.form['startdate']
		single = db.Task.find({'rest':rest, 'dov': startdate}).count()
		q1_1 = db.Task.find({'rest':rest,'q1':'1', 'dov': startdate}).count()
		q1_2 = db.Task.find({'rest':rest,'q1':'2', 'dov': startdate}).count()
		q1_3 = db.Task.find({'rest':rest,'q1':'3', 'dov': startdate}).count()
		q1_4 = db.Task.find({'rest':rest,'q1':'4', 'dov': startdate}).count()
		q1_5 = db.Task.find({'rest':rest,'q1':'5', 'dov': startdate}).count()
		q2_1 = db.Task.find({'rest':rest,'q2':'1', 'dov': startdate}).count()
		q2_2 = db.Task.find({'rest':rest,'q2':'2', 'dov': startdate}).count()
		q2_3 = db.Task.find({'rest':rest,'q2':'3', 'dov': startdate}).count()
		q2_4 = db.Task.find({'rest':rest,'q2':'4', 'dov': startdate}).count()
		q2_5 = db.Task.find({'rest':rest,'q2':'5', 'dov': startdate}).count()
		q3_1 = db.Task.find({'rest':rest,'q3':'1', 'dov': startdate}).count()
		q3_2 = db.Task.find({'rest':rest,'q3':'2', 'dov': startdate}).count()
		q3_3 = db.Task.find({'rest':rest,'q3':'3', 'dov': startdate}).count()
		q3_4 = db.Task.find({'rest':rest,'q3':'4', 'dov': startdate}).count()
		q3_5 = db.Task.find({'rest':rest,'q3':'5', 'dov': startdate}).count()
		q4_1 = db.Task.find({'rest':rest,'q4':'1', 'dov': startdate}).count()
		q4_2 = db.Task.find({'rest':rest,'q4':'2', 'dov': startdate}).count()
		q4_3 = db.Task.find({'rest':rest,'q4':'3', 'dov': startdate}).count()
		q4_4 = db.Task.find({'rest':rest,'q4':'4', 'dov': startdate}).count()
		q4_5 = db.Task.find({'rest':rest,'q4':'5', 'dov': startdate}).count()
		q5_1 = db.Task.find({'rest':rest,'q5':'1', 'dov': startdate}).count()
		q5_2 = db.Task.find({'rest':rest,'q5':'2', 'dov': startdate}).count()
		q5_3 = db.Task.find({'rest':rest,'q5':'3', 'dov': startdate}).count()
		q5_4 = db.Task.find({'rest':rest,'q5':'4', 'dov': startdate}).count()
		q5_5 = db.Task.find({'rest':rest,'q5':'5', 'dov': startdate}).count()
		q6_1 = db.Task.find({'rest':rest,'q6':'1', 'dov': startdate}).count()
		q6_2 = db.Task.find({'rest':rest,'q6':'2', 'dov': startdate}).count()
		q6_3 = db.Task.find({'rest':rest,'q6':'3', 'dov': startdate}).count()
		q6_4 = db.Task.find({'rest':rest,'q6':'4', 'dov': startdate}).count()
		q6_5 = db.Task.find({'rest':rest,'q6':'5', 'dov': startdate}).count()
		q7_1 = db.Task.find({'rest':rest,'q7':'1', 'dov': startdate}).count()
		q7_2 = db.Task.find({'rest':rest,'q7':'2', 'dov': startdate}).count()
		q7_3 = db.Task.find({'rest':rest,'q7':'3', 'dov': startdate}).count()
		q7_4 = db.Task.find({'rest':rest,'q7':'4', 'dov': startdate}).count()
		q7_5 = db.Task.find({'rest':rest,'q7':'5', 'dov': startdate}).count()
		q8_1 = db.Task.find({'rest':rest,'q8':'1', 'dov': startdate}).count()
		q8_2 = db.Task.find({'rest':rest,'q8':'2', 'dov': startdate}).count()
		q8_3 = db.Task.find({'rest':rest,'q8':'3', 'dov': startdate}).count()
		q8_4 = db.Task.find({'rest':rest,'q8':'4', 'dov': startdate}).count()
		q8_5 = db.Task.find({'rest':rest,'q8':'5', 'dov': startdate}).count()
		q9_1 = db.Task.find({'rest':rest,'q9':'1', 'dov': startdate}).count()
		q9_2 = db.Task.find({'rest':rest,'q9':'2', 'dov': startdate}).count()
		q9_3 = db.Task.find({'rest':rest,'q9':'3', 'dov': startdate}).count()
		q9_4 = db.Task.find({'rest':rest,'q9':'4', 'dov': startdate}).count()
		q9_5 = db.Task.find({'rest':rest,'q9':'5', 'dov': startdate}).count()
		
		return render_template("rest_dash.html",logo = logo, no = rest , single = single, q1_1=q1_1, q1_2=q1_2, q1_3=q1_3,q1_4=q1_4,q1_5=q1_5,q2_1=q2_1, q2_2=q2_2, q2_3=q2_3,q2_4=q2_4,q2_5=q2_5,
		q3_1=q3_1, q3_2=q3_2, q3_3=q3_3,q3_4=q3_4,q3_5=q3_5,q4_1=q4_1, q4_2=q4_2, q4_3=q4_3,q4_4=q4_4,q4_5=q4_5,q5_1=q5_1, q5_2=q5_2, q5_3=q5_3,q5_4=q5_4,q5_5=q5_5,
		q6_1=q6_1, q6_2=q6_2, q6_3=q6_3,q6_4=q6_4,q6_5=q6_5,q7_1=q7_1, q7_2=q7_2, q7_3=q7_3,q7_4=q7_4,q7_5=q7_5,q8_1=q8_1, q8_2=q8_2, q8_3=q8_3,q8_4=q8_4,q8_5=q8_5,
		q9_1=q9_1, q9_2=q9_2, q9_3=q9_3,q9_4=q9_4,q9_5=q9_5,)
		#return render_template("display.html", tasks = tasks)
	return redirect(url_for('sess'))

#Data of each rating by each visitor per restaurant
@app.route('/get_rating_<rest>_fromto', methods = ['GET','POST'])
def get_rest_rating_fromto(rest):
	if 'user' in session:

		if rest == "1":
			logo = "les.png"
		elif rest == "2":
			logo = "cucina.png"
		elif rest == "3":
			logo = "chococafe.png"
		elif rest == "4":
			logo = "luna.png"

		
		startdate = request.form['startdate']
		enddate = request.form['enddate']
		single = db.Task.find({'rest':rest,'dov': {"$gte": startdate,"$lt":enddate}}).count()
		q1_1 = db.Task.find({'rest':rest,'q1':'1','dov': {"$gte": startdate,"$lt":enddate}}).count()
		q1_2 = db.Task.find({'rest':rest,'q1':'2','dov': {"$gte": startdate,"$lt":enddate}}).count()
		q1_3 = db.Task.find({'rest':rest,'q1':'3','dov': {"$gte": startdate,"$lt":enddate}}).count()
		q1_4 = db.Task.find({'rest':rest,'q1':'4','dov': {"$gte": startdate,"$lt":enddate}}).count()
		q1_5 = db.Task.find({'rest':rest,'q1':'5','dov': {"$gte": startdate,"$lt":enddate}}).count()
		q2_1 = db.Task.find({'rest':rest,'q2':'1','dov': {"$gte": startdate,"$lt":enddate}}).count()
		q2_2 = db.Task.find({'rest':rest,'q2':'2','dov': {"$gte": startdate,"$lt":enddate}}).count()
		q2_3 = db.Task.find({'rest':rest,'q2':'3','dov': {"$gte": startdate,"$lt":enddate}}).count()
		q2_4 = db.Task.find({'rest':rest,'q2':'4','dov': {"$gte": startdate,"$lt":enddate}}).count()
		q2_5 = db.Task.find({'rest':rest,'q2':'5','dov': {"$gte": startdate,"$lt":enddate}}).count()
		q3_1 = db.Task.find({'rest':rest,'q3':'1','dov': {"$gte": startdate,"$lt":enddate}}).count()
		q3_2 = db.Task.find({'rest':rest,'q3':'2','dov': {"$gte": startdate,"$lt":enddate}}).count()
		q3_3 = db.Task.find({'rest':rest,'q3':'3','dov': {"$gte": startdate,"$lt":enddate}}).count()
		q3_4 = db.Task.find({'rest':rest,'q3':'4','dov': {"$gte": startdate,"$lt":enddate}}).count()
		q3_5 = db.Task.find({'rest':rest,'q3':'5','dov': {"$gte": startdate,"$lt":enddate}}).count()
		q4_1 = db.Task.find({'rest':rest,'q4':'1','dov': {"$gte": startdate,"$lt":enddate}}).count()
		q4_2 = db.Task.find({'rest':rest,'q4':'2','dov': {"$gte": startdate,"$lt":enddate}}).count()
		q4_3 = db.Task.find({'rest':rest,'q4':'3','dov': {"$gte": startdate,"$lt":enddate}}).count()
		q4_4 = db.Task.find({'rest':rest,'q4':'4','dov': {"$gte": startdate,"$lt":enddate}}).count()
		q4_5 = db.Task.find({'rest':rest,'q4':'5','dov': {"$gte": startdate,"$lt":enddate}}).count()
		q5_1 = db.Task.find({'rest':rest,'q5':'1','dov': {"$gte": startdate,"$lt":enddate}}).count()
		q5_2 = db.Task.find({'rest':rest,'q5':'2','dov': {"$gte": startdate,"$lt":enddate}}).count()
		q5_3 = db.Task.find({'rest':rest,'q5':'3','dov': {"$gte": startdate,"$lt":enddate}}).count()
		q5_4 = db.Task.find({'rest':rest,'q5':'4','dov': {"$gte": startdate,"$lt":enddate}}).count()
		q5_5 = db.Task.find({'rest':rest,'q5':'5','dov': {"$gte": startdate,"$lt":enddate}}).count()
		q6_1 = db.Task.find({'rest':rest,'q6':'1','dov': {"$gte": startdate,"$lt":enddate}}).count()
		q6_2 = db.Task.find({'rest':rest,'q6':'2','dov': {"$gte": startdate,"$lt":enddate}}).count()
		q6_3 = db.Task.find({'rest':rest,'q6':'3','dov': {"$gte": startdate,"$lt":enddate}}).count()
		q6_4 = db.Task.find({'rest':rest,'q6':'4','dov': {"$gte": startdate,"$lt":enddate}}).count()
		q6_5 = db.Task.find({'rest':rest,'q6':'5','dov': {"$gte": startdate,"$lt":enddate}}).count()
		q7_1 = db.Task.find({'rest':rest,'q7':'1','dov': {"$gte": startdate,"$lt":enddate}}).count()
		q7_2 = db.Task.find({'rest':rest,'q7':'2','dov': {"$gte": startdate,"$lt":enddate}}).count()
		q7_3 = db.Task.find({'rest':rest,'q7':'3','dov': {"$gte": startdate,"$lt":enddate}}).count()
		q7_4 = db.Task.find({'rest':rest,'q7':'4','dov': {"$gte": startdate,"$lt":enddate}}).count()
		q7_5 = db.Task.find({'rest':rest,'q7':'5','dov': {"$gte": startdate,"$lt":enddate}}).count()
		q8_1 = db.Task.find({'rest':rest,'q8':'1','dov': {"$gte": startdate,"$lt":enddate}}).count()
		q8_2 = db.Task.find({'rest':rest,'q8':'2','dov': {"$gte": startdate,"$lt":enddate}}).count()
		q8_3 = db.Task.find({'rest':rest,'q8':'3','dov': {"$gte": startdate,"$lt":enddate}}).count()
		q8_4 = db.Task.find({'rest':rest,'q8':'4','dov': {"$gte": startdate,"$lt":enddate}}).count()
		q8_5 = db.Task.find({'rest':rest,'q8':'5','dov': {"$gte": startdate,"$lt":enddate}}).count()
		q9_1 = db.Task.find({'rest':rest,'q9':'1','dov': {"$gte": startdate,"$lt":enddate}}).count()
		q9_2 = db.Task.find({'rest':rest,'q9':'2','dov': {"$gte": startdate,"$lt":enddate}}).count()
		q9_3 = db.Task.find({'rest':rest,'q9':'3','dov': {"$gte": startdate,"$lt":enddate}}).count()
		q9_4 = db.Task.find({'rest':rest,'q9':'4','dov': {"$gte": startdate,"$lt":enddate}}).count()
		q9_5 = db.Task.find({'rest':rest,'q9':'5','dov': {"$gte": startdate,"$lt":enddate}}).count()
		
		return render_template("rest_dash.html",logo = logo, no = rest , single = single, q1_1=q1_1, q1_2=q1_2, q1_3=q1_3,q1_4=q1_4,q1_5=q1_5,q2_1=q2_1, q2_2=q2_2, q2_3=q2_3,q2_4=q2_4,q2_5=q2_5,
		q3_1=q3_1, q3_2=q3_2, q3_3=q3_3,q3_4=q3_4,q3_5=q3_5,q4_1=q4_1, q4_2=q4_2, q4_3=q4_3,q4_4=q4_4,q4_5=q4_5,q5_1=q5_1, q5_2=q5_2, q5_3=q5_3,q5_4=q5_4,q5_5=q5_5,
		q6_1=q6_1, q6_2=q6_2, q6_3=q6_3,q6_4=q6_4,q6_5=q6_5,q7_1=q7_1, q7_2=q7_2, q7_3=q7_3,q7_4=q7_4,q7_5=q7_5,q8_1=q8_1, q8_2=q8_2, q8_3=q8_3,q8_4=q8_4,q8_5=q8_5,
		q9_1=q9_1, q9_2=q9_2, q9_3=q9_3,q9_4=q9_4,q9_5=q9_5,)
		#return render_template("display.html", tasks = tasks)
	return redirect(url_for('sess'))


#Data of each rating by each visitor per restaurant
@app.route('/get_<spa>', methods = ['GET'])
def get_spa_rating(spa):
	if 'user' in session:
		single = db.Task.find({'spa':spa}).count()
		sq1_1 = db.Task.find({'spa':spa,'sq1':'1'}).count()
		sq1_2 = db.Task.find({'spa':spa,'sq1':'2'}).count()
		sq1_3 = db.Task.find({'spa':spa,'sq1':'3'}).count()
		sq1_4 = db.Task.find({'spa':spa,'sq1':'4'}).count()
		sq1_5 = db.Task.find({'spa':spa,'sq1':'5'}).count()
		sq2_1 = db.Task.find({'spa':spa,'sq2':'1'}).count()
		sq2_2 = db.Task.find({'spa':spa,'sq2':'2'}).count()
		sq2_3 = db.Task.find({'spa':spa,'sq2':'3'}).count()
		sq2_4 = db.Task.find({'spa':spa,'sq2':'4'}).count()
		sq2_5 = db.Task.find({'spa':spa,'sq2':'5'}).count()
		sq3_1 = db.Task.find({'spa':spa,'sq3':'1'}).count()
		sq3_2 = db.Task.find({'spa':spa,'sq3':'2'}).count()
		sq3_3 = db.Task.find({'spa':spa,'sq3':'3'}).count()
		sq3_4 = db.Task.find({'spa':spa,'sq3':'4'}).count()
		sq3_5 = db.Task.find({'spa':spa,'sq3':'5'}).count()
		sq4_1 = db.Task.find({'spa':spa,'sq4':'1'}).count()
		sq4_2 = db.Task.find({'spa':spa,'sq4':'2'}).count()
		sq4_3 = db.Task.find({'spa':spa,'sq4':'3'}).count()
		sq4_4 = db.Task.find({'spa':spa,'sq4':'4'}).count()
		sq4_5 = db.Task.find({'spa':spa,'sq4':'5'}).count()
		sq5_1 = db.Task.find({'spa':spa,'sq5':'1'}).count()
		sq5_2 = db.Task.find({'spa':spa,'sq5':'2'}).count()
		sq5_3 = db.Task.find({'spa':spa,'sq5':'3'}).count()
		sq5_4 = db.Task.find({'spa':spa,'sq5':'4'}).count()
		sq5_5 = db.Task.find({'spa':spa,'sq5':'5'}).count()
		sq6_1 = db.Task.find({'spa':spa,'sq6':'1'}).count()
		sq6_2 = db.Task.find({'spa':spa,'sq6':'2'}).count()
		sq6_3 = db.Task.find({'spa':spa,'sq6':'3'}).count()
		sq6_4 = db.Task.find({'spa':spa,'sq6':'4'}).count()
		sq6_5 = db.Task.find({'spa':spa,'sq6':'5'}).count()
		sq7_1 = db.Task.find({'spa':spa,'sq7':'1'}).count()
		sq7_2 = db.Task.find({'spa':spa,'sq7':'2'}).count()
		sq7_3 = db.Task.find({'spa':spa,'sq7':'3'}).count()
		sq7_4 = db.Task.find({'spa':spa,'sq7':'4'}).count()
		sq7_5 = db.Task.find({'spa':spa,'sq7':'5'}).count()
		sq8_1 = db.Task.find({'spa':spa,'sq8':'1'}).count()
		sq8_2 = db.Task.find({'spa':spa,'sq8':'2'}).count()
		sq8_3 = db.Task.find({'spa':spa,'sq8':'3'}).count()
		sq8_4 = db.Task.find({'spa':spa,'sq8':'4'}).count()
		sq8_5 = db.Task.find({'spa':spa,'sq8':'5'}).count()
		sq9_1 = db.Task.find({'spa':spa,'sq9':'1'}).count()
		sq9_2 = db.Task.find({'spa':spa,'sq9':'2'}).count()
		sq9_3 = db.Task.find({'spa':spa,'sq9':'3'}).count()
		sq9_4 = db.Task.find({'spa':spa,'sq9':'4'}).count()
		sq9_5 = db.Task.find({'spa':spa,'sq9':'5'}).count()
		
		return render_template("spa_dash.html",single = single, sq1_1=sq1_1, sq1_2=sq1_2, sq1_3=sq1_3,sq1_4=sq1_4,sq1_5=sq1_5,sq2_1=sq2_1, sq2_2=sq2_2, sq2_3=sq2_3,sq2_4=sq2_4,sq2_5=sq2_5,
		sq3_1=sq3_1, sq3_2=sq3_2, sq3_3=sq3_3,sq3_4=sq3_4,sq3_5=sq3_5,sq4_1=sq4_1, sq4_2=sq4_2, sq4_3=sq4_3,sq4_4=sq4_4,sq4_5=sq4_5,sq5_1=sq5_1, sq5_2=sq5_2, sq5_3=sq5_3,sq5_4=sq5_4,sq5_5=sq5_5,
		sq6_1=sq6_1, sq6_2=sq6_2, sq6_3=sq6_3,sq6_4=sq6_4,sq6_5=sq6_5,sq7_1=sq7_1, sq7_2=sq7_2, sq7_3=sq7_3,sq7_4=sq7_4,sq7_5=sq7_5,sq8_1=sq8_1, sq8_2=sq8_2, sq8_3=sq8_3,sq8_4=sq8_4,sq8_5=sq8_5,
		sq9_1=sq9_1, sq9_2=sq9_2, sq9_3=sq9_3,sq9_4=sq9_4,sq9_5=sq9_5,)
		#return render_template("display.html", tasks = tasks)
	return redirect(url_for('sess'))

#Data of each rating by each visitor per restaurant
@app.route('/get_rate_<spa>_today', methods = ['GET','POST'])
def get_spa_rating_today(spa):
	if 'user' in session:
		dov = datetime.datetime.now().strftime ("%Y-%m-%d")
		single = db.Task.find({'spa':spa,'dov':dov}).count()
		sq1_1 = db.Task.find({'spa':spa,'sq1':'1','dov':dov}).count()
		sq1_2 = db.Task.find({'spa':spa,'sq1':'2','dov':dov}).count()
		sq1_3 = db.Task.find({'spa':spa,'sq1':'3','dov':dov}).count()
		sq1_4 = db.Task.find({'spa':spa,'sq1':'4','dov':dov}).count()
		sq1_5 = db.Task.find({'spa':spa,'sq1':'5','dov':dov}).count()
		sq2_1 = db.Task.find({'spa':spa,'sq2':'1','dov':dov}).count()
		sq2_2 = db.Task.find({'spa':spa,'sq2':'2','dov':dov}).count()
		sq2_3 = db.Task.find({'spa':spa,'sq2':'3','dov':dov}).count()
		sq2_4 = db.Task.find({'spa':spa,'sq2':'4','dov':dov}).count()
		sq2_5 = db.Task.find({'spa':spa,'sq2':'5','dov':dov}).count()
		sq3_1 = db.Task.find({'spa':spa,'sq3':'1','dov':dov}).count()
		sq3_2 = db.Task.find({'spa':spa,'sq3':'2','dov':dov}).count()
		sq3_3 = db.Task.find({'spa':spa,'sq3':'3','dov':dov}).count()
		sq3_4 = db.Task.find({'spa':spa,'sq3':'4','dov':dov}).count()
		sq3_5 = db.Task.find({'spa':spa,'sq3':'5','dov':dov}).count()
		sq4_1 = db.Task.find({'spa':spa,'sq4':'1','dov':dov}).count()
		sq4_2 = db.Task.find({'spa':spa,'sq4':'2','dov':dov}).count()
		sq4_3 = db.Task.find({'spa':spa,'sq4':'3','dov':dov}).count()
		sq4_4 = db.Task.find({'spa':spa,'sq4':'4','dov':dov}).count()
		sq4_5 = db.Task.find({'spa':spa,'sq4':'5','dov':dov}).count()
		sq5_1 = db.Task.find({'spa':spa,'sq5':'1','dov':dov}).count()
		sq5_2 = db.Task.find({'spa':spa,'sq5':'2','dov':dov}).count()
		sq5_3 = db.Task.find({'spa':spa,'sq5':'3','dov':dov}).count()
		sq5_4 = db.Task.find({'spa':spa,'sq5':'4','dov':dov}).count()
		sq5_5 = db.Task.find({'spa':spa,'sq5':'5','dov':dov}).count()
		sq6_1 = db.Task.find({'spa':spa,'sq6':'1','dov':dov}).count()
		sq6_2 = db.Task.find({'spa':spa,'sq6':'2','dov':dov}).count()
		sq6_3 = db.Task.find({'spa':spa,'sq6':'3','dov':dov}).count()
		sq6_4 = db.Task.find({'spa':spa,'sq6':'4','dov':dov}).count()
		sq6_5 = db.Task.find({'spa':spa,'sq6':'5','dov':dov}).count()
		sq7_1 = db.Task.find({'spa':spa,'sq7':'1','dov':dov}).count()
		sq7_2 = db.Task.find({'spa':spa,'sq7':'2','dov':dov}).count()
		sq7_3 = db.Task.find({'spa':spa,'sq7':'3','dov':dov}).count()
		sq7_4 = db.Task.find({'spa':spa,'sq7':'4','dov':dov}).count()
		sq7_5 = db.Task.find({'spa':spa,'sq7':'5','dov':dov}).count()
		sq8_1 = db.Task.find({'spa':spa,'sq8':'1','dov':dov}).count()
		sq8_2 = db.Task.find({'spa':spa,'sq8':'2','dov':dov}).count()
		sq8_3 = db.Task.find({'spa':spa,'sq8':'3','dov':dov}).count()
		sq8_4 = db.Task.find({'spa':spa,'sq8':'4','dov':dov}).count()
		sq8_5 = db.Task.find({'spa':spa,'sq8':'5','dov':dov}).count()
		sq9_1 = db.Task.find({'spa':spa,'sq9':'1','dov':dov}).count()
		sq9_2 = db.Task.find({'spa':spa,'sq9':'2','dov':dov}).count()
		sq9_3 = db.Task.find({'spa':spa,'sq9':'3','dov':dov}).count()
		sq9_4 = db.Task.find({'spa':spa,'sq9':'4','dov':dov}).count()
		sq9_5 = db.Task.find({'spa':spa,'sq9':'5','dov':dov}).count()
		
		return render_template("spa_dash.html",single = single, sq1_1=sq1_1, sq1_2=sq1_2, sq1_3=sq1_3,sq1_4=sq1_4,sq1_5=sq1_5,sq2_1=sq2_1, sq2_2=sq2_2, sq2_3=sq2_3,sq2_4=sq2_4,sq2_5=sq2_5,
		sq3_1=sq3_1, sq3_2=sq3_2, sq3_3=sq3_3,sq3_4=sq3_4,sq3_5=sq3_5,sq4_1=sq4_1, sq4_2=sq4_2, sq4_3=sq4_3,sq4_4=sq4_4,sq4_5=sq4_5,sq5_1=sq5_1, sq5_2=sq5_2, sq5_3=sq5_3,sq5_4=sq5_4,sq5_5=sq5_5,
		sq6_1=sq6_1, sq6_2=sq6_2, sq6_3=sq6_3,sq6_4=sq6_4,sq6_5=sq6_5,sq7_1=sq7_1, sq7_2=sq7_2, sq7_3=sq7_3,sq7_4=sq7_4,sq7_5=sq7_5,sq8_1=sq8_1, sq8_2=sq8_2, sq8_3=sq8_3,sq8_4=sq8_4,sq8_5=sq8_5,
		sq9_1=sq9_1, sq9_2=sq9_2, sq9_3=sq9_3,sq9_4=sq9_4,sq9_5=sq9_5,)
		#return render_template("display.html", tasks = tasks)
	return redirect(url_for('sess'))

#Data of each rating by each visitor per restaurant
@app.route('/get_rate_<spa>_dateon', methods = ['GET','POST'])
def get_spa_rating_dateon(spa):
	if 'user' in session:
		startdate = request.form['startdate']
		single = db.Task.find({'spa':spa, 'dov': startdate}).count()
		sq1_1 = db.Task.find({'spa':spa,'sq1':'1', 'dov': startdate}).count()
		sq1_2 = db.Task.find({'spa':spa,'sq1':'2', 'dov': startdate}).count()
		sq1_3 = db.Task.find({'spa':spa,'sq1':'3', 'dov': startdate}).count()
		sq1_4 = db.Task.find({'spa':spa,'sq1':'4', 'dov': startdate}).count()
		sq1_5 = db.Task.find({'spa':spa,'sq1':'5', 'dov': startdate}).count()
		sq2_1 = db.Task.find({'spa':spa,'sq2':'1', 'dov': startdate}).count()
		sq2_2 = db.Task.find({'spa':spa,'sq2':'2', 'dov': startdate}).count()
		sq2_3 = db.Task.find({'spa':spa,'sq2':'3', 'dov': startdate}).count()
		sq2_4 = db.Task.find({'spa':spa,'sq2':'4', 'dov': startdate}).count()
		sq2_5 = db.Task.find({'spa':spa,'sq2':'5', 'dov': startdate}).count()
		sq3_1 = db.Task.find({'spa':spa,'sq3':'1', 'dov': startdate}).count()
		sq3_2 = db.Task.find({'spa':spa,'sq3':'2', 'dov': startdate}).count()
		sq3_3 = db.Task.find({'spa':spa,'sq3':'3', 'dov': startdate}).count()
		sq3_4 = db.Task.find({'spa':spa,'sq3':'4', 'dov': startdate}).count()
		sq3_5 = db.Task.find({'spa':spa,'sq3':'5', 'dov': startdate}).count()
		sq4_1 = db.Task.find({'spa':spa,'sq4':'1', 'dov': startdate}).count()
		sq4_2 = db.Task.find({'spa':spa,'sq4':'2', 'dov': startdate}).count()
		sq4_3 = db.Task.find({'spa':spa,'sq4':'3', 'dov': startdate}).count()
		sq4_4 = db.Task.find({'spa':spa,'sq4':'4', 'dov': startdate}).count()
		sq4_5 = db.Task.find({'spa':spa,'sq4':'5', 'dov': startdate}).count()
		sq5_1 = db.Task.find({'spa':spa,'sq5':'1', 'dov': startdate}).count()
		sq5_2 = db.Task.find({'spa':spa,'sq5':'2', 'dov': startdate}).count()
		sq5_3 = db.Task.find({'spa':spa,'sq5':'3', 'dov': startdate}).count()
		sq5_4 = db.Task.find({'spa':spa,'sq5':'4', 'dov': startdate}).count()
		sq5_5 = db.Task.find({'spa':spa,'sq5':'5', 'dov': startdate}).count()
		sq6_1 = db.Task.find({'spa':spa,'sq6':'1', 'dov': startdate}).count()
		sq6_2 = db.Task.find({'spa':spa,'sq6':'2', 'dov': startdate}).count()
		sq6_3 = db.Task.find({'spa':spa,'sq6':'3', 'dov': startdate}).count()
		sq6_4 = db.Task.find({'spa':spa,'sq6':'4', 'dov': startdate}).count()
		sq6_5 = db.Task.find({'spa':spa,'sq6':'5', 'dov': startdate}).count()
		sq7_1 = db.Task.find({'spa':spa,'sq7':'1', 'dov': startdate}).count()
		sq7_2 = db.Task.find({'spa':spa,'sq7':'2', 'dov': startdate}).count()
		sq7_3 = db.Task.find({'spa':spa,'sq7':'3', 'dov': startdate}).count()
		sq7_4 = db.Task.find({'spa':spa,'sq7':'4', 'dov': startdate}).count()
		sq7_5 = db.Task.find({'spa':spa,'sq7':'5', 'dov': startdate}).count()
		sq8_1 = db.Task.find({'spa':spa,'sq8':'1', 'dov': startdate}).count()
		sq8_2 = db.Task.find({'spa':spa,'sq8':'2', 'dov': startdate}).count()
		sq8_3 = db.Task.find({'spa':spa,'sq8':'3', 'dov': startdate}).count()
		sq8_4 = db.Task.find({'spa':spa,'sq8':'4', 'dov': startdate}).count()
		sq8_5 = db.Task.find({'spa':spa,'sq8':'5', 'dov': startdate}).count()
		sq9_1 = db.Task.find({'spa':spa,'sq9':'1', 'dov': startdate}).count()
		sq9_2 = db.Task.find({'spa':spa,'sq9':'2', 'dov': startdate}).count()
		sq9_3 = db.Task.find({'spa':spa,'sq9':'3', 'dov': startdate}).count()
		sq9_4 = db.Task.find({'spa':spa,'sq9':'4', 'dov': startdate}).count()
		sq9_5 = db.Task.find({'spa':spa,'sq9':'5', 'dov': startdate}).count()
		
		return render_template("spa_dash.html",single = single, sq1_1=sq1_1, sq1_2=sq1_2, sq1_3=sq1_3,sq1_4=sq1_4,sq1_5=sq1_5,sq2_1=sq2_1, sq2_2=sq2_2, sq2_3=sq2_3,sq2_4=sq2_4,sq2_5=sq2_5,
		sq3_1=sq3_1, sq3_2=sq3_2, sq3_3=sq3_3,sq3_4=sq3_4,sq3_5=sq3_5,sq4_1=sq4_1, sq4_2=sq4_2, sq4_3=sq4_3,sq4_4=sq4_4,sq4_5=sq4_5,sq5_1=sq5_1, sq5_2=sq5_2, sq5_3=sq5_3,sq5_4=sq5_4,sq5_5=sq5_5,
		sq6_1=sq6_1, sq6_2=sq6_2, sq6_3=sq6_3,sq6_4=sq6_4,sq6_5=sq6_5,sq7_1=sq7_1, sq7_2=sq7_2, sq7_3=sq7_3,sq7_4=sq7_4,sq7_5=sq7_5,sq8_1=sq8_1, sq8_2=sq8_2, sq8_3=sq8_3,sq8_4=sq8_4,sq8_5=sq8_5,
		sq9_1=sq9_1, sq9_2=sq9_2, sq9_3=sq9_3,sq9_4=sq9_4,sq9_5=sq9_5,)
		#return render_template("display.html", tasks = tasks)
	return redirect(url_for('sess'))

#Data of each rating by each visitor per restaurant
@app.route('/get_rate_<spa>_fromto', methods = ['GET','POST'])
def get_spa_rating_fromto(spa):
	if 'user' in session:
		startdate = request.form['startdate']
		enddate = request.form['enddate']

		single = db.Task.find({'spa':spa,'dov': {"$gte": startdate,"$lt":enddate}}).count()
		sq1_1 = db.Task.find({'spa':spa,'sq1':'1','dov': {"$gte": startdate,"$lt":enddate}}).count()
		sq1_2 = db.Task.find({'spa':spa,'sq1':'2','dov': {"$gte": startdate,"$lt":enddate}}).count()
		sq1_3 = db.Task.find({'spa':spa,'sq1':'3','dov': {"$gte": startdate,"$lt":enddate}}).count()
		sq1_4 = db.Task.find({'spa':spa,'sq1':'4','dov': {"$gte": startdate,"$lt":enddate}}).count()
		sq1_5 = db.Task.find({'spa':spa,'sq1':'5','dov': {"$gte": startdate,"$lt":enddate}}).count()
		sq2_1 = db.Task.find({'spa':spa,'sq2':'1','dov': {"$gte": startdate,"$lt":enddate}}).count()
		sq2_2 = db.Task.find({'spa':spa,'sq2':'2','dov': {"$gte": startdate,"$lt":enddate}}).count()
		sq2_3 = db.Task.find({'spa':spa,'sq2':'3','dov': {"$gte": startdate,"$lt":enddate}}).count()
		sq2_4 = db.Task.find({'spa':spa,'sq2':'4','dov': {"$gte": startdate,"$lt":enddate}}).count()
		sq2_5 = db.Task.find({'spa':spa,'sq2':'5','dov': {"$gte": startdate,"$lt":enddate}}).count()
		sq3_1 = db.Task.find({'spa':spa,'sq3':'1','dov': {"$gte": startdate,"$lt":enddate}}).count()
		sq3_2 = db.Task.find({'spa':spa,'sq3':'2','dov': {"$gte": startdate,"$lt":enddate}}).count()
		sq3_3 = db.Task.find({'spa':spa,'sq3':'3','dov': {"$gte": startdate,"$lt":enddate}}).count()
		sq3_4 = db.Task.find({'spa':spa,'sq3':'4','dov': {"$gte": startdate,"$lt":enddate}}).count()
		sq3_5 = db.Task.find({'spa':spa,'sq3':'5','dov': {"$gte": startdate,"$lt":enddate}}).count()
		sq4_1 = db.Task.find({'spa':spa,'sq4':'1','dov': {"$gte": startdate,"$lt":enddate}}).count()
		sq4_2 = db.Task.find({'spa':spa,'sq4':'2','dov': {"$gte": startdate,"$lt":enddate}}).count()
		sq4_3 = db.Task.find({'spa':spa,'sq4':'3','dov': {"$gte": startdate,"$lt":enddate}}).count()
		sq4_4 = db.Task.find({'spa':spa,'sq4':'4','dov': {"$gte": startdate,"$lt":enddate}}).count()
		sq4_5 = db.Task.find({'spa':spa,'sq4':'5','dov': {"$gte": startdate,"$lt":enddate}}).count()
		sq5_1 = db.Task.find({'spa':spa,'sq5':'1','dov': {"$gte": startdate,"$lt":enddate}}).count()
		sq5_2 = db.Task.find({'spa':spa,'sq5':'2','dov': {"$gte": startdate,"$lt":enddate}}).count()
		sq5_3 = db.Task.find({'spa':spa,'sq5':'3','dov': {"$gte": startdate,"$lt":enddate}}).count()
		sq5_4 = db.Task.find({'spa':spa,'sq5':'4','dov': {"$gte": startdate,"$lt":enddate}}).count()
		sq5_5 = db.Task.find({'spa':spa,'sq5':'5','dov': {"$gte": startdate,"$lt":enddate}}).count()
		sq6_1 = db.Task.find({'spa':spa,'sq6':'1','dov': {"$gte": startdate,"$lt":enddate}}).count()
		sq6_2 = db.Task.find({'spa':spa,'sq6':'2','dov': {"$gte": startdate,"$lt":enddate}}).count()
		sq6_3 = db.Task.find({'spa':spa,'sq6':'3','dov': {"$gte": startdate,"$lt":enddate}}).count()
		sq6_4 = db.Task.find({'spa':spa,'sq6':'4','dov': {"$gte": startdate,"$lt":enddate}}).count()
		sq6_5 = db.Task.find({'spa':spa,'sq6':'5','dov': {"$gte": startdate,"$lt":enddate}}).count()
		sq7_1 = db.Task.find({'spa':spa,'sq7':'1','dov': {"$gte": startdate,"$lt":enddate}}).count()
		sq7_2 = db.Task.find({'spa':spa,'sq7':'2','dov': {"$gte": startdate,"$lt":enddate}}).count()
		sq7_3 = db.Task.find({'spa':spa,'sq7':'3','dov': {"$gte": startdate,"$lt":enddate}}).count()
		sq7_4 = db.Task.find({'spa':spa,'sq7':'4','dov': {"$gte": startdate,"$lt":enddate}}).count()
		sq7_5 = db.Task.find({'spa':spa,'sq7':'5','dov': {"$gte": startdate,"$lt":enddate}}).count()
		sq8_1 = db.Task.find({'spa':spa,'sq8':'1','dov': {"$gte": startdate,"$lt":enddate}}).count()
		sq8_2 = db.Task.find({'spa':spa,'sq8':'2','dov': {"$gte": startdate,"$lt":enddate}}).count()
		sq8_3 = db.Task.find({'spa':spa,'sq8':'3','dov': {"$gte": startdate,"$lt":enddate}}).count()
		sq8_4 = db.Task.find({'spa':spa,'sq8':'4','dov': {"$gte": startdate,"$lt":enddate}}).count()
		sq8_5 = db.Task.find({'spa':spa,'sq8':'5','dov': {"$gte": startdate,"$lt":enddate}}).count()
		sq9_1 = db.Task.find({'spa':spa,'sq9':'1','dov': {"$gte": startdate,"$lt":enddate}}).count()
		sq9_2 = db.Task.find({'spa':spa,'sq9':'2','dov': {"$gte": startdate,"$lt":enddate}}).count()
		sq9_3 = db.Task.find({'spa':spa,'sq9':'3','dov': {"$gte": startdate,"$lt":enddate}}).count()
		sq9_4 = db.Task.find({'spa':spa,'sq9':'4','dov': {"$gte": startdate,"$lt":enddate}}).count()
		sq9_5 = db.Task.find({'spa':spa,'sq9':'5','dov': {"$gte": startdate,"$lt":enddate}}).count()
		
		return render_template("spa_dash.html",single = single, sq1_1=sq1_1, sq1_2=sq1_2, sq1_3=sq1_3,sq1_4=sq1_4,sq1_5=sq1_5,sq2_1=sq2_1, sq2_2=sq2_2, sq2_3=sq2_3,sq2_4=sq2_4,sq2_5=sq2_5,
		sq3_1=sq3_1, sq3_2=sq3_2, sq3_3=sq3_3,sq3_4=sq3_4,sq3_5=sq3_5,sq4_1=sq4_1, sq4_2=sq4_2, sq4_3=sq4_3,sq4_4=sq4_4,sq4_5=sq4_5,sq5_1=sq5_1, sq5_2=sq5_2, sq5_3=sq5_3,sq5_4=sq5_4,sq5_5=sq5_5,
		sq6_1=sq6_1, sq6_2=sq6_2, sq6_3=sq6_3,sq6_4=sq6_4,sq6_5=sq6_5,sq7_1=sq7_1, sq7_2=sq7_2, sq7_3=sq7_3,sq7_4=sq7_4,sq7_5=sq7_5,sq8_1=sq8_1, sq8_2=sq8_2, sq8_3=sq8_3,sq8_4=sq8_4,sq8_5=sq8_5,
		sq9_1=sq9_1, sq9_2=sq9_2, sq9_3=sq9_3,sq9_4=sq9_4,sq9_5=sq9_5,)
		#return render_template("display.html", tasks = tasks)
	return redirect(url_for('sess'))

#total number of visitors
@app.route('/get_total', methods = ['GET','POST'])
def get_total():
	if 'user' in session:

		total = db.Task.count()
		rest1 = db.Task.find({'rest':'1'}).count()
		rest2 = db.Task.find({'rest':'2'}).count()
		rest3 = db.Task.find({'rest':'3'}).count()
		rest4 = db.Task.find({'rest':'4'}).count()
		rest5 = db.Task.find({'rest':'5'}).count()
		rest6 = db.Task.find({'rest':'6'}).count()
		total2 = db.Task.find({'spa':'spa'}).count()

		q1_1 = db.Task.find({'q1':'1'}).count()
		q2_1 = db.Task.find({'q2':'1'}).count()
		q3_1 = db.Task.find({'q3':'1'}).count()
		q4_1 = db.Task.find({'q4':'1'}).count()
		q5_1 = db.Task.find({'q5':'1'}).count()
		q6_1 = db.Task.find({'q6':'1'}).count()
		q7_1 = db.Task.find({'q7':'1'}).count()
		q8_1 = db.Task.find({'q8':'1'}).count()
		q9_1 = db.Task.find({'q9':'1'}).count()
		q1 = q1_1+q2_1+q3_1+q4_1+q5_1+q6_1+q7_1+q8_1+q9_1

		q1_2 = db.Task.find({'q1':'2'}).count()
		q2_2 = db.Task.find({'q2':'2'}).count()
		q3_2 = db.Task.find({'q3':'2'}).count()
		q4_2 = db.Task.find({'q4':'2'}).count()
		q5_2 = db.Task.find({'q5':'2'}).count()
		q6_2 = db.Task.find({'q6':'2'}).count()
		q7_2 = db.Task.find({'q7':'2'}).count()
		q8_2 = db.Task.find({'q8':'2'}).count()
		q9_2 = db.Task.find({'q9':'2'}).count()
		q2 = q1_2+q2_2+q3_2+q4_2+q5_2+q6_2+q7_2+q8_2+q9_2

		q1_3 = db.Task.find({'q1':'3'}).count()
		q2_3 = db.Task.find({'q2':'3'}).count()
		q3_3 = db.Task.find({'q3':'3'}).count()
		q4_3 = db.Task.find({'q4':'3'}).count()
		q5_3 = db.Task.find({'q5':'3'}).count()
		q6_3 = db.Task.find({'q6':'3'}).count()
		q7_3 = db.Task.find({'q7':'3'}).count()
		q8_3 = db.Task.find({'q8':'3'}).count()
		q9_3 = db.Task.find({'q9':'3'}).count()
		q3 = q1_3+q2_3+q3_3+q4_3+q5_3+q6_3+q7_3+q8_3+q9_3

		q1_4 = db.Task.find({'q1':'4'}).count()
		q2_4 = db.Task.find({'q2':'4'}).count()
		q3_4 = db.Task.find({'q3':'4'}).count()
		q4_4 = db.Task.find({'q4':'4'}).count()
		q5_4 = db.Task.find({'q5':'4'}).count()
		q6_4 = db.Task.find({'q6':'4'}).count()
		q7_4 = db.Task.find({'q7':'4'}).count()
		q8_4 = db.Task.find({'q8':'4'}).count()
		q9_4 = db.Task.find({'q9':'4'}).count()
		q4 = q1_4+q2_4+q3_4+q4_4+q5_4+q6_4+q7_4+q8_4+q9_4

		q1_5 = db.Task.find({'q1':'5'}).count()
		q2_5 = db.Task.find({'q2':'5'}).count()
		q3_5 = db.Task.find({'q3':'5'}).count()
		q4_5 = db.Task.find({'q4':'5'}).count()
		q5_5 = db.Task.find({'q5':'5'}).count()
		q6_5 = db.Task.find({'q6':'5'}).count()
		q7_5 = db.Task.find({'q7':'5'}).count()
		q8_5 = db.Task.find({'q8':'5'}).count()
		q9_5 = db.Task.find({'q9':'5'}).count()
		q5 = q1_5+q2_5+q3_5+q4_5+q5_5+q6_5+q7_5+q8_5+q9_5
		
		sq1_1 = db.Task.find({'sq1':'1'}).count()
		sq2_1 = db.Task.find({'sq2':'1'}).count()
		sq3_1 = db.Task.find({'sq3':'1'}).count()
		sq4_1 = db.Task.find({'sq4':'1'}).count()
		sq5_1 = db.Task.find({'sq5':'1'}).count()
		sq6_1 = db.Task.find({'sq6':'1'}).count()
		sq7_1 = db.Task.find({'sq7':'1'}).count()
		sq8_1 = db.Task.find({'sq8':'1'}).count()
		sq9_1 = db.Task.find({'sq9':'1'}).count()
		sq1 = sq1_1+sq2_1+sq3_1+sq4_1+sq5_1+sq6_1+sq7_1+sq8_1+sq9_1

		sq1_2 = db.Task.find({'sq1':'2'}).count()
		sq2_2 = db.Task.find({'sq2':'2'}).count()
		sq3_2 = db.Task.find({'sq3':'2'}).count()
		sq4_2 = db.Task.find({'sq4':'2'}).count()
		sq5_2 = db.Task.find({'sq5':'2'}).count()
		sq6_2 = db.Task.find({'sq6':'2'}).count()
		sq7_2 = db.Task.find({'sq7':'2'}).count()
		sq8_2 = db.Task.find({'sq8':'2'}).count()
		sq9_2 = db.Task.find({'sq9':'2'}).count()
		sq2 = sq1_2+sq2_2+sq3_2+sq4_2+sq5_2+sq6_2+sq7_2+sq8_2+sq9_2

		sq1_3 = db.Task.find({'sq1':'3'}).count()
		sq2_3 = db.Task.find({'sq2':'3'}).count()
		sq3_3 = db.Task.find({'sq3':'3'}).count()
		sq4_3 = db.Task.find({'sq4':'3'}).count()
		sq5_3 = db.Task.find({'sq5':'3'}).count()
		sq6_3 = db.Task.find({'sq6':'3'}).count()
		sq7_3 = db.Task.find({'sq7':'3'}).count()
		sq8_3 = db.Task.find({'sq8':'3'}).count()
		sq9_3 = db.Task.find({'sq9':'3'}).count()
		sq3 = sq1_3+sq2_3+sq3_3+sq4_3+sq5_3+sq6_3+sq7_3+sq8_3+sq9_3

		sq1_4 = db.Task.find({'sq1':'4'}).count()
		sq2_4 = db.Task.find({'sq2':'4'}).count()
		sq3_4 = db.Task.find({'sq3':'4'}).count()
		sq4_4 = db.Task.find({'sq4':'4'}).count()
		sq5_4 = db.Task.find({'sq5':'4'}).count()
		sq6_4 = db.Task.find({'sq6':'4'}).count()
		sq7_4 = db.Task.find({'sq7':'4'}).count()
		sq8_4 = db.Task.find({'sq8':'4'}).count()
		sq9_4 = db.Task.find({'sq9':'4'}).count()
		sq4 = sq1_4+sq2_4+sq3_4+sq4_4+sq5_4+sq6_4+sq7_4+sq8_4+sq9_4

		sq1_5 = db.Task.find({'sq1':'5'}).count()
		sq2_5 = db.Task.find({'sq2':'5'}).count()
		sq3_5 = db.Task.find({'sq3':'5'}).count()
		sq4_5 = db.Task.find({'sq4':'5'}).count()
		sq5_5 = db.Task.find({'sq5':'5'}).count()
		sq6_5 = db.Task.find({'sq6':'5'}).count()
		sq7_5 = db.Task.find({'sq7':'5'}).count()
		sq8_5 = db.Task.find({'sq8':'5'}).count()
		sq9_5 = db.Task.find({'sq9':'5'}).count()
		sq5 = sq1_5+sq2_5+sq3_5+sq4_5+sq5_5+sq6_5+sq7_5+sq8_5+sq9_5
				

		rest_total = rest1+rest2+rest3+rest4+rest5+rest6
		print (total)
		print(rest_total)
		print(total2)
		print(q1)
		print(q2)
		print(q3)
		print(q4)
		print(q5)
		print(sq1)
		print(sq2)
		print(sq3)
		print(sq4)
		print(sq5)
		
		cm = db.Task.find().limit(3)
		#return dumps(cm)
		return render_template("dash.html", total = total, total2 = total2, rest_total=rest_total, rest1=rest1, rest2=rest2, rest3=rest3, rest4=rest4,rest5=rest5, rest6=rest6,
			q1=q1, q2=q2, q3=q3, q4=q4, q5=q5, sq1=sq1,sq2=sq2, sq3=sq3, sq4=sq4, sq5=sq5, cm=cm)

	return redirect(url_for('sess'))
	
#total number of visitors "today"
@app.route('/get_total_today', methods = ['GET'])
def get_total_today():
	if 'user' in session:

		dov = datetime.datetime.now().strftime ("%Y-%m-%d")
		#dov = "2019-05-08"
		#total = db.Task.count()
		rest1 = db.Task.find({'rest':'1', 'dov':dov}).count()
		rest2 = db.Task.find({'rest':'2','dov':dov}).count()
		rest3 = db.Task.find({'rest':'3','dov':dov}).count()
		rest4 = db.Task.find({'rest':'4','dov':dov}).count()
		rest5 = db.Task.find({'rest':'5','dov':dov}).count()
		rest6 = db.Task.find({'rest':'6','dov':dov}).count()
		total2 = db.Task.find({'spa':'spa','dov':dov}).count()

		q1_1 = db.Task.find({'q1':'1','dov':dov}).count()
		q2_1 = db.Task.find({'q2':'1','dov':dov}).count()
		q3_1 = db.Task.find({'q3':'1','dov':dov}).count()
		q4_1 = db.Task.find({'q4':'1','dov':dov}).count()
		q5_1 = db.Task.find({'q5':'1','dov':dov}).count()
		q6_1 = db.Task.find({'q6':'1','dov':dov}).count()
		q7_1 = db.Task.find({'q7':'1','dov':dov}).count()
		q8_1 = db.Task.find({'q8':'1','dov':dov}).count()
		q9_1 = db.Task.find({'q9':'1','dov':dov}).count()
		q1 = q1_1+q2_1+q3_1+q4_1+q5_1+q6_1+q7_1+q8_1+q9_1

		q1_2 = db.Task.find({'q1':'2','dov':dov}).count()
		q2_2 = db.Task.find({'q2':'2','dov':dov}).count()
		q3_2 = db.Task.find({'q3':'2','dov':dov}).count()
		q4_2 = db.Task.find({'q4':'2','dov':dov}).count()
		q5_2 = db.Task.find({'q5':'2','dov':dov}).count()
		q6_2 = db.Task.find({'q6':'2','dov':dov}).count()
		q7_2 = db.Task.find({'q7':'2','dov':dov}).count()
		q8_2 = db.Task.find({'q8':'2','dov':dov}).count()
		q9_2 = db.Task.find({'q9':'2','dov':dov}).count()
		q2 = q1_2+q2_2+q3_2+q4_2+q5_2+q6_2+q7_2+q8_2+q9_2

		q1_3 = db.Task.find({'q1':'3','dov':dov}).count()
		q2_3 = db.Task.find({'q2':'3','dov':dov}).count()
		q3_3 = db.Task.find({'q3':'3','dov':dov}).count()
		q4_3 = db.Task.find({'q4':'3','dov':dov}).count()
		q5_3 = db.Task.find({'q5':'3','dov':dov}).count()
		q6_3 = db.Task.find({'q6':'3','dov':dov}).count()
		q7_3 = db.Task.find({'q7':'3','dov':dov}).count()
		q8_3 = db.Task.find({'q8':'3','dov':dov}).count()
		q9_3 = db.Task.find({'q9':'3','dov':dov}).count()
		q3 = q1_3+q2_3+q3_3+q4_3+q5_3+q6_3+q7_3+q8_3+q9_3

		q1_4 = db.Task.find({'q1':'4','dov':dov}).count()
		q2_4 = db.Task.find({'q2':'4','dov':dov}).count()
		q3_4 = db.Task.find({'q3':'4','dov':dov}).count()
		q4_4 = db.Task.find({'q4':'4','dov':dov}).count()
		q5_4 = db.Task.find({'q5':'4','dov':dov}).count()
		q6_4 = db.Task.find({'q6':'4','dov':dov}).count()
		q7_4 = db.Task.find({'q7':'4','dov':dov}).count()
		q8_4 = db.Task.find({'q8':'4','dov':dov}).count()
		q9_4 = db.Task.find({'q9':'4','dov':dov}).count()
		q4 = q1_4+q2_4+q3_4+q4_4+q5_4+q6_4+q7_4+q8_4+q9_4

		q1_5 = db.Task.find({'q1':'5','dov':dov}).count()
		q2_5 = db.Task.find({'q2':'5','dov':dov}).count()
		q3_5 = db.Task.find({'q3':'5','dov':dov}).count()
		q4_5 = db.Task.find({'q4':'5','dov':dov}).count()
		q5_5 = db.Task.find({'q5':'5','dov':dov}).count()
		q6_5 = db.Task.find({'q6':'5','dov':dov}).count()
		q7_5 = db.Task.find({'q7':'5','dov':dov}).count()
		q8_5 = db.Task.find({'q8':'5','dov':dov}).count()
		q9_5 = db.Task.find({'q9':'5','dov':dov}).count()
		q5 = q1_5+q2_5+q3_5+q4_5+q5_5+q6_5+q7_5+q8_5+q9_5
		
		sq1_1 = db.Task.find({'sq1':'1','dov':dov}).count()
		sq2_1 = db.Task.find({'sq2':'1','dov':dov}).count()
		sq3_1 = db.Task.find({'sq3':'1','dov':dov}).count()
		sq4_1 = db.Task.find({'sq4':'1','dov':dov}).count()
		sq5_1 = db.Task.find({'sq5':'1','dov':dov}).count()
		sq6_1 = db.Task.find({'sq6':'1','dov':dov}).count()
		sq7_1 = db.Task.find({'sq7':'1','dov':dov}).count()
		sq8_1 = db.Task.find({'sq8':'1','dov':dov}).count()
		sq9_1 = db.Task.find({'sq9':'1','dov':dov}).count()
		sq1 = sq1_1+sq2_1+sq3_1+sq4_1+sq5_1+sq6_1+sq7_1+sq8_1+sq9_1

		sq1_2 = db.Task.find({'sq1':'2','dov':dov}).count()
		sq2_2 = db.Task.find({'sq2':'2','dov':dov}).count()
		sq3_2 = db.Task.find({'sq3':'2','dov':dov}).count()
		sq4_2 = db.Task.find({'sq4':'2','dov':dov}).count()
		sq5_2 = db.Task.find({'sq5':'2','dov':dov}).count()
		sq6_2 = db.Task.find({'sq6':'2','dov':dov}).count()
		sq7_2 = db.Task.find({'sq7':'2','dov':dov}).count()
		sq8_2 = db.Task.find({'sq8':'2','dov':dov}).count()
		sq9_2 = db.Task.find({'sq9':'2','dov':dov}).count()
		sq2 = sq1_2+sq2_2+sq3_2+sq4_2+sq5_2+sq6_2+sq7_2+sq8_2+sq9_2

		sq1_3 = db.Task.find({'sq1':'3','dov':dov}).count()
		sq2_3 = db.Task.find({'sq2':'3','dov':dov}).count()
		sq3_3 = db.Task.find({'sq3':'3','dov':dov}).count()
		sq4_3 = db.Task.find({'sq4':'3','dov':dov}).count()
		sq5_3 = db.Task.find({'sq5':'3','dov':dov}).count()
		sq6_3 = db.Task.find({'sq6':'3','dov':dov}).count()
		sq7_3 = db.Task.find({'sq7':'3','dov':dov}).count()
		sq8_3 = db.Task.find({'sq8':'3','dov':dov}).count()
		sq9_3 = db.Task.find({'sq9':'3','dov':dov}).count()
		sq3 = sq1_3+sq2_3+sq3_3+sq4_3+sq5_3+sq6_3+sq7_3+sq8_3+sq9_3

		sq1_4 = db.Task.find({'sq1':'4','dov':dov}).count()
		sq2_4 = db.Task.find({'sq2':'4','dov':dov}).count()
		sq3_4 = db.Task.find({'sq3':'4','dov':dov}).count()
		sq4_4 = db.Task.find({'sq4':'4','dov':dov}).count()
		sq5_4 = db.Task.find({'sq5':'4','dov':dov}).count()
		sq6_4 = db.Task.find({'sq6':'4','dov':dov}).count()
		sq7_4 = db.Task.find({'sq7':'4','dov':dov}).count()
		sq8_4 = db.Task.find({'sq8':'4','dov':dov}).count()
		sq9_4 = db.Task.find({'sq9':'4','dov':dov}).count()
		sq4 = sq1_4+sq2_4+sq3_4+sq4_4+sq5_4+sq6_4+sq7_4+sq8_4+sq9_4

		sq1_5 = db.Task.find({'sq1':'5','dov':dov}).count()
		sq2_5 = db.Task.find({'sq2':'5','dov':dov}).count()
		sq3_5 = db.Task.find({'sq3':'5','dov':dov}).count()
		sq4_5 = db.Task.find({'sq4':'5','dov':dov}).count()
		sq5_5 = db.Task.find({'sq5':'5','dov':dov}).count()
		sq6_5 = db.Task.find({'sq6':'5','dov':dov}).count()
		sq7_5 = db.Task.find({'sq7':'5','dov':dov}).count()
		sq8_5 = db.Task.find({'sq8':'5','dov':dov}).count()
		sq9_5 = db.Task.find({'sq9':'5','dov':dov}).count()
		sq5 = sq1_5+sq2_5+sq3_5+sq4_5+sq5_5+sq6_5+sq7_5+sq8_5+sq9_5
				

		rest_total = rest1+rest2+rest3+rest4+rest5+rest6
		total = rest_total + sq1 + sq2 + sq3 + sq4 + sq5
		print (total)
		print(rest_total)
		print(total2)
		print(q1)
		print(q2)
		print(q3)
		print(q4)
		print(q5)
		print(sq1)
		print(sq2)
		print(sq3)
		print(sq4)
		print(sq5)
		
		cm = db.Task.find({'dov': dov}).limit(3)
		#return dumps(cm)
		return render_template("dash.html", total = total, total2 = total2, rest_total=rest_total, rest1=rest1, rest2=rest2, rest3=rest3, rest4=rest4,rest5=rest5, rest6=rest6,
			q1=q1, q2=q2, q3=q3, q4=q4, q5=q5, sq1=sq1,sq2=sq2, sq3=sq3, sq4=sq4, sq5=sq5, cm=cm)

	return redirect(url_for('sess'))

#total number of visitors "from-to"
@app.route('/get_total_tofrom', methods = ['GET','POST'])
def get_total_tofrom():
	if 'user' in session:

		startdate = request.form['startdate']
		enddate = request.form['enddate']
		#total = db.Task.count()
		rest1 = db.Task.find({'rest':'1', 'dov':{"$gte": startdate,"$lt":enddate}}).count()
		rest2 = db.Task.find({'rest':'2','dov':{"$gte": startdate,"$lt":enddate}}).count()
		rest3 = db.Task.find({'rest':'3','dov':{"$gte": startdate,"$lt":enddate}}).count()
		rest4 = db.Task.find({'rest':'4','dov':{"$gte": startdate,"$lt":enddate}}).count()
		rest5 = db.Task.find({'rest':'5','dov':{"$gte": startdate,"$lt":enddate}}).count()
		rest6 = db.Task.find({'rest':'6','dov':{"$gte": startdate,"$lt":enddate}}).count()
		total2 = db.Task.find({'spa':'spa','dov':{"$gte": startdate,"$lt":enddate}}).count()

		q1_1 = db.Task.find({'q1':'1','dov':{"$gte": startdate,"$lt":enddate}}).count()
		q2_1 = db.Task.find({'q2':'1','dov':{"$gte": startdate,"$lt":enddate}}).count()
		q3_1 = db.Task.find({'q3':'1','dov':{"$gte": startdate,"$lt":enddate}}).count()
		q4_1 = db.Task.find({'q4':'1','dov':{"$gte": startdate,"$lt":enddate}}).count()
		q5_1 = db.Task.find({'q5':'1','dov':{"$gte": startdate,"$lt":enddate}}).count()
		q6_1 = db.Task.find({'q6':'1','dov':{"$gte": startdate,"$lt":enddate}}).count()
		q7_1 = db.Task.find({'q7':'1','dov':{"$gte": startdate,"$lt":enddate}}).count()
		q8_1 = db.Task.find({'q8':'1','dov':{"$gte": startdate,"$lt":enddate}}).count()
		q9_1 = db.Task.find({'q9':'1','dov':{"$gte": startdate,"$lt":enddate}}).count()
		q1 = q1_1+q2_1+q3_1+q4_1+q5_1+q6_1+q7_1+q8_1+q9_1

		q1_2 = db.Task.find({'q1':'2','dov':{"$gte": startdate,"$lt":enddate}}).count()
		q2_2 = db.Task.find({'q2':'2','dov':{"$gte": startdate,"$lt":enddate}}).count()
		q3_2 = db.Task.find({'q3':'2','dov':{"$gte": startdate,"$lt":enddate}}).count()
		q4_2 = db.Task.find({'q4':'2','dov':{"$gte": startdate,"$lt":enddate}}).count()
		q5_2 = db.Task.find({'q5':'2','dov':{"$gte": startdate,"$lt":enddate}}).count()
		q6_2 = db.Task.find({'q6':'2','dov':{"$gte": startdate,"$lt":enddate}}).count()
		q7_2 = db.Task.find({'q7':'2','dov':{"$gte": startdate,"$lt":enddate}}).count()
		q8_2 = db.Task.find({'q8':'2','dov':{"$gte": startdate,"$lt":enddate}}).count()
		q9_2 = db.Task.find({'q9':'2','dov':{"$gte": startdate,"$lt":enddate}}).count()
		q2 = q1_2+q2_2+q3_2+q4_2+q5_2+q6_2+q7_2+q8_2+q9_2

		q1_3 = db.Task.find({'q1':'3','dov':{"$gte": startdate,"$lt":enddate}}).count()
		q2_3 = db.Task.find({'q2':'3','dov':{"$gte": startdate,"$lt":enddate}}).count()
		q3_3 = db.Task.find({'q3':'3','dov':{"$gte": startdate,"$lt":enddate}}).count()
		q4_3 = db.Task.find({'q4':'3','dov':{"$gte": startdate,"$lt":enddate}}).count()
		q5_3 = db.Task.find({'q5':'3','dov':{"$gte": startdate,"$lt":enddate}}).count()
		q6_3 = db.Task.find({'q6':'3','dov':{"$gte": startdate,"$lt":enddate}}).count()
		q7_3 = db.Task.find({'q7':'3','dov':{"$gte": startdate,"$lt":enddate}}).count()
		q8_3 = db.Task.find({'q8':'3','dov':{"$gte": startdate,"$lt":enddate}}).count()
		q9_3 = db.Task.find({'q9':'3','dov':{"$gte": startdate,"$lt":enddate}}).count()
		q3 = q1_3+q2_3+q3_3+q4_3+q5_3+q6_3+q7_3+q8_3+q9_3

		q1_4 = db.Task.find({'q1':'4','dov':{"$gte": startdate,"$lt":enddate}}).count()
		q2_4 = db.Task.find({'q2':'4','dov':{"$gte": startdate,"$lt":enddate}}).count()
		q3_4 = db.Task.find({'q3':'4','dov':{"$gte": startdate,"$lt":enddate}}).count()
		q4_4 = db.Task.find({'q4':'4','dov':{"$gte": startdate,"$lt":enddate}}).count()
		q5_4 = db.Task.find({'q5':'4','dov':{"$gte": startdate,"$lt":enddate}}).count()
		q6_4 = db.Task.find({'q6':'4','dov':{"$gte": startdate,"$lt":enddate}}).count()
		q7_4 = db.Task.find({'q7':'4','dov':{"$gte": startdate,"$lt":enddate}}).count()
		q8_4 = db.Task.find({'q8':'4','dov':{"$gte": startdate,"$lt":enddate}}).count()
		q9_4 = db.Task.find({'q9':'4','dov':{"$gte": startdate,"$lt":enddate}}).count()
		q4 = q1_4+q2_4+q3_4+q4_4+q5_4+q6_4+q7_4+q8_4+q9_4

		q1_5 = db.Task.find({'q1':'5','dov':{"$gte": startdate,"$lt":enddate}}).count()
		q2_5 = db.Task.find({'q2':'5','dov':{"$gte": startdate,"$lt":enddate}}).count()
		q3_5 = db.Task.find({'q3':'5','dov':{"$gte": startdate,"$lt":enddate}}).count()
		q4_5 = db.Task.find({'q4':'5','dov':{"$gte": startdate,"$lt":enddate}}).count()
		q5_5 = db.Task.find({'q5':'5','dov':{"$gte": startdate,"$lt":enddate}}).count()
		q6_5 = db.Task.find({'q6':'5','dov':{"$gte": startdate,"$lt":enddate}}).count()
		q7_5 = db.Task.find({'q7':'5','dov':{"$gte": startdate,"$lt":enddate}}).count()
		q8_5 = db.Task.find({'q8':'5','dov':{"$gte": startdate,"$lt":enddate}}).count()
		q9_5 = db.Task.find({'q9':'5','dov':{"$gte": startdate,"$lt":enddate}}).count()
		q5 = q1_5+q2_5+q3_5+q4_5+q5_5+q6_5+q7_5+q8_5+q9_5
		
		sq1_1 = db.Task.find({'sq1':'1','dov':{"$gte": startdate,"$lt":enddate}}).count()
		sq2_1 = db.Task.find({'sq2':'1','dov':{"$gte": startdate,"$lt":enddate}}).count()
		sq3_1 = db.Task.find({'sq3':'1','dov':{"$gte": startdate,"$lt":enddate}}).count()
		sq4_1 = db.Task.find({'sq4':'1','dov':{"$gte": startdate,"$lt":enddate}}).count()
		sq5_1 = db.Task.find({'sq5':'1','dov':{"$gte": startdate,"$lt":enddate}}).count()
		sq6_1 = db.Task.find({'sq6':'1','dov':{"$gte": startdate,"$lt":enddate}}).count()
		sq7_1 = db.Task.find({'sq7':'1','dov':{"$gte": startdate,"$lt":enddate}}).count()
		sq8_1 = db.Task.find({'sq8':'1','dov':{"$gte": startdate,"$lt":enddate}}).count()
		sq9_1 = db.Task.find({'sq9':'1','dov':{"$gte": startdate,"$lt":enddate}}).count()
		sq1 = sq1_1+sq2_1+sq3_1+sq4_1+sq5_1+sq6_1+sq7_1+sq8_1+sq9_1

		sq1_2 = db.Task.find({'sq1':'2','dov':{"$gte": startdate,"$lt":enddate}}).count()
		sq2_2 = db.Task.find({'sq2':'2','dov':{"$gte": startdate,"$lt":enddate}}).count()
		sq3_2 = db.Task.find({'sq3':'2','dov':{"$gte": startdate,"$lt":enddate}}).count()
		sq4_2 = db.Task.find({'sq4':'2','dov':{"$gte": startdate,"$lt":enddate}}).count()
		sq5_2 = db.Task.find({'sq5':'2','dov':{"$gte": startdate,"$lt":enddate}}).count()
		sq6_2 = db.Task.find({'sq6':'2','dov':{"$gte": startdate,"$lt":enddate}}).count()
		sq7_2 = db.Task.find({'sq7':'2','dov':{"$gte": startdate,"$lt":enddate}}).count()
		sq8_2 = db.Task.find({'sq8':'2','dov':{"$gte": startdate,"$lt":enddate}}).count()
		sq9_2 = db.Task.find({'sq9':'2','dov':{"$gte": startdate,"$lt":enddate}}).count()
		sq2 = sq1_2+sq2_2+sq3_2+sq4_2+sq5_2+sq6_2+sq7_2+sq8_2+sq9_2

		sq1_3 = db.Task.find({'sq1':'3','dov':{"$gte": startdate,"$lt":enddate}}).count()
		sq2_3 = db.Task.find({'sq2':'3','dov':{"$gte": startdate,"$lt":enddate}}).count()
		sq3_3 = db.Task.find({'sq3':'3','dov':{"$gte": startdate,"$lt":enddate}}).count()
		sq4_3 = db.Task.find({'sq4':'3','dov':{"$gte": startdate,"$lt":enddate}}).count()
		sq5_3 = db.Task.find({'sq5':'3','dov':{"$gte": startdate,"$lt":enddate}}).count()
		sq6_3 = db.Task.find({'sq6':'3','dov':{"$gte": startdate,"$lt":enddate}}).count()
		sq7_3 = db.Task.find({'sq7':'3','dov':{"$gte": startdate,"$lt":enddate}}).count()
		sq8_3 = db.Task.find({'sq8':'3','dov':{"$gte": startdate,"$lt":enddate}}).count()
		sq9_3 = db.Task.find({'sq9':'3','dov':{"$gte": startdate,"$lt":enddate}}).count()
		sq3 = sq1_3+sq2_3+sq3_3+sq4_3+sq5_3+sq6_3+sq7_3+sq8_3+sq9_3

		sq1_4 = db.Task.find({'sq1':'4','dov':{"$gte": startdate,"$lt":enddate}}).count()
		sq2_4 = db.Task.find({'sq2':'4','dov':{"$gte": startdate,"$lt":enddate}}).count()
		sq3_4 = db.Task.find({'sq3':'4','dov':{"$gte": startdate,"$lt":enddate}}).count()
		sq4_4 = db.Task.find({'sq4':'4','dov':{"$gte": startdate,"$lt":enddate}}).count()
		sq5_4 = db.Task.find({'sq5':'4','dov':{"$gte": startdate,"$lt":enddate}}).count()
		sq6_4 = db.Task.find({'sq6':'4','dov':{"$gte": startdate,"$lt":enddate}}).count()
		sq7_4 = db.Task.find({'sq7':'4','dov':{"$gte": startdate,"$lt":enddate}}).count()
		sq8_4 = db.Task.find({'sq8':'4','dov':{"$gte": startdate,"$lt":enddate}}).count()
		sq9_4 = db.Task.find({'sq9':'4','dov':{"$gte": startdate,"$lt":enddate}}).count()
		sq4 = sq1_4+sq2_4+sq3_4+sq4_4+sq5_4+sq6_4+sq7_4+sq8_4+sq9_4

		sq1_5 = db.Task.find({'sq1':'5','dov':{"$gte": startdate,"$lt":enddate}}).count()
		sq2_5 = db.Task.find({'sq2':'5','dov':{"$gte": startdate,"$lt":enddate}}).count()
		sq3_5 = db.Task.find({'sq3':'5','dov':{"$gte": startdate,"$lt":enddate}}).count()
		sq4_5 = db.Task.find({'sq4':'5','dov':{"$gte": startdate,"$lt":enddate}}).count()
		sq5_5 = db.Task.find({'sq5':'5','dov':{"$gte": startdate,"$lt":enddate}}).count()
		sq6_5 = db.Task.find({'sq6':'5','dov':{"$gte": startdate,"$lt":enddate}}).count()
		sq7_5 = db.Task.find({'sq7':'5','dov':{"$gte": startdate,"$lt":enddate}}).count()
		sq8_5 = db.Task.find({'sq8':'5','dov':{"$gte": startdate,"$lt":enddate}}).count()
		sq9_5 = db.Task.find({'sq9':'5','dov':{"$gte": startdate,"$lt":enddate}}).count()
		sq5 = sq1_5+sq2_5+sq3_5+sq4_5+sq5_5+sq6_5+sq7_5+sq8_5+sq9_5
				

		rest_total = rest1+rest2+rest3+rest4+rest5+rest6
		total = rest_total + sq1 + sq2 + sq3 + sq4 + sq5
		print (total)
		print(rest_total)
		print(total2)
		print(q1)
		print(q2)
		print(q3)
		print(q4)
		print(q5)
		print(sq1)
		print(sq2)
		print(sq3)
		print(sq4)
		print(sq5)
		
		cm = db.Task.find({'dov':{"$gte": startdate,"$lt":enddate}}).limit(3)
		#return dumps(cm)
		return render_template("dash.html", total = total, total2 = total2, rest_total=rest_total, rest1=rest1, rest2=rest2, rest3=rest3, rest4=rest4,rest5=rest5, rest6=rest6,
			q1=q1, q2=q2, q3=q3, q4=q4, q5=q5, sq1=sq1,sq2=sq2, sq3=sq3, sq4=sq4, sq5=sq5, cm=cm)

	return redirect(url_for('sess'))

	#total number of visitors "from-to"
@app.route('/get_total_date', methods = ['GET','POST'])
def get_total_date():
	if 'user' in session:

		startdate = request.form['startdate']
		#total = db.Task.count()
		rest1 = db.Task.find({'rest':'1', 'dov':startdate}).count()
		rest2 = db.Task.find({'rest':'2','dov':startdate}).count()
		rest3 = db.Task.find({'rest':'3','dov':startdate}).count()
		rest4 = db.Task.find({'rest':'4','dov':startdate}).count()
		rest5 = db.Task.find({'rest':'5','dov':startdate}).count()
		rest6 = db.Task.find({'rest':'6','dov':startdate}).count()
		total2 = db.Task.find({'spa':'spa','dov':startdate}).count()

		q1_1 = db.Task.find({'q1':'1','dov':startdate}).count()
		q2_1 = db.Task.find({'q2':'1','dov':startdate}).count()
		q3_1 = db.Task.find({'q3':'1','dov':startdate}).count()
		q4_1 = db.Task.find({'q4':'1','dov':startdate}).count()
		q5_1 = db.Task.find({'q5':'1','dov':startdate}).count()
		q6_1 = db.Task.find({'q6':'1','dov':startdate}).count()
		q7_1 = db.Task.find({'q7':'1','dov':startdate}).count()
		q8_1 = db.Task.find({'q8':'1','dov':startdate}).count()
		q9_1 = db.Task.find({'q9':'1','dov':startdate}).count()
		q1 = q1_1+q2_1+q3_1+q4_1+q5_1+q6_1+q7_1+q8_1+q9_1

		q1_2 = db.Task.find({'q1':'2','dov':startdate}).count()
		q2_2 = db.Task.find({'q2':'2','dov':startdate}).count()
		q3_2 = db.Task.find({'q3':'2','dov':startdate}).count()
		q4_2 = db.Task.find({'q4':'2','dov':startdate}).count()
		q5_2 = db.Task.find({'q5':'2','dov':startdate}).count()
		q6_2 = db.Task.find({'q6':'2','dov':startdate}).count()
		q7_2 = db.Task.find({'q7':'2','dov':startdate}).count()
		q8_2 = db.Task.find({'q8':'2','dov':startdate}).count()
		q9_2 = db.Task.find({'q9':'2','dov':startdate}).count()
		q2 = q1_2+q2_2+q3_2+q4_2+q5_2+q6_2+q7_2+q8_2+q9_2

		q1_3 = db.Task.find({'q1':'3','dov':startdate}).count()
		q2_3 = db.Task.find({'q2':'3','dov':startdate}).count()
		q3_3 = db.Task.find({'q3':'3','dov':startdate}).count()
		q4_3 = db.Task.find({'q4':'3','dov':startdate}).count()
		q5_3 = db.Task.find({'q5':'3','dov':startdate}).count()
		q6_3 = db.Task.find({'q6':'3','dov':startdate}).count()
		q7_3 = db.Task.find({'q7':'3','dov':startdate}).count()
		q8_3 = db.Task.find({'q8':'3','dov':startdate}).count()
		q9_3 = db.Task.find({'q9':'3','dov':startdate}).count()
		q3 = q1_3+q2_3+q3_3+q4_3+q5_3+q6_3+q7_3+q8_3+q9_3

		q1_4 = db.Task.find({'q1':'4','dov':startdate}).count()
		q2_4 = db.Task.find({'q2':'4','dov':startdate}).count()
		q3_4 = db.Task.find({'q3':'4','dov':startdate}).count()
		q4_4 = db.Task.find({'q4':'4','dov':startdate}).count()
		q5_4 = db.Task.find({'q5':'4','dov':startdate}).count()
		q6_4 = db.Task.find({'q6':'4','dov':startdate}).count()
		q7_4 = db.Task.find({'q7':'4','dov':startdate}).count()
		q8_4 = db.Task.find({'q8':'4','dov':startdate}).count()
		q9_4 = db.Task.find({'q9':'4','dov':startdate}).count()
		q4 = q1_4+q2_4+q3_4+q4_4+q5_4+q6_4+q7_4+q8_4+q9_4

		q1_5 = db.Task.find({'q1':'5','dov':startdate}).count()
		q2_5 = db.Task.find({'q2':'5','dov':startdate}).count()
		q3_5 = db.Task.find({'q3':'5','dov':startdate}).count()
		q4_5 = db.Task.find({'q4':'5','dov':startdate}).count()
		q5_5 = db.Task.find({'q5':'5','dov':startdate}).count()
		q6_5 = db.Task.find({'q6':'5','dov':startdate}).count()
		q7_5 = db.Task.find({'q7':'5','dov':startdate}).count()
		q8_5 = db.Task.find({'q8':'5','dov':startdate}).count()
		q9_5 = db.Task.find({'q9':'5','dov':startdate}).count()
		q5 = q1_5+q2_5+q3_5+q4_5+q5_5+q6_5+q7_5+q8_5+q9_5
		
		sq1_1 = db.Task.find({'sq1':'1','dov':startdate}).count()
		sq2_1 = db.Task.find({'sq2':'1','dov':startdate}).count()
		sq3_1 = db.Task.find({'sq3':'1','dov':startdate}).count()
		sq4_1 = db.Task.find({'sq4':'1','dov':startdate}).count()
		sq5_1 = db.Task.find({'sq5':'1','dov':startdate}).count()
		sq6_1 = db.Task.find({'sq6':'1','dov':startdate}).count()
		sq7_1 = db.Task.find({'sq7':'1','dov':startdate}).count()
		sq8_1 = db.Task.find({'sq8':'1','dov':startdate}).count()
		sq9_1 = db.Task.find({'sq9':'1','dov':startdate}).count()
		sq1 = sq1_1+sq2_1+sq3_1+sq4_1+sq5_1+sq6_1+sq7_1+sq8_1+sq9_1

		sq1_2 = db.Task.find({'sq1':'2','dov':startdate}).count()
		sq2_2 = db.Task.find({'sq2':'2','dov':startdate}).count()
		sq3_2 = db.Task.find({'sq3':'2','dov':startdate}).count()
		sq4_2 = db.Task.find({'sq4':'2','dov':startdate}).count()
		sq5_2 = db.Task.find({'sq5':'2','dov':startdate}).count()
		sq6_2 = db.Task.find({'sq6':'2','dov':startdate}).count()
		sq7_2 = db.Task.find({'sq7':'2','dov':startdate}).count()
		sq8_2 = db.Task.find({'sq8':'2','dov':startdate}).count()
		sq9_2 = db.Task.find({'sq9':'2','dov':startdate}).count()
		sq2 = sq1_2+sq2_2+sq3_2+sq4_2+sq5_2+sq6_2+sq7_2+sq8_2+sq9_2

		sq1_3 = db.Task.find({'sq1':'3','dov':startdate}).count()
		sq2_3 = db.Task.find({'sq2':'3','dov':startdate}).count()
		sq3_3 = db.Task.find({'sq3':'3','dov':startdate}).count()
		sq4_3 = db.Task.find({'sq4':'3','dov':startdate}).count()
		sq5_3 = db.Task.find({'sq5':'3','dov':startdate}).count()
		sq6_3 = db.Task.find({'sq6':'3','dov':startdate}).count()
		sq7_3 = db.Task.find({'sq7':'3','dov':startdate}).count()
		sq8_3 = db.Task.find({'sq8':'3','dov':startdate}).count()
		sq9_3 = db.Task.find({'sq9':'3','dov':startdate}).count()
		sq3 = sq1_3+sq2_3+sq3_3+sq4_3+sq5_3+sq6_3+sq7_3+sq8_3+sq9_3

		sq1_4 = db.Task.find({'sq1':'4','dov':startdate}).count()
		sq2_4 = db.Task.find({'sq2':'4','dov':startdate}).count()
		sq3_4 = db.Task.find({'sq3':'4','dov':startdate}).count()
		sq4_4 = db.Task.find({'sq4':'4','dov':startdate}).count()
		sq5_4 = db.Task.find({'sq5':'4','dov':startdate}).count()
		sq6_4 = db.Task.find({'sq6':'4','dov':startdate}).count()
		sq7_4 = db.Task.find({'sq7':'4','dov':startdate}).count()
		sq8_4 = db.Task.find({'sq8':'4','dov':startdate}).count()
		sq9_4 = db.Task.find({'sq9':'4','dov':startdate}).count()
		sq4 = sq1_4+sq2_4+sq3_4+sq4_4+sq5_4+sq6_4+sq7_4+sq8_4+sq9_4

		sq1_5 = db.Task.find({'sq1':'5','dov':startdate}).count()
		sq2_5 = db.Task.find({'sq2':'5','dov':startdate}).count()
		sq3_5 = db.Task.find({'sq3':'5','dov':startdate}).count()
		sq4_5 = db.Task.find({'sq4':'5','dov':startdate}).count()
		sq5_5 = db.Task.find({'sq5':'5','dov':startdate}).count()
		sq6_5 = db.Task.find({'sq6':'5','dov':startdate}).count()
		sq7_5 = db.Task.find({'sq7':'5','dov':startdate}).count()
		sq8_5 = db.Task.find({'sq8':'5','dov':startdate}).count()
		sq9_5 = db.Task.find({'sq9':'5','dov':startdate}).count()
		sq5 = sq1_5+sq2_5+sq3_5+sq4_5+sq5_5+sq6_5+sq7_5+sq8_5+sq9_5
				

		rest_total = rest1+rest2+rest3+rest4+rest5+rest6
		total = rest_total + sq1 + sq2 + sq3 + sq4 + sq5
		print (total)
		print(rest_total)
		print(total2)
		print(q1)
		print(q2)
		print(q3)
		print(q4)
		print(q5)
		print(sq1)
		print(sq2)
		print(sq3)
		print(sq4)
		print(sq5)
		
		cm = db.Task.find({'dov': startdate}).limit(3)
		#return dumps(cm)
		return render_template("dash.html", total = total, total2 = total2, rest_total=rest_total, rest1=rest1, rest2=rest2, rest3=rest3, rest4=rest4,rest5=rest5, rest6=rest6,
			q1=q1, q2=q2, q3=q3, q4=q4, q5=q5, sq1=sq1,sq2=sq2, sq3=sq3, sq4=sq4, sq5=sq5, cm = cm)

	return redirect(url_for('sess'))


#get number of visitors in each restaurant
@app.route('/get_rest/<rest>', methods = ['GET'])
def get_rest(rest):
	if 'user' in session:
		total = db.Task.find({'rest':rest}).count()
		return dumps(total)
		#return render_template("display.html", tasks = tasks)
	return redirect(url_for('sess'))


#delete all the data
@app.route("/remove", methods=['GET', 'POST'])
def remove():
    db.Task.drop()
    return dumps({'message' : 'Removed successfully'})

#first page for feedabck
@app.route('/reports')
def reports():
   return render_template("reports.html")

if __name__ == '__main__':
   app.run(debug = True)