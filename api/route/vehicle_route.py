from http import HTTPStatus
from flask import Flask, request, jsonify, Blueprint, make_response
from flask_cors import cross_origin, CORS
from supply_backend.api.object.vehicle import *
from supply_backend.api.service.vehicle_services import *


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

    vin = request_vehicle(start_lon,start_lat,dest_lon,dest_lat).ID

    return make_response(
        jsonify({
            'VIN': vin,
            'HTTP Status': HTTPStatus.OK.value
        }), HTTPStatus.OK.value)

@vehicle_api.route("/vehicle-add", methods=['POST'])
@cross_origin()
def vehicle_add():
    request_body = request.get_json
    request.get()

    vin = request_body.get('vin')
    lon = request_body.get('veh_lon')
    lat = request_body.get('veh_lat')
    status = request_body.get('veh_status')

    new_vehicle = Vehicle(vin, lat, lon)

    return make_response(jsonify(
        {
            "status": 'fail',
            'HTTP Status': HTTPStatus.OK.value
        }
    ), HTTPStatus.OK.value)

@vehicle_api.route("/vehicle-heartbeat", methods=['POST'])
@cross_origin()
def vehicle_heartbeat():
    data = request.get_json

    vehicleID = data.get('VIN')
    lon = data.get('veh_lon')
    lat = data.get('veh_lat')
    status = data.get('veh_status')

    vehicle = Vehicle(vehicleID, lat, lon)

    update_vehicle_status()

    response = make_response(jsonify({
        'route': ''
    }))

    return response