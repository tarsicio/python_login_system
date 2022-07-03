from wtforms import Form, HiddenField
from wtforms import validators
from wtforms import StringField, PasswordField, BooleanField
from wtforms.fields import DateField, EmailField, TelField

from .models import User

def codi_validator(form,field):
	if field.data == 'codi' or field.data == 'CODI':
		raise validators.ValidationError('El usuario codi no es permitido')

def length_honeypot(form, field):
    if len(field.data) > 0:
        raise validators.ValidationError('Solo los humanos pueden completar el registro!')

class LoginForm(Form):
	username = StringField('Username',[
		validators.Length(min=4, max=50)
		])
	password = PasswordField('Password',[
		validators.DataRequired()	
		])

class RegisterForm(Form):
	username = StringField('Username',[
		validators.Length(min=4, max=50),
		codi_validator
		])
	email = EmailField('Email',[
		validators.Length(min=1, max=100),
		validators.DataRequired(message='El Email es Requerido'),
		validators.Email(message='Ingrese un Email valido')
		])
	password = PasswordField('Password',[
		validators.DataRequired('El Password es requerido'),
		validators.EqualTo('confirm_password',message='La contraseña no coincide')	
		])
	confirm_password = PasswordField('Confirm password')
	accept = BooleanField('',[
		validators.DataRequired()
		])
	honeypot = HiddenField("", [ length_honeypot] )

	def validate_username(self,username):
		if User.get_by_username(username.data):
			raise validators.ValidationError('El usuario ya esta en Uso...!')		

	def validate_email(self,email):
		if User.get_by_email(email.data):
			raise validators.ValidationError('El Email ya esta en uso, escoja otro...!')				