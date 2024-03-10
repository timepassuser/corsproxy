from flask import Flask
from flask import request
from flask import make_response
import requests
app = Flask(__name__)

allowedOrigin = 'https://timepassuser.github.io'
allowedHeaders = ["corsproxy", "urltofetch"]

@app.route("/", methods=["GET", "OPTIONS"])
def hello():
    print('\n\nNew request here\n', request, '\n', request.headers)

    if request.method == "OPTIONS":
        response = make_response()
        response.access_control_allow_origin = allowedOrigin
        response.access_control_allow_headers = allowedHeaders
        print(f"Sending response to options\n{response.headers}")
        return response

    if "Corsproxy" not in request.headers.keys() or "Urltofetch" not in request.headers.keys():
        response = make_response("Invalid Request")
    else:
        url = request.headers["Urltofetch"]

        if "https://" not in url:
            response = make_response("Invalid url")
        elif "cdn3.digialm.com" not in url:
            response = make_response("Invalid url")
        elif ".html" not in url:
            response = make_response("Invalid url")
        else:
            try:
                r = requests.get(url, timeout=1)
                if r.status_code == requests.codes.ok:
                    response = make_response(r.text)
                else:
                    print(f"Something went wrong, status code {r.status_code}")
                    response = make_response(f"Something went wrong, status code {r.status_code}")
            except Exception as exception:
                print(f"An error occured {exception}")
                response = make_response(f"An error occured {exception}")
        # finally:
            # response.access_control_allow_origin = '*'
            # response.access_control_allow_headers = ["corsproxy", "urlToFetch"]
            # return response
        # response = make_response("This is just to show it works")
    response.access_control_allow_origin = allowedOrigin
    response.access_control_allow_headers = allowedHeaders
    return response
