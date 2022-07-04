class Config:
	SECRET_KEY = 'cambiar_por_otra_mas_robusta'

class DevelomentConfing(Config):
	DEBUG = True	
	SQLALCHEMY_DATABASE_URI ='sqlite:///python.sqlite'
	SQLALCHEMY_DATABASE_URI_01 ='mysql://root:clave@localhost/python'
	SQLALCHEMY_TRACK_MODIFICATIONS = False



config = {
	'develoment': DevelomentConfing,
	'default': DevelomentConfing
}	
