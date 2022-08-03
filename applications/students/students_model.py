import pymysql
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
    cursor.close()
    connection.close()
    return results


def create(name, email, phone_number, pronoun):
  connection = create_connection()
  with connection.cursor() as cursor:
    if pronoun == '':
        query = f"INSERT INTO Students (name, email, phone_number) VALUES (%s, %s, %s)"
        cursor.execute(query, (str(name), str(email), int(phone_number)))
    else:
        query = f"INSERT INTO Students (name, email, phone_number, pronoun) VALUES (%s, %s, %s, %s)"
        cursor.execute(query, (str(name), str(email), int(phone_number), str(pronoun)))
    connection.commit()
    connection.close()
