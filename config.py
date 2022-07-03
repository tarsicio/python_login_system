class Config:
	SECRET_KEY = 'tarsicio'

class DevelomentConfing(Config):
	DEBUG = True	
	SQLALCHEMY_DATABASE_URI ='sqlite:///python.sqlite'
	SQLALCHEMY_DATABASE_URI_01 ='mysql://root:clave@localhost/python'

config = {
	'develoment': DevelomentConfing,
	'default': DevelomentConfing
}	
