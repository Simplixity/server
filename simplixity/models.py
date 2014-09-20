import datetime
from flask import url_for
from simplixity import db
from flask.ext.mongoengine.wtf import model_form

class User(db.Document):
    created_at = db.DateTimeField(default=datetime.datetime.now, required=True)
    email = db.StringField(required=True)
    first_name = db.StringField(max_length=50)
    last_name = db.StringField(max_length=50)

    meta = {
        'allow_inheritance': True,
        'indexes': ['-created_at', 'slug'],
        'ordering': ['-created_at']
    }

class Record(db.Document):
    created_at = db.DateTimeField(default=datetime.datetime.now, required=True)

