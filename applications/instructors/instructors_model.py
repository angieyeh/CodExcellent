import pymysql
import os

def create_connection():
    return pymysql.connect(host=os.environ.get('MYSQL_HOST'),
                            user=os.environ.get('MYSQL_USER'),
                            password=os.environ.get('MYSQL_PASSWORD') ,
                            database=os.environ.get('MYSQL_DB'),
                            cursorclass=pymysql.cursors.DictCursor)

def get():
  query = """SELECT instructor_id , name, email, phone_number, instructor_title, pronoun FROM Instructors;"""

  connection = create_connection()
  with connection.cursor() as cursor:
    cursor.execute(query)
    results = cursor.fetchall()
    return results
    cursor.close()
    connection.close()


def create(name, email, phone_number, instructor_title, pronoun):
  connection = create_connection()
  with connection.cursor() as cursor:
    query = f"INSERT INTO Instructors (name, email, phone_number, instructor_title, pronoun) VALUES (%s, %s, %s, %s, %s)"
    cursor.execute(query, (str(name), str(email), int(phone_number), str(instructor_title), str(pronoun)))
    connection.commit()
    connection.close()
