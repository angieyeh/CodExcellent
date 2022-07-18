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


@app.route('/certificates')
def certificates():
    return render_template("certificates.j2")


@app.route('/students')
def students():
    return render_template("students.j2", students=sample_students)


@app.route('/instructors')
def instructors():
    return render_template("instructors.j2")


# sample data

sample_students = [
    {"student_id": "Thomas",
     "name": 33,
     "email": "New Mexico",
     "phone_number": "Blue",
     "pronoun": "Blue"
     },
    {
        "student_id": "Thomas",
        "name": 33,
        "email": "New Mexico",
        "phone_number": "Blue",
        "pronoun": "Blue"
    },
    {
        "student_id": "Thomas",
        "name": 33,
        "email": "New Mexico",
        "phone_number": "Blue",
        "pronoun": "Blue"
    },
    {
        "student_id": "Thomas",
        "name": 33,
        "email": "New Mexico",
        "phone_number": "Blue",
        "pronoun": "Blue"
    }]

# Listener
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 8888))

    app.run(port=port, debug=True)
