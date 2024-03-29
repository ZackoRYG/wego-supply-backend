from supply.src.vehicle import Vehicle

class Fleet:
    def __init__(self):
        self.fleet_members = []

    def add_vehicle(self, vehicle):
        self.fleet_members.append(vehicle)
        return True

    def remove_vehicle(self, vehicle):
        if vehicle in self.fleet_members:
            self.fleet_members.remove(vehicle)
            return True
        else:
            return False

    def get_nearest_vehicle(self, location):
        if not self.fleet_members:
            return None
        nearest_vehicle = min(self.fleet_members, key=lambda x: ((x.lat - location[0])**2 + (x.lon - location[1])**2)**0.5)
        return nearest_vehicle
