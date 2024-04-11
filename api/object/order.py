from enum import Enum

class Order_Status(Enum):
    DONE = "DONE"
    CONFIRM = "CONFIRM"
    IN_TRANSIT = "IN TRANSIT"
    CANCELED = "CANCELED"

class Order:
    def __init__(self, order_number, order_customer, destination_longitude, destination_latitude, source_longitude, source_latitude, assigned_vehicle, order_status):
        self.order_number = order_number
        self.order_customer = order_customer
        self.destination_longitude = destination_longitude
        self.destination_latitude = destination_latitude
        self.source_longitude = source_longitude
        self.source_latitude = source_latitude
        self.assigned_vehicle = assigned_vehicle
        self.order_status = order_status

    def get_order_number(self):
        return self.order_number

    def set_order_number(self, value):
        self.order_number = value

    def get_order_customer(self):
        return self.order_customer

    def set_order_customer(self, value):
        self.order_customer = value

    def get_destination_longitude(self):
        return self.destination_longitude

    def set_destination_longitude(self, value):
        self.destination_longitude = value

    def get_destination_latitude(self):
        return self.destination_latitude

    def set_destination_latitude(self, value):
        self.destination_latitude = value

    def get_source_longitude(self):
        return self.source_longitude

    def set_source_longitude(self, value):
        self.source_longitude = value

    def get_source_latitude(self):
        return self.source_latitude

    def set_source_latitude(self, value):
        self.source_latitude = value

    def get_assigned_vehicle(self):
        return self.assigned_vehicle

    def set_assigned_vehicle(self, value):
        self.assigned_vehicle = value

    def get_order_status(self):
        return self.order_status
    
    def set_order_status(self, value):
        self.order_status = value
