from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
import logging
from logging.handlers import RotatingFileHandler
import os

#create application obj as instance of class Flask
app = Flask(__name__) #name var is predefined, set to name of module in which it's used, used to load template files etc.
app.secret_key = 'you-will-never-guess'

#tell flask to read and apply config file
app.config.from_object(Config)

app.debug = False

#instantiate an SQLAlchemy database
db = SQLAlchemy(app)

#instantiate a Flask-Migrate migration engine
migrate = Migrate(app, db)

login = LoginManager(app)

#tell Flask-Login what is the view fxn that handles logins so that we can block access to pages and redirect to login screen
login.login_view = 'login'


#the app package is defined by the app directory. Routes are the different URLs that the app implements
from app import routes, models #models module will define structure of db

if not app.debug:
    if not os.path.exists('logs'):
        os.mkdir('logs')
    file_handler = RotatingFileHandler('logs/bob.log', maxBytes=10240, backupCount=10)
    file_handler.setFormatter(logging.Formatter('%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'))
    file_handler.setLevel(logging.INFO)
    app.logger.addHandler(file_handler)
    app.logger.setLevel(logging.INFO)
    app.logger.info('Bob startup')
