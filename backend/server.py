import os
from flask import Flask, jsonify, redirect, url_for
from flask import request
from flask.ext.cors import CORS
from utils import *
app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    a_long = float(request.args.get('a_long'))
    a_lat = float(request.args.get('a_lat'))
    b_long = float(request.args.get('b_long'))
    b_lat = float(request.args.get('b_lat'))
    c_long, c_lat = get_c(a_long, a_lat, b_long, b_lat)
    return jsonify({"c_long": c_long, "c_lat": c_lat})

PORT = int(os.environ.get('PORT', 5000))
print("Running on port " + str(PORT))
app.run(host='0.0.0.0', port=PORT)
