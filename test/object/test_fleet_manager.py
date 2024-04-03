import pytest #testing
from api.object.fleet import Fleet
from api.object.fleet_manager import FleetManager

@pytest.fixture
def fleet_manager():
    return FleetManager()

@pytest.fixture
def fleet():
    return Fleet()

@pytest.fixture
def vehicle():
    return "Vehicle"

def test_add_fleet(fleet_manager, fleet):
    assert fleet_manager.add_fleet(fleet) == True
    assert fleet_manager.fleet == fleet

def test_add_existing_fleet(fleet_manager, fleet):
    fleet_manager.add_fleet(fleet)
    assert fleet_manager.add_fleet(Fleet()) == False

def test_remove_fleet(fleet_manager, fleet):
    fleet_manager.add_fleet(fleet)
    assert fleet_manager.remove_fleet(fleet) == True
    assert fleet_manager.fleet == None

def test_remove_non_existing_fleet(fleet_manager, fleet):
    assert fleet_manager.remove_fleet(fleet) == False
