# Creator: Israel Showell
# Start Date: 8-30-24
# End Date: 
# Project Name: User REST API
# Description: 
"""
This project creates a RESTful API for managing user data, 
and then I call the API to load the data. 
This project let me practice developing REST APIs and calling them!
"""

#Imported libraries need to make the API work
from user_model import UserModel
from flask_restful import marshal_with, Resource, abort, fields, reqparse
from extensions import db

#This initializes a request parser object to handle incoming request arguments.
user_args = reqparse.RequestParser()

#This adds a 'name' argument to the parser, must be a string, and is required (cannot be blank).
user_args.add_argument('name', type=str, required=True, help='Name cannot be blank')

#This adds an 'email' argument to the parser, must be a string, and is required (cannot be blank).
user_args.add_argument('email', type=str, required=True, help='Email cannot be blank')

#This defines the fields for our JSON data returned by the API
#This is the shape of the data that will be returned by the API
userFields = {
    'id': fields.Integer,
    'name': fields.String,
    'email': fields.String
}

#Define a resource class named 'User' that inherits from Flask-RESTful's 'Resource' class.
class User(Resource):
    
    #marshal_with is a decorator that allows us to automatically marshal 
    # our data into the correct format
    @marshal_with(userFields)
    
    #This method is called when we want to get 1 user from the database
    def get(self, id):
        #This queries the database to find a user with the specified id
        user = UserModel.query.filter_by(id=id).first()
        
        #If no user is found, abort with a 404 error and a message
        if not user:
            abort(404, message="User not found")
        
        #Return the user data
        return user
    
    @marshal_with(userFields)
    #This method is called when we want to update an existing user in the database
    def patch(self, id):
        #This parses the incoming request arguments using the 'user_args' parser.
        args = user_args.parse_args()
         
        #This queries the database to find a user with the specified id
        user = UserModel.query.filter_by(id=id).first()
        
        #If no user is found, abort with a 404 error and a message
        if not user:
            abort(404, message="User not found")
        
        #Update the user fields with the new data
        user.name = args['name']
        user.email = args['email']
        
        #Commit the changes to the database
        db.session.commit()
        
        #Return the updated user data
        return user
    
    @marshal_with(userFields)
    #This method is called when we want to delete a user from the database
    def delete(self, id):
        #This queries the database to find a user with the specified id
        user = UserModel.query.filter_by(id=id).first()
        
        #If no user is found, abort with a 404 error and a message
        if not user:
            abort(404, message="User not found")
        
        #Delete the user from the database
        db.session.delete(user)
        
        #Commit the changes to the database
        db.session.commit()
        
        #Query the database to retrieve all remaining users
        users = UserModel.query.all()
        
        #Return the list of users and a status code of 204 (No Content)
        return users, 204
