from enum import Enum

class Vehicle_Status(Enum):
    IDLE = "IDLE"
    DELIVERY = "DELIV"
    MAINTENANCE = "MAINT"
    ERROR = "ERROR"

class Vehicle:
    def __init__(self, ID, lat, lon, status=Vehicle_Status.IDLE):
        self.ID = ID
        self.lat = lat
        self.lon = lon
        self.status = status
        self.is_running = False
        self.route = list()

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
    