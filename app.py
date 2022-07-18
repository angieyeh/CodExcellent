# Citation for the following phone numbers:
# Date: 07/17/2022
# Source URL: https://github.com/osu-cs340-ecampus/flask-starter-app

from flask import Flask, render_template
import os

# Configuration

app = Flask(__name__)


# Routes

@app.route('/')
def root():
    return render_template("main.j2")


@app.route('/students')
def students():
    return render_template("students.j2", students=sample_students)


@app.route('/student_enrollments')
def student_enrollments():
  return render_template("student_enrollments.j2")


@app.route('/instructors')
def instructors():
    return render_template("instructors.j2", instructors=sample_instructors)


@app.route('/courses')
def courses():
    return render_template("courses.j2")


@app.route('/course_instructor')
def course_instructor():
    return render_template("course_instructor.j2")


@app.route('/certificates')
def certificates():
    return render_template("certificates.j2")

# sample data


sample_students = [
    {"student_id": 1,
     "name": "Chloe Decker",
     "email": "chloedecker@gmail.com",
     "phone_number": "2025550108",
     "pronoun": "she/her"
     },
    {
        "student_id": 2,
        "name": "Ella Lopez",
        "email": "ellalopez@gmail.com",
        "phone_number": "2025550185",
        "pronoun": "she/her"
    },
    {
        "student_id": 3,
        "name": "Dan Espinoza",
        "email": "danespinoza@gmail.com",
        "phone_number": "2025550114",
        "pronoun": "he/him"
    },
    {
        "student_id": 4,
        "name": "Rory Gilmore",
        "email": "rorygilmore@gmail.com",
        "phone_number": "2025555514",
        "pronoun": None
    }]


sample_instructors = [
    {"instructor_id": 1,
     "name": "Charlotte Charles",
     "email": "charlottecharles@gmail.com",
     "instructor_title": "Teacher",
     "phone_number": "2025550109",
     "pronoun": "she/her"
     },
    {
        "instructor_id": 2,
        "name": "Cosima Niehaus",
        "email": "cosima@gmail.com",
        "phone_number": "2025550111",
        "instructor_title": "Teacher",
        "pronoun": None
    },
    {
        "instructor_id": 3,
        "name": "Donny Hendrix",
        "email": "donnyhendrix@gmail.com",
        "phone_number": "2025550110",
        "instructor_title": "Teacher",
        "pronoun": None
    },
    {
        "instructor_id": 4,
        "name": "Robin Scherbatsky",
        "email": "robinscherbatsky@gmail.com",
        "phone_number": "2025550111",
        "instructor_title": "Teaching Assistant",
        "pronoun": None
    }]

# Listener
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 8888))

    app.run(port=port, debug=True)
