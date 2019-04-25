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
def hello_world():
   return "Hello World"

#add the data
@app.route("/add_task", methods = ['POST'])
def add_task():
    try:
    	data = json.loads(request.data)
    	user_room = data['room']
    	user_topic = data['topic']
    	user_stb = data['stb']
    	user_organizer = data['organizer']
    	user_attnedee = data['attendee']
        status = db.Task.insert({
            "room" : user_room,
            "topic" : user_topic,
            "stb": user_stb,
            "organizer": user_organizer,
            "attendee": user_attnedee
            })
        return dumps({'message' : 'SUCCESS'})
    except Exception, e:
        return dumps({'error' : str(e)})

#veiw all the data
@app.route("/get_all_task", methods = ['GET'])
def get_all_contact():
    try:
        tasks = db.Task.find()
        return dumps(tasks)
    except Exception, e:
        return dumps({'error' : str(e)})


if __name__ == '__main__':
   app.run()