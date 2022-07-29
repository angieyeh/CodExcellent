from flask import redirect, request
import app_config

connection = app_config.db()

def get():
  query = """SELECT se.student_enrollment_id , st.student_id, st.name as student_name, co.course_id, co.course_name, co.start_date as course_start_date, co.end_date as course_end_date, se.is_enrolled, se.certificate_id 
    FROM Student_Enrollments se
    INNER JOIN Students st ON se.student_id = st.student_id
    INNER JOIN Courses co ON se.course_id = co.course_id;"""

  with connection.cursor() as cursor:
    cursor.execute(query)
    results = cursor.fetchall()
    return results


def create(student_id, course_id):
  with connection.cursor() as cursor:
    query = f"INSERT INTO Student_Enrollments (student_id, course_id ) VALUES (%s, %s)"
    cursor.execute(query, (int(student_id), int(course_id)))
    connection.commit()


def delete(student_enrollment_id):
  with connection.cursor() as cursor:
    query = """DELETE FROM Student_Enrollments 
            WHERE student_enrollment_id = '%s';"""
    cursor.execute(query, (int(student_enrollment_id)))
  connection.commit()
