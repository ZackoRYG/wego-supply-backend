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
    
class DeliveryTable(db.Model):
    __tablename__ = "delivery_table"

    vehicle_id = db.Column(db.Integer, primary_key=True)
    start_latitude = db.Column(db.Float, nullable=False)
    start_longitude = db.Column(db.Float, nullable=False)
    end_latitude = db.Column(db.Float, nullable=False)
    end_longitude = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return f'<Latitude> {self.latitude} <Longitude> {self.longitude} <IsRunning> {self.isRunning}'

# CREATE TABLE vehicle_table(
#     id INT AUTO_INCREMENT,
#     latitude FLOAT NOT NULL,
#     longitude FLOAT NOT NULL,
#     route VARCHAR(2048) DEFAULT "[]",
#     status VARCHAR(255) NOT NULL,
#     PRIMARY KEY (id)
# );
# CREATE TABLE delivery_table(
#     vehicle_id INT,
#     start_latitude FLOAT NOT NULL,
#     start_longitude FLOAT NOT NULL,
#     end_latitude FLOAT NOT NULL,
#     end_longitude FLOAT NOT NULL,
#     FOREIGN KEY (vehicle_id) REFERENCES vehicle_table(id)
# );