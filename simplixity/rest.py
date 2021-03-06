"""
REST endpoints for Simplixity
"""

from simplixity import fields
from simplixity import app
from simplixity import db
from simplixity.bucket import Bucket
from simplixity.database import User, Person, Organization, Policy

from mongoengine.base import ValidationError

from flask import jsonify, render_template, request, g
import json
import uuid

bucket = Bucket()
stored_person = None

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
    global stored_person
    incoming_json = request.get_json()
    print incoming_json
    target_id = incoming_json['target_system_id']
    user_id = incoming_json['username']

    # find our  user data and put it in the bucket
    try:
        u = User.objects(pk=user_id)[0]
        p = Person.objects(pk=user_id)[0]
        print u
        print p
        stored_person = p
        bucket.put(target_id, user_id, p)
    except ValidationError:
        return jsonify({'acknowledgement': False, 'message': 'Could not find user with ID %s' % user_id})

    return jsonify({'acknowledgement': True, 'messsage': 'Sending data to target %s' % target_id})



@app.route('/response', methods=['POST'])
def process_info_response():
    incoming_json = request.get_json()
    return jsonify({'status': 'Success', 'fields_sent': incoming_json})

@app.route('/patient/<target_id>', methods=['GET'])
def get_patient_list(target_id):
    result = bucket.get_patient_names(target_id)
    return jsonify(result)


@app.route('/patient/<target_id>/<patient_id>', methods=['POST'])
def get_patient(target_id, patient_id):
    incoming_json = request.get_json()
    fields = ['asdf']
    return jsonify({'acknowledge': True, 'message': 'Sending fields to user for approval'})


from time import sleep
@app.route('/poll', methods=['GET', 'POST'])
def long_poll():
    sleep(5)
    return json.dumps(['Personal', 'Employer', 'Mother', 'Father',
        'Guardian', 'Emergency', 'Medical Insurance', 'Medical Conditions'])


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
    global stored_person
    if stored_person:
        return stored_person.to_json()
    else:
        return jsonify({})

    #return Person.objects(pk=person_id).to_json()
    # return stored_person


@app.route('/policy/<policy_id>', methods=['GET'])
def get_policy(policy_id):
    return Policy.objects(pk=policy_id).to_json()




