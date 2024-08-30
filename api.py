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
from flask import Flask
from flask_restful import Api
from extensions import db
from users import Users
from user import User

#This is the main application's name
app = Flask(__name__)

#This line tells SQLAlchemy to use the SQLite database 'users.db'
#The 3 slashes (//) means the database is in the same directory as the script
app.config['SQLALCHEMY_DATABASE_URI'] ='sqlite:///users.db'

#This calls the database
db.init_app(app)

#This line creates an application context.
#Explanation: In Flask, certain operations require access to the application's context, which includes configuration settings, 
#application-level variables, and other resources. 
# The app.app_context() is a context manager that ensures that these operations can access the necessary context.
with app.app_context():
    
    #with db.create_all() instructs SQLAlchemy (Flask's ORM) to create all the database
    #tables defined by your application's models. 
    #If the tables already exist, this command will not recreate them.
    db.create_all()
    
#This tells Flask-Restful to use the API for our resources
api = Api(app)

#This tells the api that the Users resource is avaliable at the '/api/users/' endpoint
api.add_resource(Users, '/api/users/')


#This tells the api that the User resource is avaliable at the '/api/users/<int:id>' endpoint
api.add_resource(User, '/api/users/<int:id>')

#This is a route where we request data from the API
@app.route('/')
def Home():
    return '<h1>Flask REST API!</h1>'

#This tells the to start the server and listen for requests
if __name__ == '__main__':
    app.run()
    
#End of script
