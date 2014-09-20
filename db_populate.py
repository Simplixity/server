"""Database population script

This is going to jam some sweet sweet data into your mongo.
"""

from simplixity.database import Person, Address, User, Organization, Condition, Policy
from pymongo import MongoClient
import json
from faker import Faker
fake = Faker()

def make_fake_address():
    a = Address(street = fake.street_address(),
                         city = fake.city(),
                         state = fake.state(),
                         country = fake.country())
    return a

def make_fake_condition():
    c = Condition()
    c.type = 'allergy' if fake.boolean() else 'disease'
    c.code = '123456789'
    return c

def make_fake_policy():
    p = Policy()
    p.policy_id = '123456'
    p.payor_id = '1234567'
    p.group_id = '1234567'
    p.group_name = fake.company() + ' ' + fake.company_suffix()
    p.effective_start = fake.date()
    p.effective_end = fake.date()
    p.is_in_effect = fake.boolean()
    return p

def make_fake_people(number=10):

    result = []
    for i in xrange(number):
        p = Person()
        p.first_name = fake.first_name()
        p.last_name = fake.last_name()
        p.birth_date = fake.date()
        p.social_security = i
        p.emails = [fake.email()]
        p.sex = 'male' if fake.boolean() else 'female'
        p.marital_status = 'single' if fake.boolean() else 'single'
        p.religious_preference = 'unspecified'
        p.race = 'white'

        p.addresses = [ make_fake_address()]
        p.phones = [fake.phone_number(), fake.phone_number()]
        result.append(p)

    return result

def make_fake_org():
    o = Organization()
    o.name = fake.company()
    o.addresses = [make_fake_address()]
    o.phones = [fake.phone_number()]
    o.emails = [fake.email()]
    return o


if __name__ == '__main__':
    print 'Simplixity Data Insertion'

    client = MongoClient()
    db = client['simplixity']

    people = make_fake_people(10)
    person = db.person
    user = db.user
    organization = db.organization
    person.remove(None)
    user.remove(None)

    for p in people:

        policy = make_fake_policy()
        policy.save()

        o = make_fake_org()
        o.save()
        u = User(organ_donor = True)
        u.employer = o
        u.person = p
        u.conditions = [make_fake_condition()]
        u.policies = [policy]
        p.save()
        u.save(cascade=True)






