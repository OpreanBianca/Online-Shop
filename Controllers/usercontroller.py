import json

from flask import Blueprint, request
from flask_cors import cross_origin

from Services.userservice import UserService

app_user = Blueprint('app_user', __name__)


@app_user.route("/user/create", methods=['POST'])
@cross_origin()
def create():
    request_data = request.get_json()
    userservice = UserService()
    userservice.create_user(request_data)
    return json.dumps({'success': True}), 200, {'ContentType': 'application/json'}


@app_user.route("/user/login", methods=['POST'])
@cross_origin()
def login():
    request_data = request.get_json()
    userservice = UserService()
    user = userservice.login(request_data)
    if user:
        return json.dumps({
            "id": user.id,
            "username": user.username,
            "email": user.email,
            "password": user.password
        }), 200, {'ContentType': 'application/json'}
    else:
        return json.dumps({
            "Exception": 'Password is not right',
        }), 401, {'ContentType': 'application/json'}


@app_user.route("/user/change_password", methods=['PUT'])
def change_password():
    request_data = request.get_json()
    userservice = UserService()
    result = userservice.change_password(request_data)
    if result:
        return json.dumps({
            "Result": result
        }), 200, {'ContentType': 'application/json'}
    else:
        return json.dumps({
            "Exception": 'Something is wrong',
        }), 200, {'ContentType': 'application/json'}
