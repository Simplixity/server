"""
address

Defines the Address class
"""


from simplixity import db

class Address(db.EmbeddedDocument):
    street = db.StringField()
    unit = db.StringField()
    city = db.StringField()
    state = db.StringField()
    zip_code = db.StringField()
    country = db.StringField()
