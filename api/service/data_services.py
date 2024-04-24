from cs_backend.api.model.db_initialization import db
from supply_backend.api.model.db_models import VehicleTable
from supply_backend.api.service.vehicle_services import *
from sqlalchemy.sql import func
from api.object.vehicle import *
import requests, json

def getVehicle(vin):
    vehicle = get_vehicle_by_id(vin)

    return vehicle