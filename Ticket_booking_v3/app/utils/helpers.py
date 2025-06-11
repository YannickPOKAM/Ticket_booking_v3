# app/utils/helpers.py

from flask import jsonify

def jsonify_response(message, status=200):
    return jsonify({'message': message}), status
