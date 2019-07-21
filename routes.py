from flask import Flask, render_template
from flask_heroku import Heroku
from models import db, User

app = Flask(__name__)

# heroku = Heroku(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgres@localhost/housingapp'
db.init_app(app)

@app.route("/")
def index():
	return render_template("landing.html")


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