import json
from flask import Flask, request, jsonify
from app import app, db
from flask import request, make_response, jsonify
from database.db_models import CounterTable
from flask_cors import cross_origin, CORS
from sqlalchemy.sql import func

@app.route('/get', methods=['GET'])
@cross_origin()
def get_message():
    return 'OK', 200