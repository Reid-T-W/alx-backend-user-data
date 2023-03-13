#!/usr/bin/env python3
""" Route module for app """
from flask import Flask, jsonify


app = Flask(__name__)


@app.route('/', methods=['GET'])
def get_json():
    """ Gets a static json message """
    return jsonify({"message": "Bienvenue"})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
