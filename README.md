
<h1 align="center">Hospital CheckIn System </h1>
<h5 align="center"><em>(Using Face Recognition)</em></h5>

A brief description of what this project does and who it's for


## Table of Contents


* [About the Project](#about-the-project)
  * [Built With](#built-with)
* [Getting Started](#getting-started)
  * [Prerequisites](#prerequisites)
  * [Installation](#installation)
  * [Usage](#usage)
* [Contributing](#contributing)
* [License](#license)
* [Contact](#contact)
* [Acknowledgements](#acknowledgements)
## About the Project

dsssdfsd

### Built With

* [Python](https://www.python.org/)
* [Flask](https://palletsprojects.com/p/flask/)
* [Microsoft Azure Face API](https://azure.microsoft.com/en-in/services/cognitive-services/face/#overview)
* [MySQL](https://jquery.com)
## Getting Started

### Prerequisites

* [Python](https://www.python.org/)
* [MySQL Community Server](https://dev.mysql.com/downloads/mysql/)

### Installation

1. Clone the repository
```sh
git clone https://github.com/kritij19/Hospital_CheckIn.git
```
2a. Create a Virtual Environment (Optional)
```sh
python -m venv venv
```
2b. Activate the virtual environment 
```sh
.\venv\Scripts\activate
```
3. Install the requirements and dependancies
```sh
pip install -r requirements.txt
```
4. Run `setup_db.sql` in your MySQL Server  

## Usage

### I) New user registration:

1. Run the following command
```python
python registration\registration.py -u <MySQL_database_user> -p <MySQL_database_password>
```
2. View the application on localhost
<a href = 'http://127.0.0.1:5000/'> </a>

### II) Face recognition based CheckIn:
1. Run the following command
```python
python face_recognition/face_recognition.py -u <MySQL_database_user> -p <MySQL_database_password>
```
2. View the application on localhost
<a href = 'http://127.0.0.1:5000/'> </a> 
```
http://127.0.0.1:5000/
```
### III) Hospital Admin Side:
1. Run the following command
```python
python hospital_admin/hospital_admin.py -u <MySQL_database_user> -p <MySQL_database_password>
```
2. View the application on localhost
<a href = 'http://127.0.0.1:5000/'> </a>
```
http://127.0.0.1:5000/
```
> Note: You will have to stop the execution of one application to access the other
