from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from cs_backend.config import DB_CONNECTION, PORT, DEBUG
from cs_backend.api.model.db_initialization import db
from cs_backend.api.model.db_models import *
from supply_backend.api.model.db_models import *
from supply_backend.api.route.vehicle_route import vehicle_api
from supply_backend.api.route.data_route import data_api
from cs_backend.api.route.user_route import user_api

def create_app() -> Flask:
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = f'{DB_CONNECTION}'
    db.init_app(app)

    CORS(app)

    if DEBUG:
        with app.app_context():
            db.create_all()

    app.register_blueprint(vehicle_api, url_prefix = '/api/vehicles')
    app.register_blueprint(data_api, url_prefix = '/api/data')
    app.register_blueprint(user_api, url_prefix = '/api/user')
    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=DEBUG, port=PORT)