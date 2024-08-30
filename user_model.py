# Creator: Israel Showell
# Start Date: 8-30-24
# End Date: 8-30-24
# Project Name: User REST API
# Description: 
"""
This project creates a RESTful API for managing user data, 
and then I call the API to load the data. 
This project let me practice developing REST APIs and calling them!
"""

#Imported libraries need to make the API work
from extensions import db

#This is a class that represents a user in our database
class UserModel(db.Model):
    
    #This line tells SQLAlchemy to create an id for each user, and makes it a primary key
    id = db.Column(db.Integer, primary_key=True)
    
    #These lines tell SQLAlchemy to create two columns for each user: name and email
    name = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(80), unique=True, nullable=False)
    
    #This line tells Python to create a string representation of each user object
    def __repr__(self):
        #This is a raw string that represents the user object
        return f'User(name={self.name}, email={self.email})'
