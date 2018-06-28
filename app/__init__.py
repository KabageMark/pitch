from flask import Flask
from config import DevConfig
 


app = Flask(__name__)

app.config.from_object(DevConfig)

from app.main import views

# registering the blueprint
from .main import main as main_blueprint
app.register_blueprint(main_blueprint)