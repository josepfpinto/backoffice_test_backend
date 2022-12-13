from collections import namedtuple
import json
from random import choice
from flask_cors import CORS, cross_origin
from flask import Flask, request, jsonify, make_response


def _build_cors_preflight_response():
    response = make_response()
    response.headers.add("Access-Control-Allow-Origin", "*")
    response.headers.add('Access-Control-Allow-Headers', "*")
    response.headers.add('Access-Control-Allow-Methods', "*")
    return response


def _corsify_actual_response(response):
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response


app = Flask(__name__)


@app.route("/", methods=["GET", "OPTIONS"])
def api_create_order():
    if request.method == "OPTIONS": # CORS preflight
        return _build_cors_preflight_response()
    elif request.method == "GET": # The actual request following the preflight
        data = {'data':'Hello World!'}
        return _corsify_actual_response(jsonify(data))
    else:
        raise RuntimeError("Sorry, don't know how to handle method {}".format(request.method))
