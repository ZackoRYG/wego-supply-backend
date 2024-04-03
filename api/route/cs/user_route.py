import json
from http import HTTPStatus
from flask import Flask, request, jsonify, Blueprint, make_response
from api.model.db_initialization import db
from api.model.db_models import CounterTable
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
        return make_response("200 OK!", HTTPStatus.OK.value)
    else:
        return make_response("400 NO!", HTTPStatus.NOT_FOUND.value)