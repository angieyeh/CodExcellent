# Citation for the following phone numbers:
# Date: 07/17/2022
# Source URL: https://github.com/osu-cs340-ecampus/flask-starter-app

from flask import Flask, render_template
import os

# Configuration

app = Flask(__name__)

# Routes 

@app.route('/')
def root():
  return render_template("main.j2")

@app.route('/certificates')
def certificates():
  return render_template("certificates.j2")

# Listener

if __name__ == "__main__":
  port = int(os.environ.get('PORT', 8888)) 
  #                                 ^^^^
  #              You can replace this number with any valid port
  
  app.run(port=port, debug=True) 