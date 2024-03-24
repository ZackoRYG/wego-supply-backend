import json
from flask import Flask, request, jsonify
from app import app, db
from flask import request, make_response, jsonify
from database.db_models import CounterTable
from flask_cors import cross_origin, CORS
from sqlalchemy.sql import func

def add_counter():
    db.session.add(CounterTable(count=1))
    db.session.commit()

@app.route("/vehicle-request", methods=['POST'])
@cross_origin()
def vehicle_request():
    add_counter()
    print("backend hit")
    request_body = request.get_json
    return make_response("200 OK!", 200)