import pymysql
import app_config
import os

def create_connection():
    return pymysql.connect(host=os.environ.get('MYSQL_HOST'),
                            user=os.environ.get('MYSQL_USER'),
                            password=os.environ.get('MYSQL_PASSWORD') ,
                            database=os.environ.get('MYSQL_DB'),
                            cursorclass=pymysql.cursors.DictCursor)

def get():
  query = """SELECT student_id , name, email, phone_number, pronoun FROM Students;"""

  connection = create_connection()
  with connection.cursor() as cursor:
    cursor.execute(query)
    results = cursor.fetchall()
    return results
    cursor.close()
    connection.close()


def create(name, email, phone_number, pronoun):
  connection = create_connection()
  with connection.cursor() as cursor:
    query = f"INSERT INTO Students (name, email, phone_number, pronoun) VALUES (%s, %s, %s, %s)"
    cursor.execute(query, (str(name), str(email), int(phone_number), str(pronoun)))
    connection.commit()
    connection.close()