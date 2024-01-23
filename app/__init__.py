from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Creating our flask application
app = Flask(__name__)

# Configuration for our application, setting the directory for out database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///../data/books.db'
# Disabling unnecessary modifications from SLQALCHEMY that we wont need
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Enables interaction with the database using entities like classes, objects, and methods 
db = SQLAlchemy(app)

# Importing the routes from our app after our configuration so we dont get issues.
from app import routes