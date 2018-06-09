from simple_python_application import application

from flask import jsonify

@application.route('/', methods=['GET'])
def home():
    return jsonify({ 'message': 'Simple python app for CS450' })