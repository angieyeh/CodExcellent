from flask import Blueprint, render_template, abort, request, redirect, url_for, flash
from jinja2 import TemplateNotFound
from applications.students import students_model
from applications.instructors import instructors_model

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
        students = students_model.get()
        instructors = instructors_model.get()
        return render_template('students.j2', students=students, instructors=instructors)
    except TemplateNotFound:
        abort(404)


@students_bp.post('/students/edit/<int:student_id>')
def update(student_id):
    name = request.form.get('name')
    email = request.form.get('email')
    phone_number = request.form.get('phone_number')
    pronoun = request.form.get('pronoun')
    tutor_id = request.form.get('tutor_id')
    students_model.update(student_id, name, email, phone_number, pronoun, tutor_id)
    return redirect(url_for('students_bp.index'))


@students_bp.post('/students')
def new():
    name = request.form.get('name')
    email = request.form.get('email')
    phone_number = request.form.get('phone_number')
    pronoun = request.form.get('pronoun')
    tutor_id = request.form.get('instructor_id')
    if not name:
        flash("Please provide valid name.")
    if not email:
        flash("Please provide valid email.")
    else:
        students_model.create(name, email, phone_number, pronoun, tutor_id)
    return redirect(url_for('students_bp.index'))


@students_bp.get('/students/edit/<int:student_id>')
def edit(student_id):
    students = students_model.get_by(student_id)
    instructors = instructors_model.get()
    return render_template('edit.j2', students=students, instructors=instructors)

