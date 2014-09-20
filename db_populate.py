"""Database population script

This is going to jam some sweet sweet data into your mongo.
"""

from pymongo import MongoClient

sample_data = [
        {'last_name': 'Doe',
         'first_name': 'John',
         'email_address': 'john.doe@example.com',
         'home_phone': '555-555-5555',
         'work_phone': '555-555-1111'},
        {'last_name': 'out of ideas',
         'first_name': 'seriously',
         'email_address': 'barf@example.com',
         'home_phone': '555-555-2222',
         'work_phone': '555-555-1111'}]


if __name__ == '__main__':
    print 'Simplixity Data Insertion'

    client = MongoClient()
    db = client['simplixity']
    users = db.users

    # Delete all the current users and insert the dummy data
    users.remove(None)
    users.insert(sample_data)


