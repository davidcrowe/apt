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


class Photo(db.Model):
	__tablename__ = 'photos'
	pid = db.Column(db.Integer, primary_key=True, autoincrement=True)
	mls_num = db.Column(db.Integer, nullable=False)
	img_num = db.Column(db.Integer, nullable=False)
	features = db.Column(db.String, nullable=False)





