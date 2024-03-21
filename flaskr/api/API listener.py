import json
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/get', methods=['GET'])
def get_role():
    return 'OK', 200

app.run(debug=False)