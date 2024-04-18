import pytest

from supply_backend.api.object.vehicle import Vehicle

@pytest.fixture
def vehicle():
    return Vehicle(ID=1, lat=0.0, lon=0.0)

def test_start(vehicle):
    vehicle.start()
    assert vehicle.is_running

def test_stop(vehicle):
    vehicle.is_running = True
    vehicle.stop()
    assert not vehicle.is_running

def test_restart(vehicle):
    vehicle.is_running = True
    vehicle.restart()
    assert vehicle.is_running

def test_update_location(vehicle):
    new_lat, new_lon = 10.0, 20.0
    vehicle.update_location(new_lat, new_lon)
    assert vehicle.lat == new_lat
    assert vehicle.lon == new_lon

def test_get_location(vehicle):
    assert vehicle.get_location() == [vehicle.lat, vehicle.lon]
