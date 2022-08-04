# Citation for the following phone numbers:
# Date: 07/17/2022
# Source URL: https://github.com/osu-cs340-ecampus/flask-starter-app

from flask import Flask, render_template
import os

# Configuration

app = Flask(__name__, static_folder='static', template_folder='templates')
app.secret_key = "super duper secret key"

# Blueprints

from applications.student_enrollments import controller
app.register_blueprint(controller.student_enrollments_bp)

from applications.students import students_controller
app.register_blueprint(students_controller.students_bp)

from applications.instructors import instructors_controller
app.register_blueprint(instructors_controller.instructors_bp)

from applications.certificates import certificates_controller
app.register_blueprint(certificates_controller.certificates_bp)

from applications.courses import courses_controller
app.register_blueprint(courses_controller.courses_bp)

from applications.course_instructor import course_instructor_controller
app.register_blueprint(course_instructor_controller.course_instructor_bp)


# HomePage
@app.route('/')
def root():
    return render_template("main.j2")


# Listener
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 8281))

    app.run(port=port, debug=True)
