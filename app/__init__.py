from flask import Flask
from .config import Devconfig

# Initializing application
app = Flask(__name__,instance_relative_config = True)

# setting up configuration 
app.config.from_object(Devconfig)
app.config.from_pyfile('config.py')

from app import views