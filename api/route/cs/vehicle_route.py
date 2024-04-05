import json
from http import HTTPStatus
from flask import Flask, request, jsonify, Blueprint, make_response
from api.model.db_initialization import db
from flask_cors import cross_origin, CORS
from api.service.vehicle_services import *

vehicle_api = Blueprint('vehicle', __name__)
@vehicle_api.route("/vehicle-request", methods=['POST'])
@cross_origin()
def vehicle_request():
    print("backend hit")
    request_body = request.get_json

    start_lat = request_body.get('start_lat')
    start_lon = request_body.get('start_lon')
    dest_lat = request_body.get('dest_lat')
    dest_lon = request_body.get('dest_lon')

    return make_response("200 OK!", HTTPStatus.OK.value)

@vehicle_api.route("/vehicle-add", methods=['POST'])
@cross_origin()
def counter_return():
    request_body = request.get_json
    request.get()

    vin = request_body.get('VIN')
    lon = request_body.get('veh_lon')
    lat = request_body.get('veh_lat')
    status = request_body.get('veh_status')

    return jsonify(
        {
            "count_sum": sum
        }
    )