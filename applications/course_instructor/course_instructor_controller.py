from flask import Blueprint, render_template, abort, request, redirect, url_for, flash
from jinja2 import TemplateNotFound
from applications.course_instructor import course_instructor_model
from applications.courses import courses_model
from applications.instructors import instructors_model

""" 
  Citation for the following HTML:
  Date: 07/27/2022
  Flask Blueprints
  Source URL: https://hackersandslackers.com/flask-blueprints
"""
course_instructor_bp = Blueprint('course_instructor_bp', __name__, template_folder='templates')


@course_instructor_bp.get('/course_instructor')
def index():
    try:
        courses = courses_model.get()
        instructors = instructors_model.get()
        course_instructor = course_instructor_model.get()
        return render_template(
            'course_instructor.j2',
            course_instructor=course_instructor,
            courses=courses,
            instructors=instructors)
    except TemplateNotFound:
        abort(404)


@course_instructor_bp.post('/course_instructor')
def new():
  i_id = request.form.get('instructor_id')
  c_id = request.form.get('course_id')
  print(i_id, c_id)
  if not (i_id.isnumeric() and c_id.isnumeric()):
    flash("Please provide valid Instructor ID and Course ID.")
  else:
    course_instructor_model.create(i_id, c_id)
  return redirect(url_for('course_instructor_bp.index'))