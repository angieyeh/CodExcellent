from flask import redirect, request
import pymysql
import os

def create_connection():
    return pymysql.connect(host=os.environ.get('MYSQL_HOST'),
                            user=os.environ.get('MYSQL_USER'),
                            password=os.environ.get('MYSQL_PASSWORD') ,
                            database=os.environ.get('MYSQL_DB'),
                            cursorclass=pymysql.cursors.DictCursor)

def get():
  query = """SELECT se.student_enrollment_id, st.student_id, st.name as student_name, co.course_id, co.course_name, co.start_date as course_start_date, co.end_date as course_end_date, se.is_enrolled
    FROM Student_Enrollments se
    INNER JOIN Students st ON se.student_id = st.student_id
    INNER JOIN Courses co ON se.course_id = co.course_id;"""

  connection = create_connection()
  with connection.cursor() as cursor:
    cursor.execute(query)
    results = cursor.fetchall()
    cursor.close()
    connection.close()
    return results


def get_se_without_certs():
  # Date: 08/08/2022
  # Adapted from:
  # Source URL: https://stackoverflow.com/questions/4076098/how-to-select-rows-with-no-matching-entry-in-another-table

  query = """SELECT se.student_enrollment_id , st.student_id, st.name as student_name, co.course_id, co.course_name, co.start_date as course_start_date, co.end_date as course_end_date, se.is_enrolled
	FROM Student_Enrollments se
	INNER JOIN Students st ON se.student_id = st.student_id
	INNER JOIN Courses co ON se.course_id = co.course_id
    WHERE NOT EXISTS (SELECT * FROM Certificates cert WHERE cert.student_enrollment_id = se.student_enrollment_id);"""

  connection = create_connection()
  with connection.cursor() as cursor:
    cursor.execute(query)
    results = cursor.fetchall()
    cursor.close()
    connection.close()
    return results
  


def find_one(property, value):
  query = f"SELECT student_enrollment_id, student_id, course_id, is_enrolled FROM Student_Enrollments WHERE {property} = %s;"

  connection = create_connection()
  with connection.cursor() as cursor:
    cursor.execute(query, (value))
    results = cursor.fetchall()
    cursor.close()
    connection.close()
    return results


def create(student_id, course_id):
  connection = create_connection()
  with connection.cursor() as cursor:
    query = "INSERT INTO Student_Enrollments (student_id, course_id ) VALUES (%s, %s)"
    cursor.execute(query, (int(student_id), int(course_id)))
    connection.commit()
    connection.close()


def delete(student_enrollment_id):
  connection = create_connection()
  with connection.cursor() as cursor:
    query = """DELETE FROM Student_Enrollments 
                WHERE student_enrollment_id = %s;"""
    cursor.execute(query, (int(student_enrollment_id)))
    connection.commit()
    cursor.close()
    connection.close()


def update(student_enrollment_id, student_id, course_id, is_enrolled):
  connection = create_connection()
  with connection.cursor() as cursor:
    query = """UPDATE Student_Enrollments 
                SET student_id = %s, course_id = %s, is_enrolled = %s
                WHERE student_enrollment_id = %s;"""

    cursor.execute(query, (int(student_id), int(course_id), int(is_enrolled), int(student_enrollment_id)))
    connection.commit()
    cursor.close()
    connection.close()


def exists(student_id, course_id):
  query = """SELECT EXISTS(
                SELECT 1 FROM Student_Enrollments WHERE student_id = %s AND course_id = %s) 
              AS se_exists;"""

  connection = create_connection()
  with connection.cursor() as cursor:
    cursor.execute(query, (int(student_id), int(course_id)))
    results = cursor.fetchall()
    cursor.close()
    connection.close()
    return results

