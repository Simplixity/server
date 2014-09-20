"""Database population script

This is going to jam some sweet sweet data into your mongo.
"""

from pymongo import MongoClient

# Everyone's doing game of thrones these days...
sample_orgs = [{'name': 'The Wall',
                'address': [{
                    'street': '123 Wall Way',
                    'unit': 'Office of the Lord Commander',
                    'city': 'The North',
                    'state': 'KY',
                    'zip_code': '00000',
                    'country': 'Westeros'
                    }],
                'phones': ['555-555-5555', '555-555-5556'],
                'emails': ['enlist_now_no_questions_asked@the-wall.org']
                },
                {'name': 'Lanister Corp.',
                 'address': [{
                    'street': '123 Gold Rd.',
                    'city': 'Casterly Rock',
                    'state': 'KY',
                    'zip_code': '00000',
                    'country': 'Westeros'
                    }],
                'phones': ['555-555-5555', '555-555-5556'],
                'emails': ['cash-for-gold@casterlyrock.com']
                }]

sample_people = [
        {'last_name': 'Snow',
         'first_name': 'Jon',
         'address': [{
                    'street': '123 Wall Way',
                    'unit': 'Office of the Lord Commander',
                    'city': 'The North',
                    'state': 'KY',
                    'zip_code': '00000',
                    'country': 'Westeros'}],
         'birth_address': None,
         'social_scurity': 0,
         'race': 'white',
         'sex': 'male',
         'maritalStatus': 'single',
         'birthdate': '1994-01-01',
         'emails': ['jon.snow@the-wall.com'],
         'phones': ['555-555-5555']}
         ]


sample_users = [{'person': sample_people[0], 'employer': sample_orgs[0]}]


if __name__ == '__main__':
    print 'Simplixity Data Insertion'

    client = MongoClient()
    db = client['simplixity']
    person = db.person


    person.remove(None)
    result = person.insert(sample_people)
    print 'Inserted %s people' % len(result)

    user = db.user
    user.remove(None)
    result = user.insert(sample_users)
    print 'Inserted %s users' % len(result)



