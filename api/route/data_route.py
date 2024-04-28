from http import HTTPStatus
from flask import request, jsonify, Blueprint, make_response
from flask_cors import cross_origin, CORS
from supply_backend.api.service.data_services import *

data_api = Blueprint('data', __name__)
@data_api.route("/get-all-vehicles", methods=['GET'])
@cross_origin()
def get_all_vehicles():
    #request_body = request.get_json()

    #vin = request_body.get('vin')

    vehicles = query_all_vehicles()
    vehicles_dict_list = []

    if vehicles != None:
        for vehicle in vehicles:
            vehicle_dict = {
                "vin": vehicle.ID,
                "veh_lat": vehicle.lat,
                "veh_lon": vehicle.lon,
                # since vehicle.route is string represented as an array
                # we must load it as an array
                "route": json.loads(vehicle.route),
                "status": vehicle.status
            }
            print(vehicle_dict)
            vehicles_dict_list.append(vehicle_dict)

        status = 'success'

    else:
        status = 'fail'
    
    response = make_response(vehicles_dict_list, HTTPStatus.OK.value)

    return response