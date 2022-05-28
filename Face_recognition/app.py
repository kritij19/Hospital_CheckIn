"""
Capture the picture of a user. Show welcome message with apoointment details, if face recognized. Show message otherwise.

The appointment details - appointment timing (30 minutes from current time) and token number (random number between 1 and 100) is hardcoded for
representative purposes.
"""

from time import strftime
from flask import Flask, render_template, request
import base64
import os
from identify import identify
from datetime import datetime, timedelta
import random
from flaskext.mysql import MySQL

app = Flask(__name__)
mysql = MySQL()
 
# MySQL configurations
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = '1221'
app.config['MYSQL_DATABASE_DB'] = 'master'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)

@app.route("/")
def hello():
  return render_template('./index.html')
  
@app.route('/handle_data', methods=['POST'])

def handle_data():
    # Get image captured by user
    img = request.form['image']
    image_parts =  img.split(";base64,")
    image_type_aux = image_parts[0].split("image/")
    # image_type = image_type_aux[1]

    # Check if user has submitted form before cliking pixture
    try:
      image_base64 =base64.b64decode(image_parts[1])
    except: # Index out of range error
      return render_template('./result.html', output = "Please click a picture before submitting!")

    # Get path to image
    my_cwd = os.path.dirname(__file__)
    file_path = os.path.join(my_cwd, 'upload', 'image.png' )
    print(file_path)

    with open(file_path, 'wb') as f:
        f.write(image_base64)
    
    res = identify(file_path) # Returns person ID

    # If face recognized, get details from db
    if(res != ''):
      # print(res)
      queryString = f"select* from user where PersonID = '{str(res)}'"

      # Connect to database and running query
      conn = mysql.connect()
      cursor = conn.cursor()
      cursor.execute(queryString)
      fetchLabel = cursor.fetchone()  
      conn.commit()

      if(fetchLabel == None): # Details for person not found in db
        result_disp = "Face not recognized! Retry if you have registered or create a new profile"
      else:
        fname = fetchLabel[1] # First name
        lname = fetchLabel[2] # Last name
        cnum = fetchLabel[3] # Contact number

        # Generate welcome message with appointment details (hardcoded right now)
        dt = datetime.now() + timedelta(minutes=30)
        result_disp = f"""Welcome {fname} {lname}! \n 
        Your appointment is scheduled for {dt.strftime("%d/%m/%Y")} at {dt.strftime("%H:%M")} \n
        Your token number is {random.randrange(20, 50, 3)}.
        Appointments details have also been sent on your registered contact number: {cnum}"""

    else: # No face recognized in picture captured
      result_disp = "Face not recognized! Retry if you have registered or create a new profile"

    return render_template('./result.html', output = result_disp)
    
  
if __name__ == "__main__":
  app.run(debug = True)
