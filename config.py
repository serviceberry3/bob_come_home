import os
#main directory of application
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'

    #location of app's database, for Flask-SQLAlchemy extension. If undefined, configure db named app.db in main dir of app
    #IMPORTANT: if environ var DATABASE_URL not set, will TRY TO USE SQLITE!!!!
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///' + os.path.join(basedir, 'app.db')
    #SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://bob:faPple3^@localhost:3306/bob'

    #disable signaling app every time a change is about to be made in db
    SQLALCHEMY_TRACK_MODIFICATIONS = False
