from flask import Blueprint, render_template, abort, request, redirect, url_for, flash
from jinja2 import TemplateNotFound
from applications.student_enrollments import model

""" 
  Citation for the following HTML:
  Date: 07/27/2022
  Flask Blueprints
  Source URL: https://hackersandslackers.com/flask-blueprints
"""
student_enrollments_bp = Blueprint('student_enrollments_bp', __name__, template_folder='templates')

@student_enrollments_bp.get('/student_enrollments')
def index():
  try:
    results = model.get()
    return render_template('student_enrollments.j2', student_enrollments=results)
  except TemplateNotFound:
    abort(404)


@student_enrollments_bp.post('/student_enrollments')
def new():
  s_id = request.form.get('student_id')
  c_id = request.form.get('course_id')
  if not (s_id.isnumeric() and c_id.isnumeric()):
    flash("Please provide valid Student ID and Course ID.")
  else:
    model.create(s_id, c_id)
  return redirect(url_for('student_enrollments_bp.index'))
  

@student_enrollments_bp.post("/student_enrollments/delete/<int:student_enrollment_id>")
def delete(student_enrollment_id):
  model.delete(student_enrollment_id)
  return redirect(url_for('student_enrollments_bp.index'))


@student_enrollments_bp.get('/student_enrollments/<int:student_enrollment_id>')
def edit(student_enrollment_id):
  return render_template('update.j2', student_enrollment_id=student_enrollment_id)
  

# TODO: Change post to PUT, need JS
@student_enrollments_bp.post('/student_enrollments/edit/<int:student_enrollment_id>')
def update(student_enrollment_id):
  is_enrolled = request.form.get('is_enrolled')
  certificate_id = request.form.get('certificate_id')

  if not is_enrolled.isnumeric():
    flash("Please provide a valid Enrollment Status")
  else:
    model.update(student_enrollment_id, is_enrolled, certificate_id)
  return redirect(url_for('student_enrollments_bp.index'))
