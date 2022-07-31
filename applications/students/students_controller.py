from flask import Blueprint, render_template, abort, request, redirect, url_for, flash
from jinja2 import TemplateNotFound
from applications.students import students_model

""" 
  Citation for the following HTML:
  Date: 07/27/2022
  Flask Blueprints
  Source URL: https://hackersandslackers.com/flask-blueprints
"""
students_bp = Blueprint('students_bp', __name__, template_folder='templates')

@students_bp.get('/students')
def index():
    try:
        results = students_model.get()
        return render_template('students.j2', students=results)
    except TemplateNotFound:
        abort(404)


@students_bp.post('/students')
def new():
    name = request.form.get('name')
    email = request.form.get('email')
    phone_number = request.form.get('phone_number')
    pronoun = request.form.get('pronoun')
    if not name:
        flash("Please provide valid name.")
    if not email:
        flash("Please provide valid email.")
    if not phone_number.isnumeric():
        flash("Please provide valid phone number.")
    else:
        students_model.create(name, email, phone_number, pronoun)
    return redirect(url_for('students_bp.index'))