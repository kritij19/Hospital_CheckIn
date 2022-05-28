"""
User database access for hospital admin. Admin needs to first register and then login to access data.
"""

from distutils.log import debug
from flask import Flask, render_template, request, redirect, url_for, session,flash
import mysql.connector
import re
import argparse


app = Flask(__name__)

# Change this to your secret key (can be anything, it's for extra protection)
app.secret_key = '1a2b3c4d5e'

if __name__ == '__main__':  

    # Configure arguments
    ap = argparse.ArgumentParser()
    ap.add_argument("-u", "--DB_USER", required=True, help="MySQL database user")
    ap.add_argument("-p", "--DB_PASSWORD", required=True, help="MySQL database password")
    args = vars(ap.parse_args())

    # Database credentials
    db_user = args['DB_USER']
    password = args['DB_PASSWORD']
    database =  "master"
    host = "127.0.0.1"

    # Connect to db
    cnx = mysql.connector.connect(user=db_user, password=password,
                                host=host,
                                database=database)


    # Login url: http://localhost:5000/pythonlogin/
    @app.route('/', methods=['GET', 'POST'])
    def login():
        if request.method == 'POST' and 'username' in request.form and 'password' in request.form:
            # Get input from form 
            username = request.form['username']
            password = request.form['password']

            # Connect to db and execute query
            cursor = cnx.cursor()
            cursor.execute(f'SELECT * FROM accounts WHERE username = "{username}" AND password = "{password}"')

            account = cursor.fetchone()
            print(account)
            
            # If account with entered details exists in table 
            if account:
                account = list(account)

                # Create session data
                session['loggedin'] = True
                session['id'] = account[0]
                session['username'] = account[1]
                
                # Redirect to home page
                return redirect(url_for('home')) 

            else: # Account doesnt exist or username/password incorrect            
                flash("Incorrect username/password!", "danger")

        return render_template('auth/login.html',title="Login")



    # Register url: http://localhost:5000/register 
    @app.route('/register', methods=['GET', 'POST'])
    def register():      
        if request.method == 'POST' and 'username' in request.form and 'password' in request.form and 'email' in request.form:

            username = request.form['username']
            password = request.form['password']
            email = request.form['email']
            
            # Check if account exists
            cursor = cnx.cursor()
            cursor.execute( "SELECT * FROM accounts WHERE username LIKE %s", [username] )
            account = cursor.fetchone()

            # Apply checks
            if account: # Account exists
                flash("Account already exists!", "danger")
            elif not re.match(r'[^@]+@[^@]+\.[^@]+', email): # Email validation
                flash("Invalid email address!", "danger")
            elif not re.match(r'[A-Za-z0-9]+', username): # Username validation
                flash("Username must contain only characters and numbers!", "danger")
            elif not username or not password or not email: # Other validations
                flash("Incorrect username/password!", "danger")
            else: # Account details valid, insert new account into accounts table
                cursor.execute(f'INSERT INTO `accounts`(`username`, `password`, `email`) VALUES ("{username}","{password}","{email}")')
                cnx.commit() 

                flash("You have successfully registered!", "success")
                return redirect(url_for('login'))

        elif request.method == 'POST': # No inputs provided            
            flash("Please fill out the form!", "danger")

        # Show registration form with message (if any)
        return render_template('auth/register.html',title="Register")


    # Home page url: http://localhost:5000/pythinlogin/home 
    # Home page, only accessible for loggedin users
    @app.route('/home')
    def home():      
        if 'loggedin' in session: # If user is loggedin
            cursor = cnx.cursor()
            cursor.execute(f'SELECT * FROM user WHERE 1')
            userData = cursor.fetchall()

            # Display home page
            return render_template('home/home.html', username=session['username'],title="Home",userList=userData)

        # If user not loggedin, redirect to login page
        return redirect(url_for('login'))    


    # Profile, only accessible for loggedin users
    @app.route('/profile')
    def profile():        
        if 'loggedin' in session: # If user is loggedin
            user_id = session['id']

            cursor = cnx.cursor(dictionary=True)
            cursor.execute(f'SELECT *  FROM accounts WHERE id ="{user_id}"')
            user_data = cursor.fetchone()

            # Display profile
            return render_template('auth/profile.html', username=session['username'], userData=user_data)

        # If user not loggedin, redirect to login page
        return redirect(url_for('login'))  


     # Logout
    @app.route('/logout')
    def logout():
        session.pop('loggedin', None)

        # Redirect to login after logout
        return render_template('auth/login.html',title="Login") 


    # View registered user details
    @app.route('/view', methods=['GET', 'POST'])
    def view():
        if 'loggedin' in session:
            id = request.form['id']
 
            if id: # Valid user
                cursor = cnx.cursor(dictionary=True)
                cursor.execute(f'SELECT *  FROM user WHERE User_ID ="{id}"')
                user_data = cursor.fetchone()
                return render_template('home/view.html', username=session['username'], userData=user_data, message='')
            else:
                return render_template('home/view.html', username=session['username'], message="Data not found")
          

if __name__ =='__main__':
	app.run(debug = True)
