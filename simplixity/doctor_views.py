import flask
from flask import request
from simplixity import app

@app.route('/doctor/<dr_id>/<patient_id>')
def patient_detail(dr_id, patient_id):
    return flask.render_template(
        template_name_or_list='requestinfo.html',
        dr_id=dr_id, patient_id=patient_id)

@app.route('/', methods=['GET', 'POST'])
def login():
    if flask.request.method == 'POST':
        flask.flash("Successfully logged in!")
        return flask.redirect(flask.url_for(
            'get_patients',dr_id=request.form['doctorid']))
    return flask.render_template(
            template_name_or_list='login.html')

@app.route('/registration')
def registration():
    return flask.render_template('registration_form.html')

@app.route('/doctor/<dr_id>')
def get_patients(dr_id):
    patients = {'test':'works'}
    '''patients = request.get_json()'''
    return flask.render_template(
        template_name_or_list='patients.html',
        dr_id=dr_id
    )
