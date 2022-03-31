from flask import Flask
from flask import render_template
import sqlite3 

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('students.html')

if __name__ == "__main__":
    