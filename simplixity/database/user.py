class User (db.document):
    person = db.ReferenceField(Person)
    employer = db.ReferenceField(Organization)
    guardian = db.ReferenceField(Person)
    mother = db.ReferenceField(Person)
    father = db.ReferenceField(Person)
    emergency = db.ReferenceField(Person)

    religious_preference = db.StringField(
        max_length=50
    )

    organ_donor = db.BooleanField(
        required=True
    )

    conditions = db.ListField(db.EmbeddedDocumentField('Condition'))

class Condition(db.EmbeddedDocument):
    type = db.StringField()
    code = db.StringField()