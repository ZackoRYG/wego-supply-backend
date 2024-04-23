from cs_backend.api.model.db_initialization import db
from supply_backend.api.model.db_models import VehicleTable,DeliveryTable
from sqlalchemy.sql import func
from api.object.vehicle import *
import requests, json

my_token = 'pk.eyJ1IjoiZmlubjA3IiwiYSI6ImNsc2RzeWs5bDAwZ3gyanBqNGNoYmFvejYifQ.BT-DZloFB8-nheNJvf_0Ag'

# Count Order POST
def add_counter():
    pass
    # THIS IS DEPRECIATED
    # db.session.add(CounterTable(count=1))
    # db.session.commit()

# Count Order GET
def sum_counter():
    # THIS IS DEPRECIATED
    # sums "count" field of all values
    # in the database
    # int(db.session.query(func.sum(CounterTable.count)).scalar())
    return 0

def vehicle_add(vehicle: Vehicle):
    isSuccess = False
    if (vehicle.ID != None) and (vehicle.lat != None) and (vehicle.lon != None) and (vehicle.status != None) and (not vehicle_exists(vehicle)):
        db.session.add(
            VehicleTable(
                id = vehicle.ID,
                latitude = vehicle.lat,
                longitude = vehicle.lon,
                status = vehicle.status.value,
                route = None
            )
        )
        db.session.commit()
        isSuccess = True

    return isSuccess

def vehicle_exists(vehicle: Vehicle):
    vin = vehicle.ID
    existsTest = db.session.execute(db.select(VehicleTable).filter_by(id=vin)).scalar()
    return (existsTest != None)

def vehicle_heartbeat_status(vehicle_id):
    obj = None
    db_selection = db.session.query(VehicleTable).filter_by(id=vehicle_id).scalar()
    if (db_selection != None):
        listRoute = routeToList(db_selection.route) # Helper Function for converting route string. to list
        obj = Vehicle(
            vehicle_id,
            db_selection.latitude,
            db_selection.longitude,
            listRoute,
            db_selection.status
            )
        
    return obj

def request_vehicle(start_lon, start_lat,dest_lon, dest_lat):
    db_selection = db.session.query(VehicleTable).filter_by(status=Vehicle_Status.IDLE.value).first()
    if (db_selection != None):
        obj = Vehicle(
            db_selection.id,
            db_selection.latitude,
            db_selection.longitude,
            db_selection.route,
            )

        route_json = requests.get(f'https://api.mapbox.com/directions/v5/mapbox/driving/{start_lon},{start_lat};{dest_lon},{dest_lat}?steps=true&geometries=geojson&access_token={my_token}').json()
        route = json.dumps(route_json.get('routes')[0].get('geometry').get('coordinates'))

        chosenVehicle = db.session.query(VehicleTable).filter_by(id=db_selection.id).scalar()
        chosenVehicle.route=route

        db.session.commit()

    return obj

def routeToList(string):
    #this part converts the string to an array of strings
    result = string.split(",")
    result[0],result[len(result)-1] = result[0][1:],result[len(result)-1][:-1]
    for i in range(0,len(result),2):
        result[i] = result[i]+","+result[i+1]
        result[i] = result[i].strip()
    result = result[::2]
    #this part takes each element and converts it from a string to an array of floats
    for j in range(0,len(result)):
        result[j] = result[j][1:][:-1].split(",")
        result[j][0],result[j][1] = float(result[j][0]),float(result[j][1])
    #if anything breaks we are doomed
    return result

def add_delivery(vehicle_id,start_lat,start_lon,end_lat,end_lon):
    db.session.add(
        DeliveryTable(
            vehicle_id = vehicle_id,
            start_latitude = start_lat,
            start_longitude = start_lon,
            end_latitude = end_lat,
            end_longitude = end_lon
        )
        )
    db.session.commit()
    return 