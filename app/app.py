#!/usr/bin/env python
# -*- coding: utf-8 -*-


# Python standard library
import json
import pathlib

# External packages
from flask import (
    Flask,
    jsonify,
    make_response,
    request,
    render_template,
    send_from_directory,
)


# Define the Flask app
app = Flask(__name__)


filepath_json = "media/nasa_short.json"
filepath_json = pathlib.Path(filepath_json)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/video.mp4")
def video_new():
    filepath_video = "media/nasa_short.mp4"
    filepath_video = pathlib.Path(filepath_video)

    if not filepath_video.exists():
        print(f"filepath_video DOES NOT EXIST:\t({filepath_video})")

    return send_from_directory(filepath_video.parent, filepath_video.name)


@app.route("/annotation.json")
def annotation_new():
    filepath_annotation = "media/annotation.json"
    filepath_annotation = pathlib.Path(filepath_annotation)

    if not filepath_annotation.exists():
        print(f"filepath_annotation DOES NOT EXIST:\t({filepath_annotation})")

    return send_from_directory(filepath_annotation.parent, filepath_annotation.name)


@app.route("/endpoint", methods=["POST"])
def my_function():
    data = request.get_json()

    # Sort the list of annotation dictionaries
    # so that they are ordered by the start time of each annotation.
    data = sorted(data, key=lambda k: k["start"])

    res = make_response(jsonify({"message": "JSON received"}), 200)

    print(f"Saving file to : {filepath_json}")

    with open(filepath_json, "w") as file:
        # json.dump(data, file, indent=4)

        # Have newline at end of json file
        file.write(f"{json.dumps(data, indent=4)}\n")

    return res


if __name__ == "__main__":
    app.run(debug=True)
