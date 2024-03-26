# Product Service

from flask import Flask
from flask_restful import Resource, Api

app =  Flask(__name__)
api = Api(app)

class Todo(Resource):
    def get(self):
        return{
            'todo': ['bath', 'wash', 'sweep']
        }
        

api.add_resource(Todo, "/")

if __name__ == "__main__":
    app.run(host='0.0.0.', port=80, debug= True)