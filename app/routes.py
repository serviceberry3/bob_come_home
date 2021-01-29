#routes are diff URLs that app implements
#handlers for app routes are written as Python fxns, called view functions, which are mapped to one or more route URLs so
#Flask knows what logic to execute when a client requests a given URL 

#NOTE TO SELF: DO sudo supervisorctl reload to refresh site

#import the HTML template renderer. Jinja2 template engine subs {{ ... }} blocks with corresponding render_template() args
from flask import render_template, flash, redirect, request, url_for

from flask_login import current_user, login_user, logout_user, login_required
from app.models import User

from werkzeug.urls import url_parse

#import the Flask instance
from app import app, db

#import login form code
from app.forms import LoginForm, RegistrationForm

#decorators: these modify functions that follow it.
#creates assocition between URL given as argument, and the function (like callbacks)
#so the URLs / and /index will execute this fxn
@app.route('/')
@app.route('/index')
#login required to view this page, will redirect to login view fxn if not logged in
#@login_required
def index():
    #fake posts to show (list of dicts)
    posts = [
        {
            'author': {'username': 'Noah'},
            'body': 'Beautiful day in Indy!'
        },
        {
            'author': {'username': 'Bob'},
            'body': 'Hey, it\'s Bob! Rescue me from the warehouse!'
        }
    ]


    return render_template('index.html', title='Home', posts=posts)


#methods tells Flask that this view fxn accepts GET and POST requests (default is to accept only GET)
#GET: requests that return info to client (in this case, the browser)
#POST: requests used when broswer submits form data to server (GET can also be used for this, but not recommended)
@app.route('/login', methods=['GET', 'POST'])
def login():
    #if user is already logged in, return to home page
    if current_user.is_authenticated: #current_user var comes from Flask-Login, can be used at any time,
                                      #can be user object from db (read by Flask-Login thru user loader callback), or anonymous user
                                      #if not logged in yet
        return redirect(url_for('index'))

    #instantiate new LoginForm
    form = LoginForm()
    
    #validate/process the form. when browser sends GET rqst to receive the page w/the form, this will ret False,
    #so we jump to render_template
    #when browser sends POST rqst when user hits submit, this will gather all data, run attached validators, and ret True,
    #flashes message to user and goes back to homepage
    if form.validate_on_submit():
        #select users in db that have the passed username. First should hold the found user
        user = User.query.filter_by(username=form.username.data).first()

        #if user not in db or wrong password, flash error message and load login page again
        if user is None or not user.check_password(form.password.data): #take passwd hash stored w/user and determine if passwd entered matches
            flash('Invalid username or password')
            return redirect(url_for('login'))

        
        #log the user in: registers user as logged in, so any future pgs user navs to will have current_user var set to that user
        login_user(user, remember=form.remember_me.data)

        #see what next page is (the page that sent us to login if it denied access)
        #Flask provides requets var that contains all info that client sent with request. request.args exposes contents of query string in dict format
        next_page = request.args.get('next') #example URL /login?next=/index

        #if there was no access denial redirection in the first place, or if the next arg is a full URL (malicious), go back to homepage
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('index')



        #Flask stores the message, but flashed msgs won't automatically appear, need to render them in HTML template
        #flash('Login requested for user {}, remember_me = {}'.format(form.username.data, form.remember_me.data))

        #go to next page
        return redirect(next_page)

    #render login.html for user
    return render_template('login.html', title='Sign In', form=form)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))


#user registration view function
@app.route('/register', methods=['GET', 'POST'])
def register():
    #make sure user that invokes this route is not logged in already, if they are just go to home page
    if current_user.is_authenticated:
        return redirect(url_for('index'))

    #create new RegistrationForm()
    form = RegistrationForm()

    #originally returns false when browser sends GET rqst to receive the page with the form. So we get the template rendered
    #When it returns true on the POST request, we need to do the following
    if form.validate_on_submit():
        #add the user to the db
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()

        #display success message and go to login page
        flash('Congratulations, you are now a registered user!')
        return redirect(url_for('login'))

    #render register.html for user
    return render_template('register.html', title='Register', form=form)

@app.route('/memories')
def memories():
    return render_template('memories.html')

