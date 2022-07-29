from flask import Blueprint, render_template, abort, request, redirect, url_for, flash
from jinja2 import TemplateNotFound
from applications.student_enrollments import model


student_enrollments_bp = Blueprint('student_enrollments_bp', __name__, template_folder='templates')

@student_enrollments_bp.get('/student_enrollments')
def index():
  try:
    results = model.get()
    return render_template('student_enrollments.j2', student_enrollments=results)
  except TemplateNotFound:
    abort(404)


@student_enrollments_bp.post('/student_enrollments')
def create():
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

  
   


