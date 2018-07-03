from flask import Flask
from config import DevConfig
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
bootstrap = Bootstrap(app)
db = SQLAlchemy()

app.config.from_object(DevConfig)
 

from app.main import views

# registering the blueprint
from .main import main as main_blueprint
app.register_blueprint(main_blueprint)





