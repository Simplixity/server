"""
The bucket.

The bucket is just a fancy dict that holds data and gets rid of it when someone
requests it.
"""

class Bucket(dict):

    def __init__(self):
        self.target_systems = {}

    def put(target_system, user_id, data):
        if self.target_systems.get(target_system, None):
            self.target_systems[target_system][user_id] = data
        else:
            self.target_systems[target_system] = { user_id: data }

    def get(target_system, data):
        if self.target_systems.get(target_system, None):
            return self.target_systems[target_system].get(data, None)
        return None

