from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

#create application obj as instance of class Flask
app = Flask(__name__) #name var is predefined, set to name of module in which it's used, used to load template files etc.

#tell flask to read and apply config file
app.config.from_object(Config)

#instantiate an SQLAlchemy database
db = SQLAlchemy(app)

#instantiate a Flask-Migrate migration engine
migrate = Migrate(app, db)

login = LoginManager(app)

#tell Flask-Login what is the view fxn that handles logins so that we can block access to pages and redirect to login screen
login.login_view = 'login'


#the app package is defined by the app directory. Routes are the different URLs that the app implements
from app import routes, models #models module will define structure of db