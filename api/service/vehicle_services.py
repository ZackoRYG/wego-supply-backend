from cs_backend.api.model.db_initialization import db
from supply_backend.api.model.db_models import VehicleTable
from sqlalchemy.sql import func
from api.object.vehicle import *
import requests, json


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
    db_selection = db.session.query(VehicleTable).filter_by(status=Vehicle_Status.IDLE).scalar()
    if (db_selection != None):
        obj = Vehicle(
            db_selection.id,
            db_selection.latitude,
            db_selection.longitude,
            db_selection.route,
            )

    route_json = requests.get(f'https://api.mapbox.com/directions/v5/mapbox/driving/{start_lon},{start_lat};{dest_lon},{dest_lat}?steps=true&geometries=geojson&access_token={my_token}').json()
    route = json.loads(route_json.text).get('routes')[0].get('geometry').get('coordinates')

    db.session.update(VehicleTable).where(id=db_selection.id).values(route=route)

    db.session.commit()

    return obj