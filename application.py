from flask import Flask, request
from flask_restful import Resource, Api

application = app = Flask(__name__)
api = Api(app)

class HelloWorld(Resource):
    def get(self):
        return {'about':'Hello World2'}

api.add_resource(HelloWorld, '/test')

if __name__ == '__main__':
    app.run(debug=True)