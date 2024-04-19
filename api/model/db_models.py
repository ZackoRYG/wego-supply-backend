from cs_backend.api.model.db_initialization import db

class VehicleTable(db.Model):
    __tablename__ = "vehicle_table"

    id = db.Column(db.Integer, primary_key=True)
    latitude = db.Column(db.Float, nullable=False)
    longitude = db.Column(db.Float, nullable=False)
    status = db.Column(db.String(255), nullable=False)
    route = db.Column(db.String(2048))

    def __repr__(self):
        return f'<Latitude> {self.latitude} <Longitude> {self.longitude} <Status> {self.status}'
    
# with app.app_context():
#     db.create_all()

# userAccount
# CREATE TABLE user_account_table(
#     id INT AUTO_INCREMENT,
#     username VARCHAR(255) NOT NULL,
#     password VARCHAR(255) NOT NULL,
#     PRIMARY KEY (id)
# );
# CREATE TABLE vehicle_table(
#     id INT,
#     latitude FLOAT NOT NULL,
#     longitude FLOAT NOT NULL,
#     status VARCHAR(255) NOT NULL,
#     route VARCHAR(2048) NOT NULL,
#     PRIMARY KEY (id)
# );