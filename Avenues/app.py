from flask import Flask, url_for, redirect, render_template, request, abort, session
from flask import Flask, render_template, render_template, redirect, url_for, request,g
from flask import Flask
from flask_pymongo import PyMongo
from bson.json_util import dumps





app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27017/myDatabase"
mongo = PyMongo(app)

@app.route('/')
def index():
	return render_template("upload.html")

@app.route('/create', methods=['POST'])
def create():
	if 'cms_image' in request.files:
		cms_image = request.files['cms_image']
		mongo.save_file(cms_image.filename, cms_image)
		mongo.db.users.insert({'username':request.form.get('username'), 'cms_image': cms_image.filename})

	return 'DONE'

@app.route('/filename/<filename>')
def file(filename):
	return mongo.send_file(filename)

@app.route('/profile_<username>')
def profile(username):

	user = mongo.db.users.find({'username':username})

	return render_template("show.html", user = user)

@app.route('/mprofile_<username>')
def mprofile(username):

	user = mongo.db.users.find({'username':username})
	users = {"screen":user}
	#return render_template("show.html", user = {"screen":user})
	return dumps(users)


@app.route('/get_all')
def get_all():
	
	user = mongo.db.users.find()
	

	return dumps(user)

#delete all the data
@app.route("/remove", methods=['GET', 'POST'])
def remove():
    mongo.db.users.drop()
    return dumps({'message' : 'Removed successfully'})

if __name__ == '__main__':
   app.run(debug = True)