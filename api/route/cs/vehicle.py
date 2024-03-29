import json
from http import HTTPStatus
from flask import Flask, request, jsonify, Blueprint, make_response
from api.model.db_initialization import db
from api.model.db_models import CounterTable
from flask_cors import cross_origin, CORS
from api.service.vehicle_services import *

vehicle_api = Blueprint('vehicle', __name__)
'''
def add_counter():
    db.session.add(CounterTable(count=1))
    db.session.commit()

def sum_counter():
    # sums "count" field of all values
    # in the database
    return int(db.session.query(func.sum(CounterTable.count)).scalar())
'''
@vehicle_api.route("/vehicle-request", methods=['POST'])
@cross_origin()
def vehicle_request():
    add_counter()
    print("backend hit")
    request_body = request.get_json
    return make_response("200 OK!", HTTPStatus.OK.value)

@vehicle_api.route("/vehicle-request-count", methods=['GET'])
@cross_origin()
def counter_return():
    sum = sum_counter()
    print(f"attempting to send GET: {sum}")
    return jsonify(
        {
            "count_sum": sum
        }
    )