from flask import Flask

from flask import request
import pymysql
import pymysql.cursors
import os

app = Flask(__name__)


# Connect to the database
connection = pymysql.connect(host=os.environ.get('MYSQL_HOST'),
                             user=os.environ.get('MYSQL_USER'),
                             password=os.environ.get('MYSQL_PASSWORD') ,
                             database=os.environ.get('MYSQL_DB'),
                             cursorclass=pymysql.cursors.DictCursor)

def application():
  return app

# mysql = MySQL(app)
def db():
  return connection