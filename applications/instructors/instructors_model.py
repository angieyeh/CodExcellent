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
    cursor.close()
    connection.close()
    return results


def create(name, email, phone_number, instructor_title, pronoun):
  connection = create_connection()
  with connection.cursor() as cursor:
    if pronoun == '' and phone_number == '':
        query = f"INSERT INTO Instructors (name, email, instructor_title) VALUES (%s, %s, %s)"
        cursor.execute(query, (str(name), str(email), str(instructor_title)))
    elif pronoun == '':
        query = f"INSERT INTO Instructors (name, email, phone_number, instructor_title) VALUES (%s, %s, %s, %s)"
        cursor.execute(query, (str(name), str(email), int(phone_number), str(instructor_title)))
    elif phone_number == '':
        query = f"INSERT INTO Instructors (name, email, instructor_title, pronoun) VALUES (%s, %s, %s, %s)"
        cursor.execute(query, (str(name), str(email), str(instructor_title), str(pronoun)))
    else:
        query = f"INSERT INTO Instructors (name, email, phone_number, instructor_title, pronoun) VALUES (%s, %s, %s, %s, %s)"
        cursor.execute(query, (str(name), str(email), int(phone_number), str(instructor_title), str(pronoun)))
    connection.commit()
    connection.close()
        

def delete(instructor_id):
  connection = create_connection()
  with connection.cursor() as cursor:
    query = "DELETE FROM Instructors WHERE instructor_id = %s;"
    cursor.execute(query, (int(instructor_id)))
    connection.commit()
    cursor.close()
    connection.close()