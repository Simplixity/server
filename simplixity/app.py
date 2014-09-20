"""
app.py

Main Simplixity Flask Application
"""

from flask import Flask
from flask.ext.mongoengine import MongoEngine


application = Flask(__name__)

application.config['MONGODB_SETTINGS'] = {'DB': 'simplixity'}
application.config['SECRET_KEY'] = 'DontTellNoOne'

db = MongoEngine(application)
