from flask import Flask
from flask_restful import Api, Resource, reqparse

app = Flask(__name__)
api = Api(app)

# some sample users
users = [
    {
        "name": "Nicholas",
        "age": 42,
        "occupation": "Network Engineer"
    },
    {
        "name": "Elvin",
        "age": 32,
        "occupation": "Doctor"
    },
    {
        "name": "Jass",
        "age": 22,
        "occupation": "Web Developer"
    }
]

class User(Resource):
    '''
    GET - retrieves information about a user.
    return the user and 200 status code if found, 404 otherwise
    '''
    def get(self, name):
        for user in users:
            if(name == user["name"]):
                return user, 200
        return "User not found", 404

    '''
    POST - adds a user to our database, returns the user and 
    201 status code
    '''
    def post(self, name):
        parser = reqparse.RequestParser()
        parser.add_argument("age")
        parser.add_argument("occupation")
        args = parser.parse_args()

        for user in users:
            if(name == user["name"]):
                return "User with name {} already exists".format(name), 400

        user = {
            "name": name,
            "age": args["age"],
            "occupation": args["occupation"]
        }
        users.append(user)
        return user, 201

    '''
    PUT - updates a user and returns the user info and a 201 status code
    '''
    def put(self, name):
        parser = reqparse.RequestParser()
        parser.add_argument("age")
        parser.add_argument("occupation")
        args = parser.parse_args()
        
        '''
        Implement this! A put request simply updates a user
        '''

        users.append(user)
        return user, 201

    '''
    Deletes a user and returns a 200 status code or 404 if user 
    not found
    '''
    def delete(self, name):
        global users
        '''
        Implement this! This deletes a user from our app
        '''
        return "{} is deleted.".format(name), 200
      
'''
Our endpoint, to access a uer go to 127.0.0.1/user/<string:name>
ex - 127.0.0.1/user/jas
'''
api.add_resource(User, "/user/<string:name>")

app.run(debug=True)
