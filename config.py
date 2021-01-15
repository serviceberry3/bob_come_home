import os
#main directory of application
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'

    #location of app's database, for Flask-SQLAlchemy extension. If undefined, configure db named app.db in main dir of app
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///' + os.path.join(basedir, 'app.db')

    #disable signaling app every time a change is about to be made in db
    SQLALCHEMY_TRACK_MODIFICATIONS = False