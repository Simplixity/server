from datetime import datetime
from flask import url_for
from simplixity import db
from flask.ext.mongoengine.wtf import model_form

class User(db.Document):
    created_at = db.DateTimeField(
        default=datetime.now,
        required=True
    )

    email = db.EmailField(
        verbose_name=u'e-mail',
        max_length=100,
        required=True,
        unique=True
    )

    first_name = db.StringField(
        verbose_name=u'fname',
        max_length=50
    )

    last_name = db.StringField(
        verbose_name=u'lname',
        max_length=50
    )

    home_phone = db.StringField(
        verbose_name=u'homephone',
        max_length=15
    )

    work_phone = db.StringField(
        verbose_name=u'homephone',
        max_length=15
    )

    """is_active = db.BooleanField(
        verbose_name=u'active',
        default=True,
        required=True
    )

    last_login = db.DateTimeField(
        verbose_name=u'ultimo login',
        required=False
    )"""

    meta = {
        'allow_inheritance': True,
        'indexes': ['email'],
    }

    def __unicode__(self):
        return u'%s %s %s' % self.first_name, self.last_name (self.email)

    """def refresh_last_login(self):
        self.last_login = datetime.now()
        self.save()"""

class Record(db.Document):
    created_at = db.DateTimeField(
        default=datetime.now,
        required=True
    )
