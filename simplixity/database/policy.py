"""
policy

This module defines the Policy class
"""

from simplixity import db

class Policy(db.Document):

    type = db.StringField()
    policy_id = db.StringField()
    payor_id = db.StringField()
    group_id = db.StringField()
    group_name = db.StringField()

    effectiveStart = db.DateTimeField()
    effectiveEnd = db.DateTimeField()

    is_in_effect = db.BoolField()

