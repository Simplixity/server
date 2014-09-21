from flask import Flask, jsonify, render_template, request

app = Flask(__name__)
app.config['SECRET_KEY'] = 'Insert_random_string_here'
app.config['SQLALCHEMY_ECHO'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'

app.config['WTF_CSRF_ENABLED'] = True

app.config['WTF_CSRF_SECRET_KEY'] = 'Insert_random_string_here'



import wtforms
import wtforms.validators as validators
from flask.ext.wtf import Form

class AppointmentForm(Form):

    first_name_field = wtforms.TextField(
            label="First Name",
            validators=[validators.Length(max=70), validators.Required()])
    last_name_field = wtforms.TextField(
            label="Last Name",
            validators=[validators.Length(max=70), validators.Required()])
    social_security_field = wtforms.TextField(
            label="Social Security Number",
            validators=[validators.Length(max=256), validators.Required()])

    condition_select_field = wtforms.SelectField(label="Condition", coerce=int)

import flask

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


@app.route('/doctor/<dr_id>')
def get_patients(dr_id):
    patients = {'test':'works'}
    '''patients = request.get_json()'''
    return flask.render_template(
        template_name_or_list='patients.html',
        dr_id=dr_id
    )

if __name__ == '__main__':
    app.run(debug=True)
