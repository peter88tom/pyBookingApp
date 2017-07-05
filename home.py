from flask import flask
app = Flask(__name__)

@app.route('/')
def index():
	return 'Hello booking App'

if __name__ == '__main__':
	app.run()