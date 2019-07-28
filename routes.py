from flask import Flask, render_template
from flask_heroku import Heroku
import psycopg2
from models import *

app = Flask(__name__)

# comment the first line below for deploying to heroku; comment second line for local deployment 

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:baja1880@localhost/housingapp'
#heroku = Heroku(app)

db.init_app(app)

app.secret_key = "final-project-key"


@app.route("/")
def index():
	#properties = Property.query.all()
	#
	#test = Property.query.get(1) 
	return render_template("index.html")


@app.route("/register")
def register():
	message = "Register"
	return render_template("register.html", message=message)


@app.route("/login")
def login():
	message = "Login"
	return render_template("login.html", message=message)


@app.route("/landing")
def landing():
	return render_template("landing.html")



@app.route("/begin-search")
def begin_search():
	return render_template("begin-search.html")


@app.route("/property-detail")
def property_detail():
	return render_template("property-detail.html")


@app.route("/view-properties")
def view_properties():
	return render_template("view-properties.html")


if __name__ == "__main__":
	app.run(debug=True)
