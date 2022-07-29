from flask import Flask

from flask import request
import pymysql
import pymysql.cursors
import os

app = Flask(__name__)


# Connect to the database
connection = pymysql.connect(host='classmysql.engr.oregonstate.edu',
                             user='cs340_onid',
                             password='XXXX',
                             database='cs340_onid',
                             cursorclass=pymysql.cursors.DictCursor)

def application():
  return app

# mysql = MySQL(app)
mysql = connection.cursor()
def db():
  return mysql