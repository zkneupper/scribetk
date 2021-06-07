#!/usr/bin/env python
# -*- coding: utf-8 -*-


# Python standard library
import json
import pathlib
import threading
import webbrowser

# External packages
from flask import (
    Flask,
    jsonify,
    make_response,
    request,
    render_template,
    send_from_directory,
)


class VideoSubtitlerApp:
    def __init__(
        self,
        filepath_video=str(
            pathlib.Path(__file__).absolute().parent / "media/demo_video.mp4",
        ),
        filepath_annotation=str(
            pathlib.Path(__file__).absolute().parent / "media/demo_annotation.json",
        ),
    ):

        self.filepath_video = pathlib.Path(filepath_video)
        self.filepath_annotation = pathlib.Path(filepath_annotation)

        assert (
            self.filepath_video.exists()
        ), f"filepath_video DOES NOT EXIST:\t({self.filepath_video})"

        if not self.filepath_annotation.exists():
            # Create a new self.filepath_annotation if it doesn't exist
            self.filepath_annotation.touch()

        # Define the Flask app
        self.app = Flask(__name__)

        @self.app.route("/")
        def index():
            return render_template("index.html")

        @self.app.route("/video.mp4")
        def video_new():
            return send_from_directory(
                self.filepath_video.parent, self.filepath_video.name,
            )

        @self.app.route("/annotation.json")
        def annotation_new():
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

    def open_browser(self):
        """Open link to the app in the browser.

        Start new thread to open web browser.
        """

        def _open_browser():
            webbrowser.open_new(self.url)

        t = threading.Timer(0, _open_browser)
        t.start()

    def run(self, host=None, port=None, debug=None, load_dotenv=True, **options):

        browser = True

        if browser:
            # Automatically open in browser
            self.url = f"http://127.0.0.1:{port}/"
            self.open_browser()

        self.app.run(
            host=host, port=port, debug=debug, load_dotenv=load_dotenv, **options
        )
