"""
organization

Defines the Organizatino class
"""

from simplixity import db

class Organization(db.Document):

    name = db.StringField(primary_key=True)
    addresses = db.ListField(db.EmbeddedDocumentField('Address'))
    phones = db.ListField(db.StringField())
    emails = db.ListField(db.StringField())


# my test data is unemployed


