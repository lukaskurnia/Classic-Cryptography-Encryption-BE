from flask import jsonify, request, make_response
from flask_restful import Resource
from src import processor

class Hello(Resource):
    def get(self): 
        return jsonify({'message': 'hello world'})
  
    def post(self): 
        data = request.get_json()
        return jsonify({'data': data})

class Text(Resource): 
    def post(self): 
        data = request.form
        result, status_code = processor.request_processor(data['text'], data['key'], data['algorithm'], data['mode'])
        return make_response(jsonify({'result': result}), status_code)

class FileText(Resource): 
    def post(self): 
        data = request.form
        file = request.files['text']
        text = processor.convert_file_to_string(file)
        result, status_code = processor.request_processor(text, data['key'], data['algorithm'], data['mode'])
        return make_response(jsonify({'result': result}), status_code)
