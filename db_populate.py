"""Database population script

This is going to jam some sweet sweet data into your mongo.
"""

from pymongo import MongoClient

# Everyone's doing game of thrones these days...
sample_data = [
        {'last_name': 'Snow',
         'first_name': 'Jon',
         'email_address': 'jon.snow@the-wall.com',
         'home_phone': '555-555-5555',
         'work_phone': '555-555-1111'},
        {'last_name': 'Tarly',
         'first_name': 'Samwell',
         'email_address': 'samwell.tarly@the-wall.com',
         'home_phone': '555-555-2222',
         'work_phone': '555-555-1111'},
        {'last_name': 'Baratheon',
         'first_name': 'Joffrey',
         'email_address': 'king_4_life@castelyrock.com',
         'home_phone': '555-555-5555',
         'work_phone': '555-555-1234'},
        {'last_name': 'Baelish',
         'first_name': 'Petry',
         'email_address': 'littlefinger@vale.biz',
         'home_phone': '555-555-2222',
         'work_phone': '555-555-4321'},
        {'last_name': 'Lannister',
         'first_name': 'Tyrion',
         'email_address': 'impin_aint_easy@castelyrock.com',
         'home_phone': '555-555-5555',
         'work_phone': '555-555-8888'}]


if __name__ == '__main__':
    print 'Simplixity Data Insertion'

    client = MongoClient()
    db = client['simplixity']
    users = db.users

    # Delete all the current users and insert the dummy data
    users.remove(None)
    result = users.insert(sample_data)
    print 'Inserted %s users' % len(result)



