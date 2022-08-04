import pymysql
import os

def create_connection():
    return pymysql.connect(host=os.environ.get('MYSQL_HOST'),
                            user=os.environ.get('MYSQL_USER'),
                            password=os.environ.get('MYSQL_PASSWORD') ,
                            database=os.environ.get('MYSQL_DB'),
                            cursorclass=pymysql.cursors.DictCursor)


def get(active=None):
  query = "SELECT course_id, course_name, level, start_date, end_date, status FROM Courses;"

  connection = create_connection()
  with connection.cursor() as cursor:
    cursor.execute(query)
    results = cursor.fetchall()
    cursor.close()
    connection.close()
    return results


def find_by(property, value):
  query = f"SELECT course_id, course_name, level, start_date, end_date, status FROM Courses WHERE {property} = %s;"

  connection = create_connection()
  with connection.cursor() as cursor:
    cursor.execute(query, (value))
    results = cursor.fetchall()
    cursor.close()
    connection.close()
    return results


def create(course_name, level, start_date, end_date, status):
  connection = create_connection()
  with connection.cursor() as cursor:
    query = f"INSERT INTO Courses (course_name, level, start_date, end_date, status) VALUES (%s, %s, %s, %s, %s);"
    cursor.execute(query, (str(course_name), str(level), str(start_date), str(end_date), int(status)))
    connection.commit()
    connection.close()


def search(course_name):
  query = f"SELECT course_id, course_name, level, start_date, end_date, status FROM Courses WHERE course_name = %s;"

  connection = create_connection()
  with connection.cursor() as cursor:
    cursor.execute(query, str(course_name))
    results = cursor.fetchall()
    cursor.close()
    connection.close()
    return results
