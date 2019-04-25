from flask import Flask, session
from flask import Flask, render_template, render_template, redirect, url_for, request,g
import os

app = Flask(__name__)
app.secret_key = os.urandom(24)

@app.route('/', methods=['GET', 'POST'])
def sess():

	error = None
	if request.method == 'POST':
		session.pop('user',None)
		if request.form['username'] =='admin' or request.form['password'] =='admin':
			session['user'] = request.form['username']
			return redirect(url_for('protected'))

	return render_template('index.html', error=error)

@app.route('/protected')
def protected():
	if g.user:
		return render_template('protected.html')

	return render_template('index.html')	


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
	return 'Dropped'

if __name__ == "__main__":
    app.run(debug = True)