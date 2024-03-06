from flask import Flask
from flask import request
from flask import make_response
import requests
app = Flask(__name__)

@app.route("/<path:url>", methods=["GET", "OPTIONS"])
def hello(url):
    print('\n\nNew request here\n', request, '\n', request.headers)

    if request.method == "OPTIONS":
        response = make_response()
        response.access_control_allow_origin = '*'
        response.access_control_allow_headers = ["corsproxy"]
        print(f"Sending response to options\n{response.headers}")
        return response

    if "https://" not in url:
        return "Invalid url"
    elif "cdn3.digialm.com" not in url:
        return "Invalid url"
    elif ".html" not in url:
        return "Invalid url"
    elif "Corsproxy" not in request.headers.keys():
        return "Invalid request"
    else:
        try:
            r = requests.get(url, timeout=0.5)
            if r.status_code == requests.codes.ok:
                response = make_response(r.text)
            else:
                print(f"Something went wrong, status code {r.status_code}")
                response = make_response(f"Something went wrong, status code {r.status_code}")
            
        except Exception as exception:
            print(f"An error occured {exception}")
            response = make_response(f"An error occured {exception}")
        finally:
            response.access_control_allow_origin = '*'
            response.access_control_allow_headers = ["corsproxy"]
            return response

    
