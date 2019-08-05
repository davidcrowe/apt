from flask import Flask, render_template, request, redirect, session
from flask_heroku import Heroku
import psycopg2
import os
from werkzeug.utils import secure_filename
from models import db, Property
from forms import RegisterForm, LoginForm
from img_nn import *

app = Flask(__name__)

# comment the first line below for deploying to heroku; comment second line for local deployment 

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:########@localhost/housingapp'
#heroku = Heroku(app)

# Set configurations for image upload functionality
app.config["IMAGE_UPLOADS"] = "/Users/davidcrowe/code/harvard/csci_s14a/final_project/repo/HES-CSCI_S14A-CNN_Semantic_Segmentation_Team_10/uploads"
app.config["ALLOWED_IMAGE_EXTENSIONS"] = ["JPEG", "JPG", "PNG", "GIF"]
app.config["MAX_CONTENT_LENGTH"] = 50 * 1024 * 1024

db.init_app(app)

app.secret_key = "final-project-key"


@app.route("/")
@app.route('/index')
def index():
	return render_template("index.html", title="Home")
	#if 'username' in session:
		#session_user = User.query.filter_by(username=session['username']).first()
		#return render_template('index.html', title='Home', session_username=session_user.username)
	#else:
		#return render_template("index.html", title="Home")

@app.route("/register", methods=['GET', 'POST'])
def register():
	message = "Register"
	form = RegisterForm()
	if request.method == 'POST':
		username = request.form['username']
		email = request.form['email']
		password = request.form['password']
		existing_user = User.query.filter_by(username=username).first()
		if existing_user:
			flash('The username already exists. Please pick another one.')
			return redirect(url_for('register'))
		existing_email = User.query.filter_by(email=email).first()
		if existing_email:
			flash('There is already an account associated with that email. Please try again.')
			return redirect(url_for('register'))
		else:
			user = User(username=username, email=email, passwrd=sha256_crypt.hash(password))
			db.session.add(user)
			db.session.commit()
			flash('Congratulations, you are now a registered user!')
			return redirect(url_for('login'))
	else:
		return render_template('register.html', message=message, form=form)


@app.route("/login", methods=['GET', 'POST'])
def login():
	message = "Login"
	form = LoginForm()
	if request.method == 'POST':
		username = request.form['username']
		password = request.form['password']
		user = User.query.filter_by(username=username).first()
		if user is None or not sha256_crypt.verify(password, user.password):
			flash('Invalid username or password')
			return redirect(url_for('login'))
		else:
			session['username'] = username
			return redirect(url_for('index'))	
	else:
		return render_template("login.html", message=message, form=form)

@app.route('/logout', methods=['POST'])
def logout():
	session.clear()
	return redirect(url_for('index'))

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
	propertys = Property.query.filter().limit(10).all()
	return render_template("view-properties.html", propertys = propertys)


def allowed_image(filename):
	# We only want files with a . in the filename
	if not "." in filename:
		return False 

	# Split the extension from the filename
	ext = filename.rsplit(".", 1)[1]

	# Check if the extension is in ALLOWED_IMAGE_EXTENSIONS
	if ext.upper() in app.config["ALLOWED_IMAGE_EXTENSIONS"]:
		return True
	else:
		return False


@app.route("/upload-image", methods=["GET", "POST"])
def upload_image():
	if request.method == "POST":
		if request.files:
			image = request.files["image"]

			if image.filename == "":
				print("No filename")
				return redirect(request.url)

			if allowed_image(image.filename):
				filename = secure_filename(image.filename)
				image.save(os.path.join(app.config["IMAGE_UPLOADS"], filename))
				loc = os.path.join(app.config["IMAGE_UPLOADS"], filename)
				print("Loc: ")
				print(loc)
				print("Image saved")
				data_df = upload_nn(loc, dict())
				print("nn_output should now be rendered")
				return render_template("nn_output.html", data_df=data_df)

			else:
				print("That file extension is not allowed")
				return redirect(request.url)
				
	return render_template("upload_image.html")


if __name__ == "__main__":
	app.run(debug=True)
