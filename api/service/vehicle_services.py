from api.model.db_initialization import db
from api.model.db_models import VehicleTable
from sqlalchemy.sql import func

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