#!/usr/bin/env python
# -*- coding: utf-8 -*-


import click
from video_subtitler import VideoSubtitlerAppWrapper


def dequote(string):
    """Remove outer quotes if present"""
    string_new = string.strip()
    if (string_new[0] == string_new[-1]) and string_new.startswith(("'", '"')):
        return string_new[1:-1]
    return string_new


@click.command()
@click.option(
    "--filepath_video",
    default="media/nasa_short.mp4",
    help="The file path to the video you want to annotate.",
)
@click.option(
    "--filepath_annotation",
    default="media/annotation.json",
    help="The file path to the json file containing the video annotations.",
)
@click.option(
    "--port", default=5000, help="port number",
)
@click.option("--debug", "-d", is_flag=True, help="Print more output.")
@click.option(
    "--debug", "-d", default=False, is_flag=True, help="Run the app in DEBUG mode.",
)
def run_video_subtitler_app(filepath_video, filepath_annotation, port, debug):

    filepath_video = dequote(filepath_video)
    filepath_annotation = dequote(filepath_annotation)

    app_instance = VideoSubtitlerAppWrapper(
        filepath_video=filepath_video, filepath_annotation=filepath_annotation,
    )

    app_instance.run(debug=debug, port=port)


if __name__ == "__main__":
    run_video_subtitler_app()
