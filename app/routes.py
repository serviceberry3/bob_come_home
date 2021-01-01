#routes are diff URLs that app implements
#handlers for app routes are written as Python fxns, called view functions, which are mapped to one or more route URLs so
#Flask knows what logic to execute when a client requests a given URL 

#import the HTML template renderer. Jinja2 template engine subs {{ ... }} blocks with corresponding render_template() args
from flask import render_template


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


@app.route('/login')
def login():
    #instantiate new LoginForm
    form = LoginForm()
    return render_template('login.html', title='Sign In', form=form)

