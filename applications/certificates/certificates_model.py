from datetime import datetime
import pymysql
import os
from datetime import datetime

def create_connection():
    return pymysql.connect(host=os.environ.get('MYSQL_HOST'),
                            user=os.environ.get('MYSQL_USER'),
                            password=os.environ.get('MYSQL_PASSWORD') ,
                            database=os.environ.get('MYSQL_DB'),
                            cursorclass=pymysql.cursors.DictCursor)

def get():
  query = """SELECT cert.certificate_id , st.name as student_name, co.course_name, cert.certificate_title, cert.issue_date 
	FROM Certificates cert
	INNER JOIN Student_Enrollments se ON cert.certificate_id = se.certificate_id
	INNER JOIN Students st ON se.student_id = st.student_id
	INNER JOIN Courses co ON se.course_id = co.course_id;"""

  connection = create_connection()
  with connection.cursor() as cursor:
    cursor.execute(query)
    results = cursor.fetchall()
    return results
    cursor.close()
    connection.close()


def create(certificate_title, issue_date):
  connection = create_connection()
  with connection.cursor() as cursor:
    query = f"INSERT INTO Certificates (certificate_title, issue_date) VALUES (%s, %s)"
    cursor.execute(query, (str(certificate_title), str(issue_date)))
    connection.commit()
    connection.close()
