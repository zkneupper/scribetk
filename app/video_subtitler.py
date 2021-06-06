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


class VideoSubtitlerAppWrapper:
    def __init__(
        self,
        filepath_video="media/nasa_short.mp4",
        filepath_annotation="media/annotation.json",
    ):

        # Set paths to the video file and annotation file
        self.filepath_video = pathlib.Path(filepath_video)
        self.filepath_annotation = pathlib.Path(filepath_annotation)

        # Define the Flask app
        self.app = Flask(__name__)

        @self.app.route("/")
        def index():
            return render_template("index.html")

        @self.app.route("/video.mp4")
        def video_new():
            # filepath_video = "media/nasa_short.mp4"
            # filepath_video = pathlib.Path(filepath_video)

            if not self.filepath_video.exists():
                print(f"filepath_video DOES NOT EXIST:\t({self.filepath_video})")

            return send_from_directory(
                self.filepath_video.parent, self.filepath_video.name,
            )

        @self.app.route("/annotation.json")
        def annotation_new():
            # filepath_annotation = "media/annotation.json"
            # filepath_annotation = pathlib.Path(filepath_annotation)

            if not self.filepath_annotation.exists():
                print(
                    f"filepath_annotation DOES NOT EXIST:\t({self.filepath_annotation})",
                )

            return send_from_directory(
                self.filepath_annotation.parent, self.filepath_annotation.name,
            )

        @self.app.route("/endpoint", methods=["POST"])
        def my_function():
            data = request.get_json()

            # Sort the list of annotation dictionaries
            # so that they are ordered by the start time of each annotation.
            data = sorted(data, key=lambda k: k["start"])

            res = make_response(jsonify({"message": "JSON received"}), 200)

            print(f"Saving file to : {self.filepath_annotation}")

            with open(self.filepath_annotation, "w") as file:
                # json.dump(data, file, indent=4)

                # Have newline at end of json file
                file.write(f"{json.dumps(data, indent=4)}\n")

            return res

    def run(self, debug=False):
        self.app.run(debug=debug)
