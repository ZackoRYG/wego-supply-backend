from cs_backend.api.model.db_initialization import db
from supply_backend.api.model.db_models import VehicleTable
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
        obj = Vehicle(
            vehicle_id,
            db_selection.latitude,
            db_selection.longitude,
            db_selection.route,
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