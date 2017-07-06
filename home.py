from flask import Flask, render_template, session, url_for, redirect, request
app = Flask(__name__)

@app.route('/')
def index():
	if 'username' in session:
		return 'You are logged in  as ' + session['username']

	return render_template('login.html')


# Login page
@app.route('/login')
def login():
	return render_template('login.html')

if __name__ == '__main__':
	app.run(debug=True)