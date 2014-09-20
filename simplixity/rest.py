"""
REST endpoints for Simplixity
"""

from simplixity import app
from simplixity import db
from simplixity.database import User, Person, Organization

from flask import jsonify



import uuid


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


@app.route('/record', methods=['GET'])
def get_record():
    """Gets a record for a user.

    Returns a JSON object for a record"""
    return jsonify({'dummy_data': 'whatever'})


@app.route('/record', methods=['POST'])
def add_record():
    """Adds a record for a user.

    Returns the record ID"""
    return jsonify({'dummy_data': 'whatever'})


