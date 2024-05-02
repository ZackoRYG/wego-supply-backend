import pytest #testing

from api.object.fleet import Fleet
from api.object.vehicle import Vehicle

@pytest.fixture
def fleet():
    return Fleet()

@pytest.fixture
def vehicle():
    return Vehicle(1, lat=10.0, lon=20.0, route=[])

def test_add_vehicle(fleet, vehicle):
    assert fleet.add_vehicle(vehicle) == True
    assert vehicle in fleet.fleet_members

def test_remove_vehicle(fleet, vehicle):
    fleet.add_vehicle(vehicle)
    assert fleet.remove_vehicle(vehicle) == True
    assert vehicle not in fleet.fleet_members

def test_remove_nonexistent_vehicle(fleet, vehicle):
    assert fleet.remove_vehicle(vehicle) == False

def test_get_nearest_vehicle(fleet):
    vehicle1 = Vehicle(1, lat=10.0, lon=20.0, route=[])
    vehicle2 = Vehicle(2, lat=20.0, lon=30.0, route=[])
    vehicle3 = Vehicle(3, lat=30.0, lon=40.0, route=[])

    fleet.add_vehicle(vehicle1)
    fleet.add_vehicle(vehicle2)
    fleet.add_vehicle(vehicle3)

    # Simulating a location
    location = [15.0, 25.0]
    nearest_vehicle = fleet.get_nearest_vehicle(location)

    assert nearest_vehicle == vehicle1