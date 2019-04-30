from flask import Flask
from flask import request
from pymongo import MongoClient
from bson.json_util import dumps
import json
import datetime
import time
client = MongoClient('localhost:27017')
db = client.TaskDB

app = Flask(__name__)

@app.route('/')
def index():
	return dumps('Hello')

#Create Plan
@app.route('/api/plan', methods = ['POST'])
def plan_create():
	try:
		data = json.loads(request.data)
		ids = data['id']
		name = data['name']
		amount = data['amount']
		currency = data['currency']
		status = db.plan.insert({
                "id" : ids,
                "name" : name,
                "price":{"amount":amount,"currency":currency}
                #"time": user_time,
                #"ls": last_seen,
            })
		return dumps({'message' : 'SUCCESS'})
	except Exception, e:
		return dumps({'error' : str(e)})

#Create feature
@app.route('/api/feature', methods = ['POST'])
def feature_create():
	try:
		data = json.loads(request.data)
		ids = data['id']
		namef = data['namef']
		limit_amount = data['amount']
		limit_unit = data['unit']
		limit_balance = data['balance']
		extra_charge_amount = data['amounte']
		extra_charge_currency = data['currency']
		extra_charge_unit = data['unite']

		status = db.feature.insert({
                "feature":{"id" : ids,
                "name" : name,
                "limit":{"amount":limit_amount,"unit":limit_unit,"balance":limit_balance,
                "extraCharge":{"amounte":extra_charge_amount,"currency":extra_charge_currency,"unite":extra_charge_unit}}}
               
                #"time": user_time,
                #"ls": last_seen,
            })
		return dumps({'message' : 'SUCCESS'})
	except Exception, e:
		return dumps({'error' : str(e)})

#Create user
@app.route('/api/user', methods = ['POST'])
def user_create():
	try:
		data = json.loads(request.data)
		name = data['name_id']
		status = db.user.insert({
                "name_id" : name
                #"time": user_time,
                #"ls": last_seen,
            })
		return dumps({'message' : 'SUCCESS'})
	except Exception, e:
		return dumps({'error' : str(e)})

@app.route("/api/plan/list_all", methods = ['GET'])
def get_all_plan():#customer_id,**kwargs):
	try:
		get = db.plan.find()
		return dumps(get)
	except Exception, e:
		return dumps({'error' : str(e)})

@app.route("/api/user/list_all", methods = ['GET'])
def get_all_user():#customer_id,**kwargs):
	try:
		get = db.user.find()
		return dumps(get)
	except Exception, e:
		return dumps({'error' : str(e)})

@app.route("/api/feature/list_all", methods = ['GET'])
def get_all_feature():#customer_id,**kwargs):
	try:
		get = db.feature.find()
		return dumps(get)
	except Exception, e:
		return dumps({'error' : str(e)})


#Clear database
@app.route("/remove", methods=['GET', 'POST'])
def remove():
    db.plan.drop()
    return dumps({'message' : 'Removed successfully'})

if __name__ == '__main__':
   app.run(debug = True)