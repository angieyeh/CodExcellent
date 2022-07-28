from flask import Blueprint, render_template, abort
from jinja2 import TemplateNotFound
from applications.student_enrollments import model


student_enrollments_bp = Blueprint('student_enrollments_bp', __name__, template_folder='templates')

@student_enrollments_bp.get('/student_enrollments')
def index():
  try:
    results = model.get()
    print(results)
    return render_template('student_enrollments.j2', student_enrollments=results)
  except TemplateNotFound:
    abort(404)
