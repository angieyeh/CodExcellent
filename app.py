# Citation for the following phone numbers:
# Date: 07/17/2022
# Source URL: https://github.com/osu-cs340-ecampus/flask-starter-app

from flask import Flask, render_template
import os
import app_config

# Configuration

app = app_config.application()


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
    return render_template("courses.j2", courses=sample_courses)


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


sample_courses = [
    {
        "course_id": 1,
        "course_name": "Intro to Programming",
        "level": "beginner",
        "start_date": "2022-01-09",
        "end_date": "2022-10-17",
        "status": 1
    },
    {
        "course_id": 2,
        "course_name": "Intro to HTML/CSS and Javascript",
        "level": "beginner",
        "start_date": "2020-01-09",
        "end_date": "2020-03-17",
        "status": 1
    },
    {
        "course_id": 3,
        "course_name": "Intro to Python",
        "level": "beginner",
        "start_date": "2022-05-09",
        "end_date": "2023-07-17",
        "status": 1
    },
    {
        "course_id": 4,
        "course_name": "Data Structures",
        "level": "intermediate",
        "start_date": "2022-05-09",
        "end_date": "2023-07-17",
        "status": 0
    }
]

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 8281))

    app.run(port=port, debug=True)
