from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
	__tablename__ = 'template'
	address = db.Column(db.String(64), primary_key=True)
	year_built = db.Column(db.Integer, nullable=False)
	beds = db.Column(db.Integer, nullable=False)
	baths = db.Column(db.Integer, nullable=False)
	sqft = db.Column(db.Integer, nullable=False)
	floors = db.Column(db.Integer, nullable=False)
	type_ = db.Column(db.String(64), nullable=False)
	rental = db.Column(db.Boolean, nullable=False)


