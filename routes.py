import psycopg2
import os
from flask import Flask, flash, render_template, request, redirect, jsonify, session, url_for
from flask_heroku import Heroku
from werkzeug.utils import secure_filename
from passlib.hash import sha256_crypt
from models import *
from img_nn import *
from forms import RegisterForm, LoginForm

app = Flask(__name__)


# comment the first line below for deploying to heroku; comment second line for local deployment 
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:baja1880@localhost/housingapp'
# Also need to be sure to remove requirements.txt from .gitignore in order to deploy to Heroku
#heroku = Heroku(app)

# Set configurations for image upload functionality
# Note - IMAGE_UPLOADS will need to change in order to deploy to Heroku
##app.config["IMAGE_UPLOADS"] = "/uploads/"
app.config["IMAGE_UPLOADS"] = "/Users/davidcrowe/code/harvard/csci_s14a/final_project/repo/HES-CSCI_S14A-CNN_Semantic_Segmentation_Team_10/uploads"
app.config["ALLOWED_IMAGE_EXTENSIONS"] = ["JPEG", "JPG", "PNG", "GIF"]
app.config["MAX_CONTENT_LENGTH"] = 50 * 1024 * 1024


db.init_app(app)

app.secret_key = "final-project-key"


@app.route("/")
@app.route('/index')
def index():
	# return render_template("index.html", title="Home")
	if 'username' in session:
		session_user = User.query.filter_by(username=session['username']).first()
		return render_template('index.html', title='Home', session_username=session_user.username)
	else:
		return render_template("index.html", title="Home")

@app.route("/register", methods=['GET', 'POST'])
def register():
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
		return render_template('register.html', form=form)


@app.route("/login", methods=['GET', 'POST'])
def login():
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
		return render_template("login.html", form=form)

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

# This used to be property-detail
@app.route("/<cid>")
def property_detail(cid):
	property = Property.query.get(cid)

	mls = str(property.mls_num)
	print(mls)

	#mls = str(71857486)
	photos = Photo.query.all()
	mlsNums = []

	for photo in photos:
		mlsNums.append(photo.mls_num)
		print(mlsNums)

		photo_mls = photos.mls_num
	if mls in mlsNums:
		prop_func = Photo.query.filter_by(mls_num=str(mls)).first()
		db_images = Photo.query.filter().limit(20).all()
		closest = []
		closest = findClosestPropDetail(prop_func, db_images)
	else:
		print('else')

		# closest must equal to dictonary
		closest = ['71835057', '71895128', '71895125', '71826868', '71902172']

	print(closest)

	final_product = Property.query.filter(Property.mls_num.in_(closest)).all()

	print(final_product)

	return render_template('property-detail.html', property=property, closest=closest, final_product = final_product)


@app.route("/view-properties")
def view_properties():
	#propertys = Property.query.paginate(1, 20, False).items
	page = request.args.get('page', 1, type=int)
	propertys = Property.query.paginate(page, 30, False)
	next_url = url_for('view_properties', page=propertys.next_num) \
		if propertys.has_next else None
	prev_url = url_for('view_properties', page=propertys.prev_num) \
		if propertys.has_prev else None
	return render_template("view-properties.html", propertys = propertys.items, next_url=next_url, prev_url=prev_url)



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

			db_images = Photo.query.filter().all()
			upload_image = request.files["image"]

			if upload_image.filename == "":
				print("No filename")
				return redirect(request.url)

			if allowed_image(upload_image.filename):
				filename = secure_filename(upload_image.filename)
				upload_image.save(os.path.join(app.config["IMAGE_UPLOADS"], filename))
				loc = os.path.join(app.config["IMAGE_UPLOADS"], filename)
				print("Loc: ")
				print(loc)
				print("Image saved")

				closest = findClosest(upload_image, db_images)
				print(closest)
				#data_df = upload_nn(loc, dict())
				#print("nn_output should now be rendered")
				return render_template("nn_output.html")

			else:
				print("That file extension is not allowed")
				return redirect(request.url)
				
	return render_template("upload_image.html")


if __name__ == "__main__":
	app.run(debug=True)
