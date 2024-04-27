from http import HTTPStatus
from flask import Flask, request, jsonify, Blueprint, make_response
from flask_cors import cross_origin, CORS
from supply_backend.api.object.vehicle import *
from supply_backend.api.object.delivery import *
from supply_backend.api.service.vehicle_services import *


vehicle_api = Blueprint('vehicle', __name__)
@vehicle_api.route("/vehicle-request", methods=['POST'])
@cross_origin()
def vehicle_request():
    print("backend hit")
    request_body = request.get_json()

    start_lat = request_body.get('start_lat')
    start_lon = request_body.get('start_lon')
    dest_lat = request_body.get('dest_lat')
    dest_lon = request_body.get('dest_lon')

    requested_vehicle = request_vehicle(start_lon,start_lat,dest_lon,dest_lat)

    if requested_vehicle != None:
        status = 'success'
        vin = requested_vehicle.ID
    else:
        status = 'fail'
        vin = -1

    return make_response(
        jsonify({
            'VIN': vin,
            'status': status,
            'HTTP Status': HTTPStatus.OK.value
        }), HTTPStatus.OK.value)

@vehicle_api.route("/vehicle-add", methods=['POST'])
@cross_origin()
def vehicle_add_request():
    request_body = request.get_json()

    vin = request_body.get('vin')
    lon = request_body.get('veh_lon')
    lat = request_body.get('veh_lat')
    status = Vehicle_Status.IDLE #request_body.get('veh_status')

    new_vehicle = Vehicle(vin, lat, lon, route= None, status= status)

    if vehicle_add(new_vehicle):
        status = 'success'
    else:
        status = 'fail'

    return make_response(jsonify(
        {
            "status": status,
            'HTTP Status': HTTPStatus.OK.value
        }
    ), HTTPStatus.OK.value)

@vehicle_api.route("/vehicle-heartbeat", methods=['POST'])
@cross_origin()
def vehicle_heartbeat():
    data = request.get_json()
    print("!!! VEHICLE DATA RECIEVED: " + str(data))

    vehicleID = data.get('vin')
    print(vehicleID)
    lon = data.get('veh_lon')
    lat = data.get('veh_lat')
    status = data.get('veh_status')
    route = data.get('route')

    vehicle = Vehicle(vehicleID, lat, lon, route, status)

    return_val = update_vehicle_status(vehicle)

    delivery = get_delivery(vehicleID)

    if delivery != None:
        response = make_response(jsonify({
            'start_lat': delivery.start_latitude,
            'start_lon': delivery.start_longitude,
            'dest_lat': delivery.destination_latitude,
            'dest_lon': delivery.destination_longitude
        }), HTTPStatus.OK.value)
    else:
        response = make_response(
        jsonify({
            'Updated': return_val,
            'HTTP Status': HTTPStatus.ACCEPTED.value
        }), HTTPStatus.ACCEPTED.value)

    return response