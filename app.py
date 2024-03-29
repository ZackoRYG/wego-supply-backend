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


from api.route.vehicle import vehicle_api
app.register_blueprint(vehicle_api, url_prefix = '/vehicle')

from api.route.sample_api import *

# from api.route.react_request import *


'''
def create_app() -> Flask:
    app = Flask(__name__)
    app.register_blueprint(vehicle_api, url_prefix = '/vehicle')
    return app
'''


if __name__ == "__main__":
    app.run(debug=True, port=f'{PORT}') 