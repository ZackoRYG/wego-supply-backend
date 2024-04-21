from http import HTTPStatus
from flask import request, jsonify, Blueprint, make_response
from flask_cors import cross_origin, CORS
from supply_backend.api.service.data_services import *

data_api = Blueprint('data', __name__)
@data_api.route("/vehicle-route-request/<vin>", methods=['GET'])
@cross_origin()
def vehicle_route_request(vin):
    #request_body = request.get_json()

    #vin = request_body.get('vin')

    vehicle = getVehicle(vin)

    if vehicle != None:
        route = json.loads(vehicle.route)
        status = 'success'
    else:
        route = None
        status = 'fail'
    
    response = make_response(
        jsonify({
            'status': status,
            'route': route,
            'HTTP Status': HTTPStatus.OK.value
        }), HTTPStatus.OK.value
    )

    return response