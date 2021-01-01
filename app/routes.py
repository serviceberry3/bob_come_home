#routes are diff URLs that app implements
#handlers for app routes are written as Python fxns, called view functions, which are mapped to one or more route URLs so
#Flask knows what logic to execute when a client requests a given URL 

#import the HTML template renderer. Jinja2 template engine subs {{ ... }} blocks with corresponding render_template() args
from flask import render_template, flash, redirect


#import the Flask instance
from app import app

#import login form code
from app.forms import LoginForm

#decorators: these modify functions that follow it.
#creates assocition between URL given as argument, and the function (like callbacks)
#so the URLs / and /index will execute this fxn
@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Noah'}

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


    return render_template('index.html', title='Home', user=user, posts=posts)


#methods tells Fask that this view fxn accepts GET and POST requests (default is to accept only GET)
#GET: requests that return info to client (in this case, the browser)
#POST: requests used when broswer submits form data to server (GET can also be used for this, but not recommended)
@app.route('/login', methods=['GET', 'POST'])
def login():
    #instantiate new LoginForm
    form = LoginForm()
    
    #validate/process the form. when browser sends GET rqst to receive the page w/the form, this will ret False,
    #so we jump to render_template
    #when browser sends POST rqst when user hits submit, this will gather all data, run attached validators, and ret True,
    #flashes message to user and goes back to homepage
    if form.validate_on_submit():
        #Flask stores the message, but flashed msgs won't automatically appear, need to render them in HTML template
        flash('Login requested for user {}, remember_me = {}'.format(form.username.data, form.remember_me.data))

        #return to homepage
        return redirect('/index')

    #render login.html for user
    return render_template('login.html', title='Sign In', form=form)

