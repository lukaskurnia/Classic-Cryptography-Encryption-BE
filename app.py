from flask import Flask, jsonify, request 
from flask_restful import Resource, Api 
from src import routes
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
api = Api(app)  

# adding the defined resources along with their corresponding urls 
api.add_resource(routes.Hello, '/')
api.add_resource(routes.Text, '/text')
api.add_resource(routes.FileText, '/file_text')
api.add_resource(routes.FileBinary, '/file_binary')

if __name__ == '__main__': 
    app.run(debug = True) 
