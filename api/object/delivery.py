class Delivery:
    def __init__(self, vehicle_id, start_longitude, start_latitude, destination_longitude, destination_latitude):
        self.vehicle_id = vehicle_id
        self.start_longitude = start_longitude
        self.start_latitude = start_latitude
        self.destination_longitude = destination_longitude
        self.destination_latitude = destination_latitude

    def get_vehicle_id(self):
        return self.vehicle_id

    def set_vehicle_id(self, value):
        self.vehicle_id = value

    def get_start_longitude(self):
        return self.start_longitude

    def set_start_longitude(self, value):
        self.start_longitude = value

    def get_start_latitude(self):
        return self.start_latitude

    def set_start_latitude(self, value):
        self.start_latitude = value

    def get_destination_longitude(self):
        return self.destination_longitude

    def set_destination_longitude(self, value):
        self.destination_longitude = value

    def get_destination_latitude(self):
        return self.destination_latitude

    def set_destination_latitude(self, value):
        self.destination_latitude = value
