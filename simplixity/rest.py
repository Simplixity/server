"""
REST endpoints for Simplixity
"""

from simplixity import app
import simplixity.database
from flask import jsonify

import uuid



@app.route('/user', methods=['POST'])
def authorize():
    """This is a fake authorization method that the phone app calls
    to initiate logging in

    Returns a fake session ID.
    """
    return jsonify({'session_id': uuid.uuid4()})


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


