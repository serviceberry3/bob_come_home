#top-level Python script that defines Flask application instance


#import application instance
from app import app, db
from app.models import User, Post

#this decorator registers the fxn as a shell context fxn. When flask shell command runs, it'll invoke this fxn and register
#the items returned by it in the shell session
@app.shell_context_processor
def make_shell_context():
    #must provide a name for each item
    return {'db': db, 'User': User, 'Post': Post}
