from flask import Blueprint, render_template, abort, request, redirect, url_for, flash
from jinja2 import TemplateNotFound
from applications.certificates import certificates_model
from applications.student_enrollments import model
from datetime import datetime
from dateutil.parser import parser

""" 
  Citation for the following Flask Blueprints:
  Date: 07/27/2022
  Adapted from:
  Source URL: https://hackersandslackers.com/flask-blueprints
"""
certificates_bp = Blueprint('certificates_bp', __name__, template_folder='templates')

@certificates_bp.get('/certificates')
def index():
    try:
        results = certificates_model.get()
        se_res = model.get_se_without_certs()
        return render_template(
                'certificates.j2',
                certificates=results,
                student_enrollments=se_res,
                table_headers=['certificate_id', 'student_name', 'course_name', 'certificate_title', 'issue_date', 'student_enrollment_id'])
    except TemplateNotFound:
        abort(404)


@certificates_bp.post('/certificates')
def new():
    certificate_title = request.form.get('certificate_title')
    issue_date = request.form.get('issue_date')
    se_id = request.form.get('student_enrollment_id')
    student_enrollment_id = request.form.get('student_enrollment_id')
    if not certificate_title:
        flash("Please provide a valid certificate title.")
    elif not (issue_date and is_valid(issue_date)):
        flash("Please provide a valid issue date.")
    elif not se_id.isnumeric():
        flash("Please provide a valid Student Enrollment ID.")
    else:
        # Citation for the date conversion: 
        # Date: 08/08/2022
        # Copied from:
        # Source URL: https://stackoverflow.com/questions/18039680/django-get-only-date-from-datetime-strptime
        issue_date = datetime.strptime(request.form.get('issue_date'), '%Y-%m-%d').date()
        certificates_model.create(certificate_title, issue_date, se_id)
    return redirect(url_for('certificates_bp.index'))


# Citation for the date validation: 
# Date: 08/08/2022
# Adapted from:
# Source URL: https://stackoverflow.com/questions/25341945/check-if-string-has-date-any-format
def is_valid(date):
    valid = None
    try:
        parser(date)
        valid = True
    except ValueError:
        valid = False
    return valid
    