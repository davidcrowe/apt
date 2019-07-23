import csv
import os

from flask import Flask, render_template, request
from models import *

#from sqlalchemy import create_engine
#from sqlalchemy.orm import scoped_session, sessionmaker

#engine = create_engine('postgresql://postgres:baja1880@localhost/housingapp')
#db = scoped_session(sessionmaker(bind=engine))

app = Flask(__name__)
# Need to uncomment the line below and add password
#app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:########@localhost/housingapp'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

def main():
	f = open("property_table.csv")
	reader = csv.reader(f)
	for MLSNUM, LISTPRICE, SOLDPRICE, LISTDATE, SOLDDATE, DOM, DTO, AREA, BEDS, BATHS, SQFT, AGE, LOTSIZE, SHOWINGINSTRUCTIONS, \
		REMARKS, LEVEL, GARAGE, PHOTOURL in reader:
		property = Property(mls_num=MLSNUM, list_price=LISTPRICE, sold_price=SOLDPRICE, list_date=LISTDATE, sold_date=SOLDDATE, dom=DOM, dto=DTO, \
			area=AREA, beds=BEDS, baths=BATHS, sqft=SQFT, age=AGE, lot_size=LOTSIZE, showing_instructions=SHOWINGINSTRUCTIONS, \
			remarks=REMARKS, level=LEVEL, garage=GARAGE, photo_url=PHOTOURL)
		db.session.add(property)
	db.session.commit()

if __name__ == '__main__':
	with app.app_context():
		main()




#STATUS, ADDRESS, AGENTINFO, STYLE, HEATING, COOLING, ELEMENTARY, JUNIORHIGH, HIGHSCHOOL, OTHERFEATURES, PROPERTYTYPE, 

