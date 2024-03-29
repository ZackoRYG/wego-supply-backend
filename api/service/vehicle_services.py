from api.model.db_initialization import db
from api.model.db_models import CounterTable
from sqlalchemy.sql import func

def add_counter():
    db.session.add(CounterTable(count=1))
    db.session.commit()

def sum_counter():
    # sums "count" field of all values
    # in the database
    return int(db.session.query(func.sum(CounterTable.count)).scalar())