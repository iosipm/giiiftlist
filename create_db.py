from flask import Flask
from flask import render_template
import sqlite3 

app = Flask(__name__)


 
@app.errorhandler(404)
def students(e):
    con = sqlite3.connect('mydatabase.db')

    try:
        con.execute('CREATE TABLE students (name TEXT, id INT)')
        print ('Table created successfully');
    except:
        pass

    con.close()

    con = sqlite3.connect("mydatabase.db")
    con.row_factory = sqlite3.Row
    cur = con.cursor()
    cur.execute("SELECT * from students")
    rows = cur.fetchall();

    return render_template('students.html', 'login.html')
#This is the file from the lab. I have tried to run it but it wouldn't work, I could get 404 error. Therefore, for this particular file, I have thought about using the 
#error handler. I have thought about returning the render template with the student timetable. Although is not the way to make it work, I have managed to fix the error










