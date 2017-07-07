from flask import Flask, render_template, session,redirect, request, url_for
from flask_mysqldb import MySQL

app = Flask(__name__)
mysql = MySQL()

# MySQL configurations
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'pybookingapp'
app.config['MYSQL_HOST'] = 'localhost'
mysql.init_app(app)

# Default route for the application if session exist otherwise show login page
@app.route('/')
def index():
	if 'username' in session:
		return render_template('dashboard.html',username=session['username'])
		#return 'You are logged in  as ' + session['username']

	return render_template('login.html')


# Login page
@app.route('/login', methods=['POST'])
def login(): 
	# Check if request is POST
	if request.method == 'POST':

		# Assign the posted form data to variables
		eml = request.form['email'].format()
		pswd = request.form['password'].format()

		# Initiate connection to mysql
		conn = mysql.connection.cursor()

		# Run SQL query
		conn.execute('''SELECT * FROM py_users WHERE user_email="" AND user_password=""''')
		rv = conn.fetchall()
		if rv:
			# user found in the database, give session and redirect to index
			session['username'] = request.form['email']
			return redirect(url_for('index'))

		return render_template('login.html')

	return "Method Not Allowed"



# logout user
@app.route('/logout')
def logout():
	# Remove username from session if its there
	session.pop('username',None)
	return redirect(url_for('index'))


if __name__ == '__main__':
	app.secret_key = ''
	app.run(debug=True)