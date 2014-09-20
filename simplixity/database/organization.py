"""
organization

Defines the Organizatino class
"""

from simplixity import db

class Organization(db.EmbeddedDocument):

    name = db.StringField()

