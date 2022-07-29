from flask import redirect, request
import app_config
import os

def create_connection():
    return pymysql.connect(host=os.environ.get('MYSQL_HOST'),
                            user=os.environ.get('MYSQL_USER'),
                            password=os.environ.get('MYSQL_PASSWORD') ,
                            database=os.environ.get('MYSQL_DB'),
                            cursorclass=pymysql.cursors.DictCursor)

def get():
  query = """SELECT se.student_enrollment_id , st.student_id, st.name as student_name, co.course_id, co.course_name, co.start_date as course_start_date, co.end_date as course_end_date, se.is_enrolled, se.certificate_id 
    FROM Student_Enrollments se
    INNER JOIN Students st ON se.student_id = st.student_id
    INNER JOIN Courses co ON se.course_id = co.course_id;"""

  connection = create_connection()
  with connection.cursor() as cursor:
    cursor.execute(query)
    results = cursor.fetchall()
    return results
    cursor.close()
    connection.close()


def create(student_id, course_id):
  connection = create_connection()
  with connection.cursor() as cursor:
    query = f"INSERT INTO Student_Enrollments (student_id, course_id ) VALUES (%s, %s)"
    cursor.execute(query, (int(student_id), int(course_id)))
    connection.commit()
    connection.close()


def delete(student_enrollment_id):
  connection = create_connection()
  with connection.cursor() as cursor:
    query = """DELETE FROM Student_Enrollments 
            WHERE student_enrollment_id = '%s';"""
    cursor.execute(query, (int(student_enrollment_id)))
    connection.commit()
    cursor.close()
    connection.close()


def update(student_enrollment_id, is_enrolled, certificate_id):
  connection = create_connection()
  with connection.cursor() as cursor:
    if certificate_id == '': 
      query = f"UPDATE Student_Enrollments SET is_enrolled = %s WHERE student_enrollment_id = %s;"
      cursor.execute(query, (int(is_enrolled), int(student_enrollment_id)))
    else:
      query = f"UPDATE Student_Enrollments SET is_enrolled = %s, certificate_id = %s WHERE student_enrollment_id = %s;"
      cursor.execute(query, (int(is_enrolled), int(certificate_id), int(student_enrollment_id)))
    connection.commit()
    cursor.close()
    connection.close()
