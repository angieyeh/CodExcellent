from flask import Blueprint, render_template, abort, request, redirect, url_for, flash
from jinja2 import TemplateNotFound
from applications.courses import courses_model

""" 
  Citation for the following HTML:
  Date: 07/27/2022
  Flask Blueprints
  Source URL: https://hackersandslackers.com/flask-blueprints
"""
courses_bp = Blueprint('courses_bp', __name__, template_folder='templates')

@courses_bp.get('/courses')
def index():
    try:
        results = courses_model.get()
        return render_template(
                    'courses.j2',
                    courses=results,
                    table_headers=['course_id',	'course_name', 'level',	
                    'start_date', 'end_date', 'status'])
    except TemplateNotFound:
        abort(404)


@courses_bp.post('/courses/search')
def search():
    course_name = request.form.get('course_name')
    results = courses_model.search(course_name)
    if not results:
        flash("Courses Not Found")
    return render_template('courses.j2', courses=results)


@courses_bp.post('/courses')
def new():
    course_name = request.form.get('course_name')
    level = request.form.get('level')
    start_date = request.form.get('start_date')
    end_date = request.form.get('end_date')
    status = request.form.get('status')
    if not course_name:
        flash("Please provide valid course title.")
    if not start_date or not end_date:
        flash("Please provide start and end dates.")
    if not level:
        flash("Please provide valid level for the course.")
    else:
        courses_model.create(course_name, level, start_date, end_date, status)
    return redirect(url_for('courses_bp.index'))