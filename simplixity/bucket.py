"""
The bucket.

The bucket is just a fancy dict that holds data and gets rid of it when someone
requests it.
"""

from simplixity.database import Person
from simplixity import db

class Bucket(dict):

    def __init__(self):
        people = Person.objects()

        self.target_systems = {}

        # populate some dummy data in the bucket
        p = Person()
        p.first_name = 'test'
        p.last_name = 'test test'

        self.target_systems['test_doctor_123'] = {}
        for p in people:
            self.target_systems['test_doctor_123'][str(p.id)] = p


    def put(self, target_system, user_id, data):
        if self.target_systems.get(target_system, None):
            self.target_systems[target_system][user_id] = data
        else:
            self.target_systems[target_system] = { user_id: data }

    def get(self, target_system, user_id):
        if self.target_systems.get(target_system, None):
            return self.target_systems[target_system].get(user_id, None)
        return None

    def get_patient_names(self, target_system):
        """Gets the patient names and IDs

        Returns a list of  dicts of patient IDs and names"""

        return self.target_systems.get(target_system, {})


