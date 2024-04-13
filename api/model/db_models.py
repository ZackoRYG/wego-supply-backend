from cs_backend.api.model.db_initialization import db

class VehicleTable(db.Model):
    __tablename__ = "vehicle_table"

    id = db.Column(db.Integer, primary_key=True)
    latitude = db.Column(db.Float, nullable=False)
    longitude = db.Column(db.Float, nullable=False)
    isRunning = db.Column(db.Boolean, nullable=False)

    def __repr__(self):
        return f'<Latitude> {self.latitude} <Longitude> {self.longitude} <IsRunning> {self.isRunning}'