from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, TextAreaField
from wtforms.validators import DataRequired

class RegisterForm(FlaskForm):
	username = StringField('Enter a Username:', validators=[DataRequired()])
	email = StringField('Enter your Email:', validators=[DataRequired()])
	password = PasswordField('Enter a Password:', validators=[DataRequired()])
	submit = SubmitField('Register')

class LoginForm(FlaskForm):
	username = StringField('Enter your Username:', validators=[DataRequired()])
	password = PasswordField('Enter your Password:', validators=[DataRequired()])
	submit = SubmitField('Login')