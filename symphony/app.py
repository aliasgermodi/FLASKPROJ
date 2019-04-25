from flask import Flask, url_for, redirect, render_template, request, abort, session
from flask import Flask, render_template, render_template, redirect, url_for, request,g
from pymongo import MongoClient
import json
from flask_pymongo import PyMongo
from flask import jsonify
from bson.json_util import dumps
import os


client = MongoClient('localhost:27017')
db = client.TaskDB
app = Flask(__name__)
app.secret_key = os.urandom(24)

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
		return redirect(url_for('get_total'))

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


@app.route('/ser_en')
def services_en():
   return render_template("serviceEN.html")

@app.route('/ser_ar')
def services_ar():
	   return render_template("serviceAR.html")


#Restaurant 1   

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
		rest = "1"
		name = request.form['NAME']
		phone = request.form['PHNO']
		email = request.form['EMAIL']
		dob = request.form['DOB']
		ad = request.form['AD']
		dov = request.form['DOV']
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
		db.Task.insert({"rest":rest, "name": name, "phone": phone, "email":email, "dob":dob, 
			"ad": ad, "dov": dov, "us":us, "p":p, "meal": meal, "q1": q1, "q2":q2, "q3":q3, "q4": q4, "q5":q5, "q6":q6,
			"q7": q7, "q8":q8, "q9":q9, "q10":q10, "rating":rating,"fr":fr, "cm":cm })
		return render_template("ty_en.html")
		#return render_template("service.html", fn = first_name, ln = last_name, gender = gender)

	except Exception, e:
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
		rest = "1"
		name = request.form['NAME']
		phone = request.form['PHNO']
		email = request.form['EMAIL']
		dob = request.form['DOB']
		ad = request.form['AD']
		dov = request.form['DOV']
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
		db.Task.insert({"rest":rest, "name": name, "phone": phone, "email":email, "dob":dob, 
			"ad": ad, "dov": dov, "us":us, "p":p, "meal": meal, "q1": q1, "q2":q2, "q3":q3, "q4": q4, "q5":q5, "q6":q6,
			"q7": q7, "q8":q8, "q9":q9, "q10":q10, "rating":rating,"fr":fr, "cm":cm })
		return render_template("ty_ar.html")
		#return render_template("service.html", fn = first_name, ln = last_name, gender = gender)

	except Exception, e:
		return dumps({'error' : str(e)})

#Restaurant 2

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
		ad = request.form['AD']
		dov = request.form['DOV']
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
		db.Task.insert({"rest":rest, "name": name, "phone": phone, "email":email, "dob":dob, 
			"ad": ad, "dov": dov, "us":us, "p":p, "meal": meal, "q1": q1, "q2":q2, "q3":q3, "q4": q4, "q5":q5, "q6":q6,
			"q7": q7, "q8":q8, "q9":q9, "q10":q10, "rating":rating,"fr":fr, "cm":cm })
		return render_template("ty_en.html")
		#return render_template("service.html", fn = first_name, ln = last_name, gender = gender)

	except Exception, e:
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
		ad = request.form['AD']
		dov = request.form['DOV']
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
		db.Task.insert({"rest":rest, "name": name, "phone": phone, "email":email, "dob":dob, 
			"ad": ad, "dov": dov, "us":us, "p":p, "meal": meal, "q1": q1, "q2":q2, "q3":q3, "q4": q4, "q5":q5, "q6":q6,
			"q7": q7, "q8":q8, "q9":q9, "q10":q10, "rating":rating,"fr":fr, "cm":cm })
		return render_template("ty_ar.html")
		#return render_template("service.html", fn = first_name, ln = last_name, gender = gender)

	except Exception, e:
		return dumps({'error' : str(e)})

#Restaurant 3

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
		ad = request.form['AD']
		dov = request.form['DOV']
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
		db.Task.insert({"rest":rest, "name": name, "phone": phone, "email":email, "dob":dob, 
			"ad": ad, "dov": dov, "us":us, "p":p, "meal": meal, "q1": q1, "q2":q2, "q3":q3, "q4": q4, "q5":q5, "q6":q6,
			"q7": q7, "q8":q8, "q9":q9, "q10":q10, "rating":rating,"fr":fr, "cm":cm })
		return render_template("ty_en.html")
		#return render_template("service.html", fn = first_name, ln = last_name, gender = gender)

	except Exception, e:
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
		ad = request.form['AD']
		dov = request.form['DOV']
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
		db.Task.insert({"rest":rest, "name": name, "phone": phone, "email":email, "dob":dob, 
			"ad": ad, "dov": dov, "us":us, "p":p, "meal": meal, "q1": q1, "q2":q2, "q3":q3, "q4": q4, "q5":q5, "q6":q6,
			"q7": q7, "q8":q8, "q9":q9, "q10":q10, "rating":rating,"fr":fr, "cm":cm })
		return render_template("ty_ar.html")
		#return render_template("service.html", fn = first_name, ln = last_name, gender = gender)

	except Exception, e:
		return dumps({'error' : str(e)})


#Restaurant 4

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
		ad = request.form['AD']
		dov = request.form['DOV']
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
		db.Task.insert({"rest":rest, "name": name, "phone": phone, "email":email, "dob":dob, 
			"ad": ad, "dov": dov, "us":us, "p":p, "meal": meal, "q1": q1, "q2":q2, "q3":q3, "q4": q4, "q5":q5, "q6":q6,
			"q7": q7, "q8":q8, "q9":q9, "q10":q10, "rating":rating,"fr":fr, "cm":cm })
		return render_template("ty_en.html")
		#return render_template("service.html", fn = first_name, ln = last_name, gender = gender)

	except Exception, e:
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
		ad = request.form['AD']
		dov = request.form['DOV']
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
		db.Task.insert({"rest":rest, "name": name, "phone": phone, "email":email, "dob":dob, 
			"ad": ad, "dov": dov, "us":us, "p":p, "meal": meal, "q1": q1, "q2":q2, "q3":q3, "q4": q4, "q5":q5, "q6":q6,
			"q7": q7, "q8":q8, "q9":q9, "q10":q10, "rating":rating,"fr":fr, "cm":cm })
		return render_template("ty_ar.html")
		#return render_template("service.html", fn = first_name, ln = last_name, gender = gender)

	except Exception, e:
		return dumps({'error' : str(e)})


#Restaurant 5
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
		ad = request.form['AD']
		dov = request.form['DOV']
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
		db.Task.insert({"rest":rest, "name": name, "phone": phone, "email":email, "dob":dob, 
			"ad": ad, "dov": dov, "us":us, "p":p, "meal": meal, "q1": q1, "q2":q2, "q3":q3, "q4": q4, "q5":q5, "q6":q6,
			"q7": q7, "q8":q8, "q9":q9, "q10":q10, "rating":rating,"fr":fr, "cm":cm })
		return render_template("ty_en.html")
		#return render_template("service.html", fn = first_name, ln = last_name, gender = gender)

	except Exception, e:
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
		ad = request.form['AD']
		dov = request.form['DOV']
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
		db.Task.insert({"rest":rest, "name": name, "phone": phone, "email":email, "dob":dob, 
			"ad": ad, "dov": dov, "us":us, "p":p, "meal": meal, "q1": q1, "q2":q2, "q3":q3, "q4": q4, "q5":q5, "q6":q6,
			"q7": q7, "q8":q8, "q9":q9, "q10":q10, "rating":rating,"fr":fr, "cm":cm })
		return render_template("ty_ar.html")
		#return render_template("service.html", fn = first_name, ln = last_name, gender = gender)

	except Exception, e:
		return dumps({'error' : str(e)})

#Restaurant 6
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
		ad = request.form['AD']
		dov = request.form['DOV']
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
		db.Task.insert({"rest":rest, "name": name, "phone": phone, "email":email, "dob":dob, 
			"ad": ad, "dov": dov, "us":us, "p":p, "meal": meal, "q1": q1, "q2":q2, "q3":q3, "q4": q4, "q5":q5, "q6":q6,
			"q7": q7, "q8":q8, "q9":q9, "q10":q10, "rating":rating,"fr":fr, "cm":cm })
		return render_template("ty_en.html")
		#return render_template("service.html", fn = first_name, ln = last_name, gender = gender)

	except Exception, e:
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
		ad = request.form['AD']
		dov = request.form['DOV']
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
		db.Task.insert({"rest":rest, "name": name, "phone": phone, "email":email, "dob":dob, 
			"ad": ad, "dov": dov, "us":us, "p":p, "meal": meal, "q1": q1, "q2":q2, "q3":q3, "q4": q4, "q5":q5, "q6":q6,
			"q7": q7, "q8":q8, "q9":q9, "q10":q10, "rating":rating,"fr":fr, "cm":cm })
		return render_template("ty_ar.html")
		#return render_template("service.html", fn = first_name, ln = last_name, gender = gender)

	except Exception, e:
		return dumps({'error' : str(e)})


#SPA english
@app.route('/spa_en')
def spa_en():
   return render_template("spa_form_en.html")

@app.route('/spa_ar')
def spa_ar():
   return render_template("spa_form_ar.html")

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
		ad = request.form['AD']
		dov = request.form['DOV']
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
		db.Task.insert({"spa":spa, "sname": name, "sphone": phone, "email":email, "dob":dob, 
			"ad": ad, "dov": dov, "us":us, "sp":p, "sq1": q1, "sq2":q2, "sq3":q3, "sq4": q4, "sq5":q5, "sq6":q6,
			"sq7": q7, "sq8":q8, "sq9":q9, "sq10":q10, "sq11":q11, "name_spa":name_spa, "scm":cm })
		return render_template("ty_en.html")
		#return render_template("service.html", fn = first_name, ln = last_name, gender = gender)

	except Exception, e:
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
		ad = request.form['AD']
		dov = request.form['DOV']
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
		db.Task.insert({"spa":spa, "sname": name, "sphone": phone, "email":email, "dob":dob, 
			"ad": ad, "dov": dov, "us":us, "sp":p, "sq1": q1, "sq2":q2, "sq3":q3, "sq4": q4, "sq5":q5, "sq6":q6,
			"sq7": q7, "sq8":q8, "sq9":q9, "sq10":q10, "sq11":q11, "name_spa":name_spa, "scm":cm })
		return render_template("ty_ar.html")
		#return render_template("service.html", fn = first_name, ln = last_name, gender = gender)

	except Exception, e:
		return dumps({'error' : str(e)})



@app.route('/next', methods = ['POST'])
def move_forward():
    #Moving forward code
    return render_template("service.html")

@app.route('/users', methods = ['GET'])
def get_users():
    #Moving forward code
    return render_template("users.html")

#get all the users json
@app.route('/get_all', methods = ['GET'])
def get_all():
	try:
		tasks = db.Task.find()
		#return render_template("users_rest.html", tasks = tasks)
		return dumps(tasks)
	except Exception, e:
		return dumps({'error' : str(e)})

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

#get all the users for spa
@app.route('/get_all_spa', methods = ['GET'])
def get_all_spa():
	if 'user' in session:
		tasks = db.Task.find({'spa':'spa'})
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
		single = db.Task.find({'name':name})
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


#Data of each rating by each visitor per restaurant
@app.route('/get_rating_<rest>', methods = ['GET'])
def get_rest_rating(rest):
	if 'user' in session:
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
		
		return render_template("rest_dash.html",no = rest , single = single, q1_1=q1_1, q1_2=q1_2, q1_3=q1_3,q1_4=q1_4,q1_5=q1_5,q2_1=q2_1, q2_2=q2_2, q2_3=q2_3,q2_4=q2_4,q2_5=q2_5,
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
		sq1_1 = db.Task.find({'spa':spa,'q1':'1'}).count()
		sq1_2 = db.Task.find({'spa':spa,'q1':'2'}).count()
		sq1_3 = db.Task.find({'spa':spa,'q1':'3'}).count()
		sq1_4 = db.Task.find({'spa':spa,'q1':'4'}).count()
		sq1_5 = db.Task.find({'spa':spa,'q1':'5'}).count()
		sq2_1 = db.Task.find({'spa':spa,'q2':'1'}).count()
		sq2_2 = db.Task.find({'spa':spa,'q2':'2'}).count()
		sq2_3 = db.Task.find({'spa':spa,'q2':'3'}).count()
		sq2_4 = db.Task.find({'spa':spa,'q2':'4'}).count()
		sq2_5 = db.Task.find({'spa':spa,'q2':'5'}).count()
		sq3_1 = db.Task.find({'spa':spa,'q3':'1'}).count()
		sq3_2 = db.Task.find({'spa':spa,'q3':'2'}).count()
		sq3_3 = db.Task.find({'spa':spa,'q3':'3'}).count()
		sq3_4 = db.Task.find({'spa':spa,'q3':'4'}).count()
		sq3_5 = db.Task.find({'spa':spa,'q3':'5'}).count()
		sq4_1 = db.Task.find({'spa':spa,'q4':'1'}).count()
		sq4_2 = db.Task.find({'spa':spa,'q4':'2'}).count()
		sq4_3 = db.Task.find({'spa':spa,'q4':'3'}).count()
		sq4_4 = db.Task.find({'spa':spa,'q4':'4'}).count()
		sq4_5 = db.Task.find({'spa':spa,'q4':'5'}).count()
		sq5_1 = db.Task.find({'spa':spa,'q5':'1'}).count()
		sq5_2 = db.Task.find({'spa':spa,'q5':'2'}).count()
		sq5_3 = db.Task.find({'spa':spa,'q5':'3'}).count()
		sq5_4 = db.Task.find({'spa':spa,'q5':'4'}).count()
		sq5_5 = db.Task.find({'spa':spa,'q5':'5'}).count()
		sq6_1 = db.Task.find({'spa':spa,'q6':'1'}).count()
		sq6_2 = db.Task.find({'spa':spa,'q6':'2'}).count()
		sq6_3 = db.Task.find({'spa':spa,'q6':'3'}).count()
		sq6_4 = db.Task.find({'spa':spa,'q6':'4'}).count()
		sq6_5 = db.Task.find({'spa':spa,'q6':'5'}).count()
		sq7_1 = db.Task.find({'spa':spa,'q7':'1'}).count()
		sq7_2 = db.Task.find({'spa':spa,'q7':'2'}).count()
		sq7_3 = db.Task.find({'spa':spa,'q7':'3'}).count()
		sq7_4 = db.Task.find({'spa':spa,'q7':'4'}).count()
		sq7_5 = db.Task.find({'spa':spa,'q7':'5'}).count()
		sq8_1 = db.Task.find({'spa':spa,'q8':'1'}).count()
		sq8_2 = db.Task.find({'spa':spa,'q8':'2'}).count()
		sq8_3 = db.Task.find({'spa':spa,'q8':'3'}).count()
		sq8_4 = db.Task.find({'spa':spa,'q8':'4'}).count()
		sq8_5 = db.Task.find({'spa':spa,'q8':'5'}).count()
		sq9_1 = db.Task.find({'spa':spa,'q9':'1'}).count()
		sq9_2 = db.Task.find({'spa':spa,'q9':'2'}).count()
		sq9_3 = db.Task.find({'spa':spa,'q9':'3'}).count()
		sq9_4 = db.Task.find({'spa':spa,'q9':'4'}).count()
		sq9_5 = db.Task.find({'spa':spa,'q9':'5'}).count()
		
		return render_template("spa_dash.html",single = single, sq1_1=sq1_1, sq1_2=sq1_2, sq1_3=sq1_3,sq1_4=sq1_4,sq1_5=sq1_5,sq2_1=sq2_1, sq2_2=sq2_2, sq2_3=sq2_3,sq2_4=sq2_4,sq2_5=sq2_5,
		sq3_1=sq3_1, sq3_2=sq3_2, sq3_3=sq3_3,sq3_4=sq3_4,sq3_5=sq3_5,sq4_1=sq4_1, sq4_2=sq4_2, sq4_3=sq4_3,sq4_4=sq4_4,sq4_5=sq4_5,sq5_1=sq5_1, sq5_2=sq5_2, sq5_3=sq5_3,sq5_4=sq5_4,sq5_5=sq5_5,
		sq6_1=sq6_1, sq6_2=sq6_2, sq6_3=sq6_3,sq6_4=sq6_4,sq6_5=sq6_5,sq7_1=sq7_1, sq7_2=sq7_2, sq7_3=sq7_3,sq7_4=sq7_4,sq7_5=sq7_5,sq8_1=sq8_1, sq8_2=sq8_2, sq8_3=sq8_3,sq8_4=sq8_4,sq8_5=sq8_5,
		sq9_1=sq9_1, sq9_2=sq9_2, sq9_3=sq9_3,sq9_4=sq9_4,sq9_5=sq9_5,)
		#return render_template("display.html", tasks = tasks)
	return redirect(url_for('sess'))


#total number of visitors
@app.route('/get_total', methods = ['GET'])
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

if __name__ == '__main__':
   app.run(debug = True)