"""
REST endpoints for Simplixity
"""

from simplixity import app
from simplixity import db
from simplixity.bucket import Bucket
from simplixity.database import User, Person, Organization, Policy

from flask import jsonify, render_template, request

import uuid

bucket = Bucket()

### the important API calls
@app.route('/authentication', methods=['POST'])
def authenticate():
    try:
        incoming_json = request.get_json(force=True)
        print incoming_json
    except Exception as e:
        print e
    return jsonify({'session_id': uuid.uuid4()})

@app.route('/handshake', methods=['POST'])
def handshake():
    # put some data in the bucket
    return jsonify({'acknowledgement': True})

@app.route('/response', methods=['POST'])
def process_info_response():
    incoming_json = request.get_json()
    return jsonify({'status': 'Success', 'fields_sent': incoming_json})

@app.route('/patient/<target_id>', methods=['GET'])
def get_patient_list(target_id):
    result = bucket.get_patient_names(target_id)
    return jsonify(result)

@app.route('/patient/<target_id>/<patient_id>', methods=['GET'])
def get_patient(target_id, patient_id):
    data = bucket.get(target_id, patient_id)
    print data.to_json()
    return data.to_json()



@app.route('/api', methods=['GET'])
def api_help():
    return render_template('api.html')

@app.route('/user', methods=['GET'])
def get_user():
    """Lets make a method that gets all the users"""
    return User.objects.to_json()

@app.route('/user/<user_id>')
def get_single_user(user_id):
    return User.objects(pk=user_id).to_json()


@app.route('/user', methods=['POST'])
def authorize():
    """This is a fake authorization method that the phone app calls
    to initiate logging in

    Returns a user and a fake session ID
    """
    user = User.objects.all()[0]
    return jsonify({'session_id': uuid.uuid4(), 'user': user})

def recover_password():
    pass

@app.route('/register', methods=['POST'])
def register():
    pass

@app.route('/person/<person_id>', methods=['GET'])
def get_person(person_id):
    return Person.objects(pk=person_id).to_json()


@app.route('/policy/<policy_id>', methods=['GET'])
def get_policy(policy_id):
    return Policy.objects(pk=policy_id).to_json()




