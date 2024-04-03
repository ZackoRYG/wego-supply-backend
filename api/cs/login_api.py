import json
from http import HTTPStatus
from flask import Flask, request, jsonify, Blueprint, make_response
from api.model.db_initialization import db
from api.model.db_models import AccountTable
from flask_cors import cross_origin, CORS

login_api = Blueprint('login', __name__)

def user_exists(username, password):
    return

@login_api.route("/login-request", methods=['POST'])
@cross_origin()
def login_request():
    print("backend hit")
    request_body = request.get_json
    username = request_body.get("username")
    password = request_body.get("password")

    if user_exists(username, password):
        response = make_response("User exists OK!", HTTPStatus.OK.value)
    else:
        response = make_response("User not found", HTTPStatus.OK.value)

    return response
