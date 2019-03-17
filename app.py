from flask import Flask
from flask import Flask, flash, redirect, render_template, request, session, abort
import os
from sqlalchemy.orm import sessionmaker
from tabledef import *
from insertDb import *
from writeJson import *

engine = create_engine('sqlite:///userdata.db', echo=True)
 
app = Flask(__name__)

currentUser = None
 
@app.route('/')
def home():
    global currentUser
    if not session.get('logged_in'):
        return render_template('login.html', page_title = "Login")
    else:  
        try:
            with open("data.json") as dfile:
                d = json.load(dfile)

            for user in d['users']:
                if(user['email'] == currentUser):
                    data = user

            return render_template('details.html', page_title = "Your Details", data = data)
        except:
            return render_template('details.html', page_title = "Your Details")
        
@app.route('/login', methods=['POST'])
def do_login():
    global currentUser
    POST_EMAIL = str(request.form['email'])
    POST_PASSWORD = str(request.form['password'])
    
    Session = sessionmaker(bind=engine)
    s = Session()
    query = s.query(User).filter(User.email.in_([POST_EMAIL]), User.password.in_([POST_PASSWORD]) )
    result = query.first()
    if result:
        session['logged_in'] = True
        currentUser = POST_EMAIL
    else:
        flash('wrong password!')
    return home()

@app.route('/registerpage')
def registerpage():
    if not session.get("logged_in"):
        return render_template('register.html', page_title = "Registration")
    else:
        return "You are already registered! <a href='/logout'>Logout</a>"

@app.route('/register', methods=['POST'])
def do_register():
    POST_USERNAME = str(request.form['username'])
    POST_PASSWORD = str(request.form['password'])
    POST_EMAIL = str(request.form['email'])
    POST_DEGREE = str(request.form['degree'])
    POST_REGISTER = int(request.form['register'])
    POST_AGE = int(request.form['age'])
    POST_CITY = str(request.form['city'])

    data = {}
    data['users'] = []
    data['users'].append({
        'username' : POST_USERNAME,
        'password' : POST_PASSWORD,
        'email' : POST_EMAIL,
        'degree' : POST_DEGREE,
        'register' : POST_REGISTER,
        'age' : POST_AGE,
        'city' : POST_CITY
    })

    writejson(data, "data.json")

    insertDb(POST_USERNAME, POST_PASSWORD, POST_EMAIL, POST_DEGREE, POST_REGISTER, POST_AGE, POST_CITY)

    return home()

@app.route("/logout")
def logout():
    global currentUser
    session['logged_in'] = False
    currentUser = None
    return home()
 
if __name__ == "__main__":
    app.secret_key = os.urandom(12)
    app.run(debug=True,host='0.0.0.0', port=4000)