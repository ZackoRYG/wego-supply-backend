from api.model.db_initialization import db

class UserAccountTable(db.Model):
    __tablename__ = "user_account_table"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255), nullable=False)
    password = db.Column(db.String(255), nullable=False)

    def __repr__(self):
        return f'<Username> {self.username} <Password> {self.password}'

class VehicleTable(db.Model):
    __tablename__ = "vehicle_table"

    id = db.Column(db.Integer, primary_key=True)
    latitude = db.Column(db.Float, nullable=False)
    longitude = db.Column(db.Float, nullable=False)
    isRunning = db.Column(db.Boolean, nullable=False)

    def __repr__(self):
        return f'<Latitude> {self.latitude} <Longitude> {self.longitude} <IsRunning> {self.isRunning}'
    
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
#     id INT AUTO_INCREMENT,
#     latitude FLOAT NOT NULL,
#     longitude FLOAT NOT NULL,
#     is_running BOOLEAN NOT NULL DEFAULT FALSE,
#     PRIMARY KEY (id)
# );