from flask import Blueprint, render_template, abort, request, redirect, url_for, flash
from jinja2 import TemplateNotFound
from applications.student_enrollments import model
from applications.students import students_model
from applications.courses import courses_model

""" 
  Citation for the following HTML:
  Date: 07/27/2022
  Flask Blueprints
  Source URL: https://hackersandslackers.com/flask-blueprints
"""
student_enrollments_bp = Blueprint(
                          'student_enrollments_bp', 
                          __name__, 
                          template_folder='templates',
                          static_folder='static',
                          static_url_path='/applications/student_enrollments/static'
                        )

@student_enrollments_bp.get('/student_enrollments')
def index():
  try:
    student_enrollments = model.get()
    students = students_model.get()
    courses = courses_model.find_by('status', 1)
    return render_template(
            'student_enrollments.j2', 
            student_enrollments=student_enrollments,
            students=students,
            courses=courses,
            modal_title='Student Enrollments',
            modal_body='Are you sure you want to delete this student enrollment?')
  except TemplateNotFound:
    abort(404)


@student_enrollments_bp.post('/student_enrollments')
def new():
  s_id = request.form.get('student_id')
  c_id = request.form.get('course_id')
  print(s_id, c_id)
  if not (s_id.isnumeric() and c_id.isnumeric()):
    flash("Please provide valid Student ID and Course ID.")
  else:
    model.create(s_id, c_id)
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


@student_enrollments_bp.delete("/student_enrollments/<int:student_enrollment_id>")
def delete(student_enrollment_id):
  print(student_enrollment_id)
  model.delete(student_enrollment_id)
  return {student_enrollment_id: student_enrollment_id}
