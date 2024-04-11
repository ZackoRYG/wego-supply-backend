import pytest
from api.object.order import Order, Order_Status

@pytest.fixture
def sample_order():
    return Order(
        order_number="123",
        order_customer="John Doe",
        destination_longitude=45.678,
        destination_latitude=-67.890,
        source_longitude=12.345,
        source_latitude=-56.789,
        assigned_vehicle="Truck",
        order_status=Order_Status.CONFIRM
    )

def test_order_number(sample_order):
    assert sample_order.get_order_number() == "123"
    sample_order.set_order_number("456")
    assert sample_order.get_order_number() == "456"

def test_order_customer(sample_order):
    assert sample_order.get_order_customer() == "John Doe"
    sample_order.set_order_customer("Jane Smith")
    assert sample_order.get_order_customer() == "Jane Smith"

def test_destination_longitude(sample_order):
    assert sample_order.get_destination_longitude() == 45.678
    sample_order.set_destination_longitude(78.901)
    assert sample_order.get_destination_longitude() == 78.901

def test_destination_latitude(sample_order):
    assert sample_order.get_destination_latitude() == -67.890
    sample_order.set_destination_latitude(-23.456)
    assert sample_order.get_destination_latitude() == -23.456

def test_source_longitude(sample_order):
    assert sample_order.get_source_longitude() == 12.345
    sample_order.set_source_longitude(34.567)
    assert sample_order.get_source_longitude() == 34.567

def test_source_latitude(sample_order):
    assert sample_order.get_source_latitude() == -56.789
    sample_order.set_source_latitude(-89.012)
    assert sample_order.get_source_latitude() == -89.012

def test_assigned_vehicle(sample_order):
    assert sample_order.get_assigned_vehicle() == "Truck"
    sample_order.set_assigned_vehicle("Van")
    assert sample_order.get_assigned_vehicle() == "Van"

def test_order_status(sample_order):
    assert sample_order.get_order_status() == Order_Status.CONFIRM
    sample_order.set_order_status(Order_Status.DONE)
    assert sample_order.get_order_status() == Order_Status.DONE
