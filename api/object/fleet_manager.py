from api.object.user import User

class FleetManager:
    def __init__(self):
        self.fleet = None

    def add_fleet(self, fleet):
        if not self.fleet:
            self.fleet = fleet
            print("Fleet added.")
            return True
        else:
            print("Fleet already exists.")
            return False

    def remove_fleet(self, fleet):
        if self.fleet == fleet:
            self.fleet = None
            print("Fleet removed.")
            return True
        else:
            print("Fleet not found.")
            return False
