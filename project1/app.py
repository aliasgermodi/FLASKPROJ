#Import the Flask class from the flask module
from flask import Flask, render_template, redirect, url_for, request, session, flash, g
from functools import wraps
import sqlite3

#create the application object
app = Flask(__name__)

#need secret key to avoid runtime error(for session)
app.secret_key = 'my precious'
app.database = 'sample.db'

#this is used for user authentication(if not logged in, it redirects to login page)
def login_required(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return f(*args, **kwargs)
        else:
            flash('You need to login first.')
            return redirect(url_for('login'))
    return wrap

#use decorators to link the function to a url 
@app.route('/')
@login_required #to come to index.html login is required.
def home():
        g.db = connect_db() #g is a flask tool, for temporary storage
    	cur = g.db.execute('select * from posts') #query the database
    	posts = [dict(title=row[0], description=row[1]) for row in cur.fetchall()] #put it in a dictionary
	g.db.close() #close the database
	#return "Hello, World!"  #return a string
    	return render_template('index.html', posts=posts) #render a template, post the database on the tamplate	

@app.route('/welcome')
def welcome():
	return render_template('welcome.html') #render template

# route for handling the login page logic
@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
            error = 'Invalid Credentials. Please try again.'
        else:
	    session['logged_in'] = True
	    flash('You were logged in.')		
            return redirect(url_for('home'))
    return render_template('login.html', error=error)

# route handling log out logic.
@app.route('/logout')
@login_required #to come to logout page login is required.
def logout():
	session.pop('logged_in',None)
	flash('You were logged out')
	return redirect(url_for('welcome'))

# connect to database
def connect_db():
	return sqlite3.connect(app.database)

#start the server with the 'run()' method
if __name__ == '__main__':
	app.run(debug=True)
