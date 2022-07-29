import pymysql
import pymysql.cursors
import app_config

mysql = app_config.db()

def get():
  cur = mysql
  query = """SELECT se.student_enrollments_id , st.student_id, st.name as student_name, co.course_id, co.course_name, co.start_date as course_start_date, co.end_date as course_end_date, se.is_enrolled, se.certificate_id 
    FROM Student_Enrollments se
    INNER JOIN Students st ON se.student_id = st.student_id
    INNER JOIN Courses co ON se.course_id = co.course_id;"""
  cur.execute(query)
  results = cur.fetchall()
  return results
  