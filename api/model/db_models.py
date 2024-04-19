from cs_backend.api.model.db_initialization import db

class VehicleTable(db.Model):
    __tablename__ = "vehicle_table"

    id = db.Column(db.Integer, primary_key=True)
    latitude = db.Column(db.Float, nullable=False)
    longitude = db.Column(db.Float, nullable=False)
    status = db.Column(db.String(255), nullable=False)
    route = db.Column(db.String(2048))

    def __repr__(self):
        return f'<Latitude> {self.latitude} <Longitude> {self.longitude} <IsRunning> {self.isRunning}'