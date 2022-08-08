from flask import Blueprint, render_template, abort, request, redirect, url_for, flash
from jinja2 import TemplateNotFound
from applications.certificates import certificates_model
from datetime import datetime

""" 
  Citation for the following HTML:
  Date: 07/27/2022
  Flask Blueprints
  Source URL: https://hackersandslackers.com/flask-blueprints
"""
certificates_bp = Blueprint('certificates_bp', __name__, template_folder='templates')

@certificates_bp.get('/certificates')
def index():
    try:
        results = certificates_model.get()
        return render_template(
                'certificates.j2',
                certificates=results,
                table_headers=['certificate_id', 'student_name', 'course_name', 'certificate_title', 'issue_date'])
    except TemplateNotFound:
        abort(404)


@certificates_bp.post('/certificates')
def new():
    certificate_title = request.form.get('certificate_title')
    # issue_date = datetime.strptime(request.form.get('issue_date'), '%Y-%m-%d')
    issue_date = request.form.get('issue_date')
    if not certificate_title:
        flash("Please provide title.")
    if not issue_date:
        flash("Please provide issue date.")
    else:
        certificates_model.create(certificate_title, issue_date)
    return redirect(url_for('certificates_bp.index'))