import pymysql
import os

def create_connection():
    return pymysql.connect(host=os.environ.get('MYSQL_HOST'),
                            user=os.environ.get('MYSQL_USER'),
                            password=os.environ.get('MYSQL_PASSWORD') ,
                            database=os.environ.get('MYSQL_DB'),
                            cursorclass=pymysql.cursors.DictCursor)


def get():
  query = """SELECT Students.student_id , Students.name, Students.email, Students.phone_number, Students.pronoun, Students.tutor_id, Instructors.name as tutor_name
            FROM Students
            LEFT JOIN Instructors ON Students.tutor_id = Instructors.instructor_id;"""

  connection = create_connection()
  with connection.cursor() as cursor:
    cursor.execute(query)
    results = cursor.fetchall()
    cursor.close()
    connection.close()
    return results


def get_by(student_id):
  query = """SELECT Students.student_id , Students.name, Students.email, Students.phone_number, Students.pronoun, Students.tutor_id, Instructors.name as tutor_name
            FROM Students
            LEFT JOIN Instructors ON Students.tutor_id = Instructors.instructor_id
            WHERE Students.student_id = %s;"""

  connection = create_connection()
  with connection.cursor() as cursor:
    cursor.execute(query, int(student_id))
    results = cursor.fetchall()
    cursor.close()
    connection.close()
    return results


def create(name, email, phone_number, pronoun, tutor_id):
  connection = create_connection()
  with connection.cursor() as cursor:
    if phone_number == '' and pronoun == '' and tutor_id == '':
        query = f"INSERT INTO Students (name, email) VALUES (%s, %s)"
        cursor.execute(query, (str(name), str(email)))
    elif pronoun == '':
        query = f"INSERT INTO Students (name, email, phone_number, tutor_id) VALUES (%s, %s, %s, %s)"
        cursor.execute(query, (str(name), str(email), int(phone_number), int(tutor_id)))
    elif tutor_id == '':
        query = f"INSERT INTO Students (name, email, phone_number, pronoun) VALUES (%s, %s, %s, %s)"
        cursor.execute(query, (str(name), str(email), int(phone_number), str(pronoun)))
    elif phone_number == '':
        query = f"INSERT INTO Students (name, email, pronoun, tutor_id) VALUES (%s, %s, %s, %s, %s)"
        cursor.execute(query, (str(name), str(email), str(pronoun), int(tutor_id)))
    else:
        query = f"INSERT INTO Students (name, email, phone_number, pronoun, tutor_id) VALUES (%s, %s, %s, %s, %s)"
        cursor.execute(query, (str(name), str(email), int(phone_number), str(pronoun), int(tutor_id)))
    connection.commit()
    connection.close()


def update(student_id, name, email, phone_number, pronoun, tutor_id):
    connection = create_connection()
    with connection.cursor() as cursor:
        if tutor_id == '' and pronoun == '' and phone_number == '':
            query = """UPDATE Students SET name = %s, email = %s, phone_number = %s, pronoun = %s, tutor_id = %s 
            WHERE student_id = %s;"""
            new_values = (str(name), str(email), None, None, None, int(student_id))
        elif tutor_id == '':
            query = """UPDATE Students SET name = %s, email = %s, phone_number = %s, pronoun = %s, tutor_id = %s 
            WHERE student_id = %s;"""
            new_values = (str(name), str(email), int(phone_number), str(pronoun), None, int(student_id))
        elif pronoun == '':
            query = """UPDATE Students SET name = %s, email = %s, phone_number = %s, pronoun = %s, tutor_id = %s
                        WHERE student_id = %s;"""
            new_values = (str(name), str(email), int(phone_number), None, int(student_id))
        else:
            query = """UPDATE Students SET name = %s, email = %s, phone_number = %s, pronoun = %s, tutor_id = %s 
            WHERE student_id = %s;"""
            new_values = (str(name), str(email), int(phone_number), str(pronoun), int(tutor_id), int(student_id))
        cursor.execute(query, new_values)
        connection.commit()
        cursor.close()
        connection.close()
