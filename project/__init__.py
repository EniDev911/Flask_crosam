from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# init SQLAlchemy
db = SQLAlchemy()

def create_app():
	app = Flask(__name__)

	app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'

	db.init_app(app)

	# blueprint para nuestras rutas
	from .auth import auth as auth_blueprint
	app.register_blueprint(auth_blueprint)

	# blueprint para los no autenticado en nuestra app
	from .main import main as main_blueprint
	app.register_blueprint(main_blueprint)

	return app

	


