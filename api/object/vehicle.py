from enum import Enum

class VehicleStatus(Enum):
    IDLE = "IDLE"
    ON_THE_WAY = "OTW"
    DELIVERY = "DELIVERY"
    MAINTENANCE = "MAINTENANCE"
    ERROR = "ERROR"

class Vehicle:
    def __init__(self, ID, lat, lon, route, status = VehicleStatus.IDLE):
        self.ID = ID
        self.lat = lat
        self.lon = lon
        self.status = status
        self.is_running = False
        self.route = route

    def start(self):
        if not self.is_running:
            self.is_running = True
            print("Vehicle started.")
        else:
            print("Vehicle is already running.")

    def stop(self):
        if self.is_running:
            self.is_running = False
            print("Vehicle stopped.")
        else:
            print("Vehicle is already stopped.")

    def restart(self):
        self.stop()
        self.start()

    def update_location(self, new_lat, new_lon):
        self.lat = new_lat
        self.lon = new_lon
        print("Location updated.")

    def get_location(self):
        return [self.lat, self.lon]
    