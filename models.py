from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Property(db.Model):
	__tablename__ = 'properties'
	id = db.Column(db.Integer, primary_key=True)
	mls_num = db.Column(db.String(8), nullable=False)
	status_id = db.Column(db.Integer, db.ForeignKey("status.id"), nullable=False)
	list_price = db.Column(db.Integer, nullable=False)
	sold_price = db.Column(db.Integer, nullable=False)
	list_date = db.Column(db.DateTime, nullable=False)
	sold_date = db.Column(db.DateTime, nullable=False)
	dom = db.Column(db.Integer, nullable=False)
	dto = db.Column(db.Integer, nullable=False)
	address = db.Column(db.Integer, db.ForeignKey("addresses.id"), nullable=False)
	area = db.Column(db.Integer, nullable=True)
	beds = db.Column(db.Integer, nullable=False)
	baths = db.Column(db.Float, nullable=False)
	sqft = db.Column(db.Integer, nullable=False)
	age = db.Column(db.Integer, nullable=False)
	lot_size = db.Column(db.Integer, nullable=True)
	agent_info = db.Column(db.Integer, db.ForeignKey("agents.id"), nullable=False)
	showing_instructions = db.Column(db.String(256), nullable=True)
	remarks = db.Column(db.String(256), nullable=True)
	style = db.Column(db.Integer, db.ForeignKey("styles.id"), nullable=False)
	level = db.Column(db.Integer, nullable=True)
	garage = db.Column(db.Integer, nullable=False)
	heating = db.Column(db.Integer, db.ForeignKey("heating.id"), nullable=False)
	cooling = db.Column(db.Integer, db.ForeignKey("cooling.id"), nullable=False)
	elementary = db.Column(db.Integer, db.ForeignKey("elementary_schools.id"), nullable=False)
	junior_high = db.Column(db.Integer, db.ForeignKey("junior_highs.id"), nullable=False)
	high_school = db.Column(db.Integer, db.ForeignKey("high_schools.id"), nullable=False)
	other_features = db.Column(db.Integer, db.ForeignKey("other_features.id"), nullable=False)
	property_type = db.Column(db.Integer, db.ForeignKey("property_types.id"), nullable=False)
	photo_url = db.Column(db.String(128), nullable=False)


class Status(db.Model):
	__tablename__ = 'status'
	id = db.Column(db.Integer, primary_key=True)
	status = db.Column(db.String(4), nullable=True)


class Address(db.Model):
	__tablename__ = 'addresses'
	id = db.Column(db.Integer, primary_key=True)
	address = db.Column(db.String(128), nullable=False)
	city_id = db.Column(db.Integer, db.ForeignKey("cities.id"), nullable=False)
	state_id = db.Column(db.Integer, db.ForeignKey("states.id"), nullable=False)
	zip_code_id = db.Column(db.Integer, db.ForeignKey("zips.id"), nullable=False)
	street_name_id = db.Column(db.Integer, db.ForeignKey("streets.id"), nullable=False)
	house_num_1 = db.Column(db.String(64), nullable=True)
	house_num_2 = db.Column(db.String(64), nullable=True)


class City(db.Model):
	__tablename__ = 'cities'
	id = db.Column(db.Integer, primary_key=True)
	city = db.Column(db.String(64), nullable=False)


class State(db.Model):
	__tablename__ = 'states'
	id = db.Column(db.Integer, primary_key=True)
	state = db.Column(db.String(64), nullable=False)


class Zip(db.Model):
	__tablename__ = 'zips'
	id = db.Column(db.Integer, primary_key=True)
	zip_code = db.Column(db.String(64), nullable=False)


class Street(db.Model):
	__tablename__ = 'streets'
	id = db.Column(db.Integer, primary_key=True)
	street = db.Column(db.String(64), nullable=False)


class Agent(db.Model):
	__tablename__ = 'agents'
	id = db.Column(db.Integer, primary_key=True)
	agent = db.Column(db.String(64), nullable=False)
	office = db.Column(db.Integer, db.ForeignKey("offices.id"), nullable=False)


class Office(db.Model):
	__tablename__ = 'offices'
	id = db.Column(db.Integer, primary_key=True)
	office_name = db.Column(db.String(64), nullable=False)
	office_phone = db.Column(db.String(64), nullable=False)


class Style(db.Model):
	__tablename__ = 'styles'
	id = db.Column(db.Integer, primary_key=True)
	style = db.Column(db.String(64), nullable=False)


class Heating(db.Model):
	__tablename__ = 'heating'
	id = db.Column(db.Integer, primary_key=True)
	heating_type = db.Column(db.String(64), nullable=True)


class Cooling(db.Model):
	__tablename__ = 'cooling'
	id = db.Column(db.Integer, primary_key=True)
	cooling_type = db.Column(db.String(64), nullable=True)


class Elementary(db.Model):
	__tablename__ = 'elementary_schools'
	id = db.Column(db.Integer, primary_key=True)
	elementary = db.Column(db.String(128), nullable=True)


class Junior(db.Model):
	__tablename__ = 'junior_highs'
	id = db.Column(db.Integer, primary_key=True)
	junior_high = db.Column(db.String(128), nullable=True)


class High(db.Model):
	__tablename__ = 'high_schools'
	id = db.Column(db.Integer, primary_key=True)
	highschool = db.Column(db.String(128), nullable=True)


class Features(db.Model):
	__tablename__ = 'other_features'
	id = db.Column(db.Integer, primary_key=True)
	features = db.Column(db.String(256), nullable=True)


class PropType(db.Model):
	__tablename__ = 'property_types'
	id = db.Column(db.Integer, primary_key=True)
	prop_types = db.Column(db.String(64), nullable=True)


