from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
	message = "Hello world"
	return render_template("layout.html", message=message)


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