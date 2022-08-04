import pymysql
import os

def create_connection():
    return pymysql.connect(host=os.environ.get('MYSQL_HOST'),
                            user=os.environ.get('MYSQL_USER'),
                            password=os.environ.get('MYSQL_PASSWORD') ,
                            database=os.environ.get('MYSQL_DB'),
                            cursorclass=pymysql.cursors.DictCursor)


def get(active=None):
  query = """SELECT Course_Instructors.course_id, Courses.course_name, Course_Instructors.instructor_id, Instructors.name, Instructors.instructor_title
        FROM Course_Instructors
        JOIN Courses ON Course_Instructors.course_id = Courses.course_id
        JOIN Instructors ON Course_Instructors.instructor_id = Instructors.instructor_id;"""

  connection = create_connection()
  with connection.cursor() as cursor:
    cursor.execute(query)
    results = cursor.fetchall()
    cursor.close()
    connection.close()
    return results


def create(instructor_id, course_id):
  connection = create_connection()
  with connection.cursor() as cursor:
    query = "INSERT INTO Course_Instructors (instructor_id, course_id ) VALUES (%s, %s)"
    cursor.execute(query, (int(instructor_id), int(course_id)))
    connection.commit()
    connection.close()