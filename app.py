from collections import namedtuple
import json
from random import choice
from flask import Flask, jsonify
from flask_cors import CORS, cross_origin

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route("/", methods=["GET"])
@cross_origin()
def hello_world():
    data = {'data':'Hello World!'}
    return data, 200 # data is automatically 'jsonify' and the '200' corresponds to the status code