from simplixity import db
from datetime import datetime

class Person(db.Document):

    created_at = db.DateTimeField(
        default=datetime.now,
        required=True
    )

    first_name = db.StringField(
        max_length=50
    )

    last_name = db.StringField(
        max_length=50
    )

    addresses = db.ListField(db.EmbeddedDocumentField('Address'))

    birth_address = db.EmbeddedDocumentField('Address')

    social_security = db.IntField(
        required=True,
        unique=True,
        max_value=999999999
    )

    sex = db.StringField()

    martial_status = db.StringField()

    race = db.StringField()

    birth_date = db.DateTimeField(
        required=True
    )

    emails = db.ListField(db.EmailField(
        max_length=100,
        required=True,
        unique=True
    ))

    home_phone = db.StringField(
        max_length=15
    )

    work_phone = db.StringField(
        max_length=15
    )

    meta = {
        'allow_inheritance': True,
        'indexes': ['social_security'],
    }

    def __unicode__(self):
        return u'%s %s %s' % self.first_name, self.last_name (self.email)
