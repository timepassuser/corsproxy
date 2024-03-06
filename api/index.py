from flask import Flask
from flask import request
from flask import make_response
import requests
app = Flask(__name__)

@app.route("/<path:a>", methods=["GET", "OPTIONS"])
def hello(a):
    if request.method == "OPTIONS":
        print("\n\n\nOPTIOnS HERE\n\n\n")
    print('\n\nNew request here\n', request, '\n', request.headers)
    response = make_response(f"Hi {request}  <br>  {request.headers}")
    response.access_control_allow_origin = '*'
    return response
    
