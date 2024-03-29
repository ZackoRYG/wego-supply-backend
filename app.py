from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import DB_CONNECTION, PORT
from api.model.db_initialization import db
from api.model.db_models import CounterTable
from api.route.cs.vehicle_route import vehicle_api

def create_app() -> Flask:
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = f'{DB_CONNECTION}'
    db.init_app(app)

    with app.app_context():
        db.create_all()

    app.register_blueprint(vehicle_api, url_prefix = '/vehicle')
    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True, port=PORT)