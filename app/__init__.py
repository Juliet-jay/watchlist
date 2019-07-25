from flask import Flask
from .config import Devconfig
from flask_bootstrap import Bootstrap
# Initializing application
app = Flask(__name__,instance_relative_config = True)

# setting up configuration 
app.config.from_object(Devconfig)
app.config.from_pyfile('config.py')

# Initializing Flask Extentions
Bootstrap = Bootstrap(app)

from app import views
