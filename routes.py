from flask import Flask, render_template
from flask_heroku import Heroku
from models import db, Property
import psycopg2


app = Flask(__name__)
#app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:baja1880@localhost/housingapp'
heroku = Heroku(app)

db.init_app(app)

app.secret_key = "final-project-key"


@app.route("/")
def index():
	properties = Property.query.all()
	return render_template("landing.html", properties=properties)


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


if __name__ == "__main__":
	app.run(debug=True)