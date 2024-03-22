import json
from flask import Flask, request, jsonify
from app import app, db
from flask import request, make_response, jsonify
from database.db_models import CounterTable
from flask_cors import cross_origin, CORS
from sqlalchemy.sql import func

def sum_counter():
    # sums "count" field of all values
    # in the database
    return int(db.session.query(func.sum(CounterTable.count)).scalar())

@app.route("/retrieve-counter", methods=['GET'])
@cross_origin()
def counter_return():
    sum = sum_counter()
    print(f"attempting to send GET: {sum}")
    return jsonify(
        {
            "count_sum": sum
        }
    )