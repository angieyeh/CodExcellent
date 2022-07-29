from flask import Flask

from flask import request
import pymysql
import pymysql.cursors
import os

app = Flask(__name__)


# Connect to the database
connection = pymysql.connect(host='classmysql.engr.oregonstate.edu',
                             user='cs340_fishebeg',
                             password='7237',
                             database='cs340_fishebeg',
                             cursorclass=pymysql.cursors.DictCursor)

# app.config['MYSQL_HOST'] = os.environ.get('MYSQL_HOST')
# app.config['MYSQL_USER'] =  os.environ.get('MYSQL_USER')
# app.config['MYSQL_PASSWORD'] = os.environ.get('MYSQL_PASSWORD') 
# app.config['MYSQL_DB'] = os.environ.get('MYSQL_DB')
# app.config['MYSQL_CURSORCLASS'] = os.environ.get('MYSQL_CURSORCLASS')

def application():
  return app

# mysql = MySQL(app)
mysql = connection.cursor()
def db():
  return mysql