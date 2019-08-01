import csv
import os

from flask import Flask, render_template, request
from models import *

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

#engine = create_engine('postgresql://postgres:########@localhost/housingapp')
#db = scoped_session(sessionmaker(bind=engine))

app = Flask(__name__)

# Need to uncomment the line below and add password
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:########@localhost/housingapp'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

def main():
	f = open("static/data/properties.csv")
	reader = csv.reader(f)
	next(reader, None)
	for MLSNUM, LISTPRICE, ZIP, BEDS, BATHS, SQFT, PHOTOURL in reader:
		property = Property(mls_num=MLSNUM, list_price=LISTPRICE, zip=ZIP, beds=BEDS, baths=BATHS, sqft=SQFT, photo_url=PHOTOURL)
		db.session.add(property)
	db.session.commit()

if __name__ == '__main__':
	with app.app_context():
		main()
