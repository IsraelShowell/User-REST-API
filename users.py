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
from flask_restful import Resource, reqparse, fields, marshal_with
from user_model import UserModel
from extensions import db

#This initializes a request parser object to handle incoming request arguments.
user_args = reqparse.RequestParser()

#This adds a 'name' argument to the parser, must be a string, and is required (cannot be blank).
user_args.add_argument('name', type=str, required=True, help='Name cannot be blank')

#This adds an 'email' argument to the parser, must be a string, and is required (cannot be blank).
user_args.add_argument('email', type=str, required=True, help='Email cannot be blank')

#This defines the fields for our Json data returned by the API
#This is the shape of the data that will be returned by the API
userFields = {
    'id': fields.Integer,
    'name': fields.String,
    'email': fields.String
}

#Define a resource class named 'Users' that inherits from Flask-RESTful's 'Resource' class.
class Users(Resource):  
    
    #Marshal_with is a decorator that allows us to automatically marshal 
    # our data into the correct format
    @marshal_with(userFields)
    
    #This defines a 'get' method to handle GET requests for this resource.
    def get(self): 
        
        #This queries the database to retrieve all records from the 'user_model' table.
        users = UserModel.query.all()  
        
        #This returns a list of users as the response.
        return users  

    @marshal_with(userFields)
    
    #This defines a 'post' method to handle POST requests for this resource.
    def post(self):  
        
        #This parses the incoming request arguments using the 'user_args' parser.
        args = user_args.parse_args()  
        
        #This creates a new 'UserModel' instance with the parsed 'name' and 'email'.
        user = UserModel(name=args['name'], email=args['email'])  
        
        #This adds the new user instance to the database session.
        db.session.add(user)  
        
        #This commits the session to save the new user to the database.
        db.session.commit()  
        
        #This queries the database to retrieve all records from the 'UserModel' table.
        users = UserModel.query.all()  
        
        #This returns the list of users and a status code of 201 (Created).
        return users, 201
