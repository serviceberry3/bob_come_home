from flask import Flask

#create application obj as instance of class Flask
app = Flask(__name__) #name var is predefined, set to name of module in which it's used, used to load template files etc.

#the app package is defined by the app directory. Routes are the different URLs that the app implements
from app import routes