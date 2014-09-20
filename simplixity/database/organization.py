"""
organization

Defines the Organizatino class
"""

from simplixity import db

class Organization(db.EmbeddedDocument):

    name = db.StringField()
    addresses = db.ListField(db.EmbeddedDocumentField('Address'))
    phones = db.ListField(db.StringField())
    emails = db.ListField(db.StringField())

