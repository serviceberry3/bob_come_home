from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

#import LoginManager instance from __init__.py
from app import login

#import db from __init__.py, which is SQLAlchemy instance
from app import db

#Model is base class for all models from Flask-SQLAlchemy

#All models have a query attribute that is entry pt to run db queries
#query.all() returns all elements of this class
#query.get(primary key) returns that specific instance of the class
class User(UserMixin, db.Model):
    #automatically assigned id of the user. This is primary key for this model
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))

    #not actual database field, just a high-lvl view of relationship between users and posts
    #for a one-to-many relationship (one user, many posts), a db.relationship is usually defined on the "one" side
    #for example for a user u, u.posts will run a db query that returns all posts written by that user
    posts = db.relationship('Post', backref='author', lazy='dynamic') 
    #args: model class that reps "many" side, name of a field that will be added to objects of "many" class that pts back at the
    #"one" object (adds post.author expression in this case), how db query for the relationship will be used 

    #tells python how to print objects of this class (useful for debugging)
    def __repr__(self):
        return '<User {}>'.format(self.username)

    #function to set the user's password
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    #function to check the user's password with the previously generated hash
    def check_password(self, password):
        return check_password_hash(self.password_hash, password)


#A blog post
class Post(db.Model):
    #automatically assigned integer id of the post
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.String(140))

    #make timestamp indexed, in case we want to retrieve posts in chron order
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow) #pass utcnow fxn itself

    #foreignkey means this field references an id value from the users table
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return '<Post {}>'.format(self.body)


#user loading callback fxn for Flask-Login LoginManager. Can be called to load a user given the ID
@login.user_loader
def load_user(id):
    #return the User that has the passed ID
    return User.query.get(int(id))

   
