from flask import Flask, render_template, request, redirect
from flask_heroku import Heroku
import psycopg2
import os
from werkzeug.utils import secure_filename
from models import *

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
				print("Image saved")
				return redirect(request.url)

			else:
				print("That file extension is not allowed")
				return redirect(request.url)
	return render_template("upload_image.html")


if __name__ == "__main__":
	app.run(debug=True)
