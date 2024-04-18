from api.model.db_initialization import db
from api.model.db_models import VehicleTable
from sqlalchemy.sql import func
from api.object.vehicle import Vehicle


# Count Order POST
def add_counter():
    pass
    # THIS IS DEPRECIATED
    # db.session.add(CounterTable(count=1))
    # db.session.commit()

# Count Order GET
def sum_counter():
    # THIS IS DEPRECIATED
    # sums "count" field of all values
    # in the database
    # int(db.session.query(func.sum(CounterTable.count)).scalar())
    return 0

def vehicle_heartbeat_status(vehicle_id):
    obj = None
    db_selection = db.session.query(VehicleTable).filter_by(id=vehicle_id).scalar()
    if (db_selection != None):
        obj = Vehicle(
            vehicle_id,
            db_selection.latitude,
            db_selection.longitude,
            db_selection.route,
            db_selection.status
            )
        
    return obj