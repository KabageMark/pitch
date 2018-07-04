from flask import Flask
from config import DevConfig
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

app = Flask(__name__)
bootstrap = Bootstrap(app)
db = SQLAlchemy()
login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'auth.login'

app.config.from_object(DevConfig)
 
login_manager.init_app(app) 

from app.main import views

# registering the blueprint



def create_app(config_name):
    #...
    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint,url_prefix = '/authenticate')
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)   



    return app
