#!/usr/bin/env python
# -*- coding: utf-8 -*-


# Python standard library
import json
import pathlib
import re
import sys

# External packages
import pandas as pd
from flask import (
    Flask,
    jsonify,
    make_response,
    redirect,
    request,
    render_template,
    send_from_directory,
    url_for,
)


# Define the Flask app
app = Flask(__name__)


filepath_json = "media/nasa.json"
filepath_json = pathlib.Path(filepath_json)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/media/nasa.json")
def annotation():
    return send_from_directory("media", "nasa.json")


@app.route("/media/nasa.mp4")
def video():
    return send_from_directory("media", "nasa.mp4")


@app.route("/endpoint", methods=["POST"])
def my_function():
    data = request.get_json()

    # Sort the list of annotation dictionaries
    # so that they are ordered by the start time of each annotation.
    data = sorted(data, key=lambda k: k["start"])

    res = make_response(jsonify({"message": "JSON received"}), 200)

    print(f"Saving file to : {filepath_json}")

    with open(filepath_json, "w") as file:
        json.dump(data, file, indent=4)

    return res


if __name__ == "__main__":
    app.run(debug=True)
