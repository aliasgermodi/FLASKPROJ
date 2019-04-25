# import the Flask class from the flask module
from flask import Flask, render_template, render_template, redirect, url_for, request
from bson.json_util import dumps
from flask import Flask
from flask_pymongo import PyMongo
import json
from pymongo import MongoClient
import os

from werkzeug import secure_filename


app = Flask(__name__)
client = MongoClient('localhost:27017')
db = client.TaskDB

# create the application object
app = Flask(__name__)


UPLOAD_FOLDER = 'static/images'
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


# use decorators to link the function to a url
@app.route('/')
def home():
    return "Hello, World!"  # return a string

@app.route('/welcome')
def welcome():
    return render_template('hello.html')  # render a template


# Route for handling the login page logic
@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
            error = 'Invalid Credentials. Please try again.'
        else:
            return redirect(url_for('welcome'))
    return render_template('login.html', error=error)


#add the data
@app.route("/add_country", methods = ['POST'])
def add_cou():
    try:
        data = json.loads(request.data)
        country = data['country']
        project = "project 1"
        #last_seen = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
        if country:
            db.Task.insert_one({"country": country,"project": project})
        return dumps({'message' : 'SUCCESS'})
    except Exception, e:
        return dumps({'error' : str(e)})


#veiw all the data
@app.route("/get_all_task", methods = ['GET'])
def get_all_contact():
    try:
        tasks = db.Project.find()
        return dumps(tasks)
    except Exception, e:
        return dumps({'error' : str(e)})

#uploading of images to a folder
@app.route('/upload')
def upload():
   return render_template('upload.html')

    
@app.route('/uploader', methods = ['GET', 'POST'])
def upload_file():
   if request.method == 'POST':
      f = request.files['file']
      filename = f.filename
      f.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
      return 'file uploaded successfully'


#add project details
@app.route("/add_project", methods=['GET','POST'])
def add_project ():
    #Adding a Task
    data = json.loads(request.data)

    status = db.Project.insert({
        "id":data['id'],
        "project":{"project_name":data['project'],"country":data['country']}
        })
    return dumps({'message' : 'SUCCESS'})
    #return render_template('project.html')
    

#get project details in table format
@app.route("/get_project", methods=['GET'])
def get_project():
    id = db.Project.find()
    project = db.Project.find()
    print project
    return render_template('admin.html', id = id, project = project)

#delete all the data
@app.route("/remove", methods=['GET', 'POST'])
def remove():
    db.Project.drop()
    return dumps({'message' : 'Removed successfully'})

# start the server with the 'run()' method
if __name__ == "__main__":
    app.run(host='127.0.0.1', port='5000',debug=True)

