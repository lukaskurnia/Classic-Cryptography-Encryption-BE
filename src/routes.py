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
        data = request.get_json()
        try:
            result, status_code = processor.request_processor(data['text'], data['key'], data['algorithm'], data['mode'])
            return make_response(jsonify({'result': result}), status_code)
        except KeyError as err:
            return make_response(jsonify({'result': f'required key {err}'}), 400)
