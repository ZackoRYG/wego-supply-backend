# NOT NEEDED
from app import app
from flask import request

@app.route("/call-backend", methods=['POST'])
def sample_api():
    print("backend hit")
    request_body = request.get_json()
    return 200, "200 OK!"