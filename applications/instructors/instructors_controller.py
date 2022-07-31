from flask import Blueprint, render_template, abort, request, redirect, url_for, flash
from jinja2 import TemplateNotFound
from applications.instructors import instructors_model

""" 
  Citation for the following HTML:
  Date: 07/27/2022
  Flask Blueprints
  Source URL: https://hackersandslackers.com/flask-blueprints
"""
instructors_bp = Blueprint('instructors_bp', __name__, template_folder='templates')

@instructors_bp.get('/instructors')
def index():
    try:
        results = instructors_model.get()
        return render_template('instructors.j2', instructors=results)
    except TemplateNotFound:
        abort(404)


@instructors_bp.post('/instructors')
def new():
    name = request.form.get('name')
    email = request.form.get('email')
    phone_number = request.form.get('phone_number')
    instructor_title = request.form.get('instructor_title')
    pronoun = request.form.get('pronoun')
    if not name:
        flash("Please provide valid name.")
    if not email:
        flash("Please provide valid email.")
    if not phone_number.isnumeric():
        flash("Please provide valid phone number.")
    else:
        instructors_model.create(name, email, phone_number, instructor_title, pronoun)
    return redirect(url_for('instructors_bp.index'))