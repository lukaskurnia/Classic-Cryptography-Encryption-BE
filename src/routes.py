from flask import jsonify, request, make_response, send_file
from flask_restful import Resource
from src import processor
import base64
import binascii

class Hello(Resource):
    def get(self): 
        return jsonify({'message': 'hello world'})
  
    def post(self): 
        data = request.get_json()
        return jsonify({'data': data})

class Text(Resource): 
    def post(self): 
        data = request.form
        result, status_code = processor.request_processor(data['text'], data['key'], data['algorithm'], data['mode'], is_binary = False)
        
        output = request.args.get('output')
        if output == 'file' and status_code == 200:
            filename = "result.txt"
            processor.output_to_file(filename, result)
            return send_file(filename, mimetype='text/plain', attachment_filename=filename, as_attachment=True)
        else:
            return make_response(jsonify({'result': result}), status_code)

class FileText(Resource): 
    def post(self): 
        data = request.form
        file = request.files['text']
        text = processor.convert_file_to_string(file)
        result, status_code = processor.request_processor(text, data['key'], data['algorithm'], data['mode'], is_binary = False)
        
        output = request.args.get('output')
        if output == 'file' and status_code == 200:
            filename = "result.txt"
            processor.output_to_file(filename, result)
            return send_file(filename, mimetype='text/plain', attachment_filename=filename, as_attachment=True)
        else:
            return make_response(jsonify({'result': result}), status_code)

class FileBinary(Resource): 
    def post(self): 
        data = request.form
        file = request.files['text']
        readed = file.read()
        result, status_code = processor.request_processor(readed, data['key'], data['algorithm'], data['mode'], is_binary = True)
        
        output = request.args.get('output')
        if output == 'file' and status_code == 200:
            filename = "result.txt"
            processor.output_to_file(filename, result)
            return send_file(filename, mimetype='text/plain', attachment_filename=filename, as_attachment=True)
        else:
            return make_response(jsonify({'result': result}), status_code)