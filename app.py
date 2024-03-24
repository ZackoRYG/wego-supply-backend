from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import DB_CONNECTION, PORT

from schema.db_initialization import db

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = f'{DB_CONNECTION}'
db.init_app(app)

from schema.db_models import CounterTable
with app.app_context():
    db.create_all()

from api.sample_api import *
from api.vehicle_request import *
from api.react_request import *

if __name__ == "__main__":
    app.run(debug=True, port=f'{PORT}') 