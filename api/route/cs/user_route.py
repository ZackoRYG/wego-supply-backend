import json
from http import HTTPStatus
from flask import Flask, request, jsonify, Blueprint, make_response
from api.model.db_initialization import db
from flask_cors import cross_origin, CORS
from api.service.user_services import *

user_api = Blueprint('user', __name__)
@user_api.route("/user-signup", methods=['POST'])
@cross_origin()
def user_signup():
    print("backend hit")
    # extract request json
    data = request.get_json()

    # extract user & pass vals
    username = data.get("username")
    password = data.get("password")
    
    if create_user(username,password):
        response = make_response(jsonify({"status" : "success",
                                          "HTTP Status" : HTTPStatus.OK.value}), HTTPStatus.OK.value)
    else:
        response = make_response(jsonify({"status" : "fail",
                                          "HTTP Status" : HTTPStatus.OK.value}), HTTPStatus.OK.value)

    return response

@user_api.route("/user-login", methods=['POST'])
@cross_origin()
def login_request():
    print("backend hit")

    #extract json
    request_body = request.get_json()

    #extract username and password
    username = request_body.get("username")
    password = request_body.get("password")

    if valid_login(username, password):
        response = make_response(jsonify({"status" : "success"}), HTTPStatus.OK.value)
    else:
        response = make_response(jsonify({"status" : "fail"}), HTTPStatus.OK.value)

    return response
