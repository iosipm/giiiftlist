from flask import Flask
from markupsafe import escape
from flask import url_for
from flask import render_template
from flask import request
from flask import redirect
from flask import abort
from flask import make_response
import sqlite3 
#
app = Flask(__name__)
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        return do_the_registration(request.form['uname'], request.form['pwd'])
    else:
        return show_the_registration_form();

def show_the_registration_form():
    return render_template('register.html',page=url_for('register'))

def do_the_registration(u,p):
    con = sqlite3.connect('registered_users.db')
    try:
        con.execute('CREATE TABLE users (name TEXT, pwd INT)')
        print ('Table created successfully');
    except:
        pass
    
    con.close()  
    
    con = sqlite3.connect('registered_users.db')
    con.execute("INSERT INTO users values(?,?);", (u, p))
    con.commit()
    con.close()  

    return show_the_login_form()

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return do_the_login(request.form['uname'], request.form['pwd'])
    else:
        return show_the_login_form()

def show_the_login_form():
    return render_template('login.html',page=url_for('login'))

def do_the_login(u,p):
    con = sqlite3.connect('registered_users.db')
    cur = con.cursor();
    cur.execute("SELECT count(*) FROM users WHERE name=? AND pwd=?;", (u, p))
    if(int(cur.fetchone()[0]))>0:                                               
        return render_template('index.html', page=url_for('login'))

    else:
        abort(403)   
@app.errorhandler(403)
def wrong_details(error):
    return render_template('wrong_details.html'), 403

#This block of code has been reused from the Lab document-basic login details. It has been modified along with the html files.


con = sqlite3.connect('Gifts.db')
con.row_factory = sqlite3.Row
cur = con.cursor()
cur.execute("SELECT * from gift")
rows = cur.fetchall();

@app.route('/wishlist')
def wishlist():     
    return render_template("wishlist.html",rows = rows)

#For this block of code I have created the wishlist file which displays the data from the database Gifts.db along with pictures to represent the gifts.

@app.route('/homepage')
def homepage():
    return render_template("homepage.html", rows = rows)

#This block of code takes the user to the homepage which is modified, I have added images into the html files along with a background image

def show_the_add_form():
    return render_template('index.html',page=url_for('index'))


def do_the_add(u,i):
    con = sqlite3.connect('events.db')
    try:
        con.execute('CREATE TABLE events (, id INT, name TEXT, date INT)')
        print ('Table created successfully');
    except:
        pass
    
    con.close()  
    
    con = sqlite3.connect('events.db')
    con.execute("INSERT INTO Events values(?,?);", (u,i))
    con.commit()
    con.close()  
    
    return show_the_add_form()


@app.route('/index')
def students():
    con = sqlite3.connect("events.db")
    con.row_factory = sqlite3.Row
    cur = con.cursor()
    cur.execute("SELECT * from events")
    rows = cur.fetchall();

    return render_template("index.html",rows = rows)
#This block of code has been created to take the user to the event page so they can create an event. The code structure is identical with the one used for the giftlist and for th eusers
#Although the guests can access the page, they can't create an event.









