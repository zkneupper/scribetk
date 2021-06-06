#!/usr/bin/env python
# -*- coding: utf-8 -*-


import click
from video_subtitler import VideoSubtitlerAppWrapper


# @click.option("--debug",  default=1 prompt="Your name", help="The person to greet.")
# def run_video_subtitler_app(filepath_video, filepath_annotation, debug):


@click.command()
@click.option(
    "--filepath_video",
    default="media/nasa_short.mp4",
    prompt="filepath_video:",
    help="The file path to the video you want to annotate.",
)
@click.option(
    "--filepath_annotation",
    default="media/annotation.json",
    prompt="filepath_annotation:",
    help="The file path to the json file containing the video annotations.",
)
@click.option(
    "--port", default=None, prompt="port number: (e.g., 5000)", help="port number",
)
def run_video_subtitler_app(filepath_video, filepath_annotation, port):
    debug = True

    app_instance = VideoSubtitlerAppWrapper(
        filepath_video=filepath_video, filepath_annotation=filepath_annotation,
    )

    app_instance.run(debug=debug, port=port)


if __name__ == "__main__":
    run_video_subtitler_app()
