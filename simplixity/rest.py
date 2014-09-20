"""
REST endpoints for Simplixity
"""

from simplixity import app
from simplixity import db
from simplixity.database import User, Person, Organization, Policy

from flask import jsonify, render_template



import uuid

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

def register():
    pass

@app.route('/person/<person_id>', methods=['GET'])
def get_person(person_id):
    return Person.objects(pk=person_id).to_json()


@app.route('/policy/<policy_id>', methods=['GET'])
def get_policy(policy_id):
    return Policy.objects(pk=policy_id).to_json()




