from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Property(db.Model):
	__tablename__ = 'properties'
	cid = db.Column(db.Integer, primary_key=True, autoincrement=True)
	mls_num = db.Column(db.Integer, nullable=False)
	zip = db.Column(db.String, nullable=False)
	beds = db.Column(db.Integer, nullable=False)
	baths = db.Column(db.Float, nullable=False)	
	sqft = db.Column(db.Float, nullable=False)
	list_price = db.Column(db.Integer, nullable=False)
	photo_url = db.Column(db.String(128), nullable=False)
	address = db.Column(db.String(256))
	city = db.Column(db.String(128))
	state = db.Column(db.String(4))
	remarks = db.Column(db.String(1024))
	style = db.Column(db.String(128))


class Photo(db.Model):
	__tablename__ = 'photos'
	pid = db.Column(db.Integer, primary_key=True, autoincrement=True)
	mls_num = db.Column(db.Integer, nullable=False)
	img_num = db.Column(db.Integer, nullable=False)
	features = db.Column(db.String, nullable=False)


class User(db.Model):
	__tablename__ = 'users'
	uid = db.Column(db.Integer, primary_key=True, autoincrement=True)
	username = db.Column(db.String, unique=True, nullable=False)
	email = db.Column(db.String, unique=True, nullable=False)
	password = db.Column(db.String(128), nullable=False)




