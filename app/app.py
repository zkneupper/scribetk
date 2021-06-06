#!/usr/bin/env python
# -*- coding: utf-8 -*-


import click
from video_subtitler import VideoSubtitlerAppWrapper


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
    "--port", default=5000, prompt="port number", help="port number",
)
@click.option("--debug", "-d", is_flag=True, help="Print more output.")
@click.option(
    "--debug",
    "-d",
    default=False,
    is_flag=True,
    prompt="debug:",
    help="Run the app in DEBUG mode.",
)
def run_video_subtitler_app(filepath_video, filepath_annotation, port, debug):

    app_instance = VideoSubtitlerAppWrapper(
        filepath_video=filepath_video, filepath_annotation=filepath_annotation,
    )

    app_instance.run(debug=debug, port=port)


if __name__ == "__main__":
    run_video_subtitler_app()
