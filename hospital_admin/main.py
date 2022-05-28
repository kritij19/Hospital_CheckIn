from flask import Flask, render_template, request, redirect, url_for, session,flash
# from flask_mysqldb import MySQL
# import MySQLdb.cursors
import mysql.connector
import re



app = Flask(__name__)

# Change this to your secret key (can be anything, it's for extra protection)
app.secret_key = '1a2b3c4d5e'


# database credential
db_user = "root"
password = "1221"
database =  "master"
host = "127.0.0.1"

cnx = mysql.connector.connect(user=db_user, password=password,
                              host=host,
                              database=database)



# Intialize MySQL
# mysql = MySQL(app)

# http://localhost:5000/pythonlogin/ - this will be the login page, we need to use both GET and POST requests
@app.route('/', methods=['GET', 'POST'])
def login():
# Output message if something goes wrong...
    # Check if "username" and "password" POST requests exist (user submitted form)
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form:
        # Create variables for easy access
        username = request.form['username']
        password = request.form['password']
        # Check if account exists using MySQL
        # cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor = cnx.cursor()
        cursor.execute(f'SELECT * FROM accounts WHERE username = "{username}" AND password = "{password}"')
        # Fetch one record and return result
        account = cursor.fetchone()
        print(account)
        # If account exists in accounts table in out database
        if account:
            account = list(account)
            # Create session data, we can access this data in other routes
            session['loggedin'] = True
            session['id'] = account[0]
            session['username'] = account[1]
            # Redirect to home page
            return redirect(url_for('home'))
        else:
            # Account doesnt exist or username/password incorrect
            flash("Incorrect username/password!", "danger")
    return render_template('auth/login.html',title="Login")



# http://localhost:5000/register 
# This will be the registration page, we need to use both GET and POST requests
@app.route('/register', methods=['GET', 'POST'])
def register():
    # Check if "username", "password" and "email" POST requests exist (user submitted form)
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form and 'email' in request.form:
        # Create variables for easy access
        username = request.form['username']
        password = request.form['password']
        email = request.form['email']
        cursor = cnx.cursor()
        
        # Check if account exists using MySQL
        cursor.execute( "SELECT * FROM accounts WHERE username LIKE %s", [username] )
        account = cursor.fetchone()
        # If account exists show error and validation checks

        if account:
            flash("Account already exists!", "danger")
        elif not re.match(r'[^@]+@[^@]+\.[^@]+', email):
            flash("Invalid email address!", "danger")
        elif not re.match(r'[A-Za-z0-9]+', username):
            flash("Username must contain only characters and numbers!", "danger")
        elif not username or not password or not email:
            flash("Incorrect username/password!", "danger")
        else:
        # Account doesnt exists and the form data is valid, now insert new account into accounts table
            cursor.execute(f'INSERT INTO `accounts`(`username`, `password`, `email`) VALUES ("{username}","{password}","{email}")')
            cnx.commit()
            flash("You have successfully registered!", "success")
            return redirect(url_for('login'))

    elif request.method == 'POST':
        # Form is empty... (no POST data)
        flash("Please fill out the form!", "danger")
    # Show registration form with message (if any)
    return render_template('auth/register.html',title="Register")

# http://localhost:5000/pythinlogin/home 
# This will be the home page, only accessible for loggedin users

@app.route('/home')
def home():
    # Check if user is loggedin
    if 'loggedin' in session:

        cursor = cnx.cursor()
        cursor.execute(f'SELECT * FROM user WHERE 1')
        # Fetch one record and return result
        userData = cursor.fetchall()

        # User is loggedin show them the home page
        return render_template('home/home.html', username=session['username'],title="Home",userList=userData)
    # User is not loggedin redirect to login page
    return redirect(url_for('login'))    


@app.route('/profile')
def profile():
    # Check if user is loggedin
    if 'loggedin' in session:
        user_id = session['id']
        cursor = cnx.cursor(dictionary=True)
        cursor.execute(f'SELECT *  FROM accounts WHERE id ="{user_id}"')
        user_data = cursor.fetchone()
        # User is logged in show them the home page
        return render_template('auth/profile.html', username=session['username'], userData=user_data)
    # User is not loggedin redirect to login page
    return redirect(url_for('login'))  

@app.route('/logout')
def logout():
	session.pop('loggedin', None)
	return render_template('auth/login.html',title="Login")

@app.route('/view', methods=['GET', 'POST'])
def view():
    if 'loggedin' in session:
        id = request.form['id']
        if id:
            cursor = cnx.cursor(dictionary=True)
            cursor.execute(f'SELECT *  FROM user WHERE User_ID ="{id}"')
            user_data = cursor.fetchone()
            return render_template('home/view.html', username=session['username'], userData=user_data, message='')
        else:
            return render_template('home/view.html', username=session['username'], message="Data not found")

            

if __name__ =='__main__':
	app.run()
