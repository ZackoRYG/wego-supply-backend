from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import DB_CONNECTION

db = SQLAlchemy()


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = f'{DB_CONNECTION}'
db.init_app(app)

# from demand_models import CounterTable
with app.app_context():
    db.create_all()

from sample_api import *

if __name__ == "__main__":
    app.run(host='0.0.0.0')