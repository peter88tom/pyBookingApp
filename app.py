from flask import Flask, render_template, session,redirect, request, url_for, flash
from flask_mysqldb import MySQL

app = Flask(__name__)
mysql = MySQL()

# MySQL configurations
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'chanzodata'
app.config['MYSQL_DB'] = 'pybookingapp'
app.config['MYSQL_HOST'] = 'localhost'
mysql.init_app(app)

# Default route for the application if session exist otherwise show login page
@app.route('/')
def index():
	if 'username' in session:
		return render_template('dashboard.html',username=session['username'])
   
	return render_template('login.html')


# Login page
@app.route('/login', methods=['POST'])
def login(): 
	# Check if request is POST
	if request.method == 'POST':

		# Assign the posted form data to variables
		usrname = request.form['user_name']
		pswd = request.form['password']

		# Initiate connection to mysql
		conn = mysql.connection.cursor()

		# Run SQL query
		conn.execute(''' SELECT * FROM py_users WHERE `user_name`="%s" AND `user_password`="%s" ''' %(usrname,pswd))
		returnuser = conn.fetchall()
		if returnuser:
			# user found in the database, give session and redirect to index
			session['username'] = request.form['user_name']
			return redirect(url_for('index'))
            
        # return login if request is not a post
		return render_template('login.html')


	return render_template()


#customers
@app.route('/customers')
def customers():
	pass


#Events
@app.route('/book_events')
def book_events():
	if 'username' in session:
		# Initiate connection to mysql to get event types,
		dbconnect = mysql.connection.cursor()
		# Select all events
		dbconnect.execute(''' SELECT * FROM event_types ''')
		getevents = dbconnect.fetchall()
        
        # fetch banks
		dbconnect.execute(''' SELECT * FROM banks ''')
		getbanks = dbconnect.fetchall()
		myname = "peter"

		return render_template('book_events.html', username=session['username'],namename=myname, events=getevents, banks=getbanks)

	return render_template('login.html')

# Banks
@app.route('/banks')
def banks():
	pass

# Payments
@app.route('/payments')
def payments():
	pass



# logout user
@app.route('/logout')
def logout():
	# Remove username from session if its there
	session.pop('username',None)
	return redirect(url_for('index'))


if __name__ == '__main__':
	app.secret_key = 'WER%DF$%^&#$#@FWE$^#@%$@#'
	app.run(debug=True)