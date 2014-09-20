class User (db.document):
    person = db.ReferenceField(Person)
    employer = db.ReferenceField(Organization)
    guardian = db.ReferenceField(Person)
    mother = db.ReferenceField(Person)
    father = db.ReferenceField(Person)
    emergency = db.ReferenceField(Person)

    religiousPreference = db.StringField(
        max_length=50
    )

    organDonor = db.BooleanField(
        required=True
    )

    conditions = db.EmbeddedDocumentField(condition)