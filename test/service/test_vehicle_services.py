import pytest
from app import create_app
from api.service.vehicle_services import *

@pytest.fixture
def app():
    return create_app().test_client()

def test_add_vehicle(app):
    id = 1001
    lat = 0
    lon = 0
    status = VehicleStatus.IDLE

    with app.app_context():
        test_vehicle = Vehicle(id, lat, lon, None, status)
        assert vehicle_add(test_vehicle) == False

def test_request_vehicle(app):
    start_lon = -97.75280733759806
    start_lat = 30.22900303498313
    dest_lon = -97.75324792368177
    dest_lat = 30.238900654991145

    with app.app_context():
        obj = request_vehicle(start_lon, start_lat,dest_lon, dest_lat)
        assert obj.route != None