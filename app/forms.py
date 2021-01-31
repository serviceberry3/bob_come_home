from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo
from app.models import User

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')

class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])

    #ensure email matches general structure of an email address
    email = StringField('Email', validators=[DataRequired(), Email()])


    password = PasswordField('Password', validators=[DataRequired()])

    #make sure this password matches first
    password2 = PasswordField('Enter password again', validators=[DataRequired(), EqualTo('password')])


    submit = SubmitField('Register')


    # When you add any methods that match pattern validate_<field_name>, WTForms invokes them in addition to stock validators. 

    def validate_username(self, username):
        #query the db for this username to make sure this user doesn't already exist
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            #add this message to the errors for username field
            raise ValidationError('User already exists. Please use a different username.')


    def validate_email(self, email):
        #query the db for this email address
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            #add this message to the errors for email field
            raise ValidationError('User with this email already exists. Please use a different email address.')