#!/usr/bin/env python
# -*- coding: utf-8 -*-


# Python standard library
import pathlib

# External packages
import click
from scribetk import VideoSubtitlerApp


def dequote(string):
    """Remove outer quotes if present"""
    string_new = string.strip()
    if (string_new[0] == string_new[-1]) and string_new.startswith(("'", '"')):
        return string_new[1:-1]
    return string_new


@click.command()
@click.option(
    "--video",
    "-v",
    default=str(pathlib.Path(__file__).absolute().parent / "media/demo_video.mp4"),
    help="The file path to the video you want to annotate.",
)
@click.option(
    "--note",
    "-n",
    default=str(
        pathlib.Path(__file__).absolute().parent / "media/demo_annotation.json",
    ),
    help="The file path to the json file containing the video annotations.",
)
@click.option(
    "--host", default="127.0.0.1", help="host",
)
@click.option(
    "--port", "-p", default=5000, help="port number",
)
@click.option(
    "--debug", "-d", default=False, is_flag=True, help="Run the app in DEBUG mode.",
)
@click.option(
    "--browser/--no-browser",
    default=True,
    is_flag=True,
    help="Automatically open in browser",
)
def cli(video, note, host, port, debug, browser):

    filepath_video = dequote(video)
    filepath_annotation = dequote(note)

    filepath_video = pathlib.Path(filepath_video).absolute()
    filepath_annotation = pathlib.Path(filepath_annotation).absolute()

    print(filepath_video)
    print(filepath_video.exists())
    print(filepath_annotation)
    print(filepath_annotation.exists())

    app_instance = VideoSubtitlerApp(
        filepath_video=filepath_video, filepath_annotation=filepath_annotation,
    )

    app_instance.run(debug=debug, host=host, port=port)


if __name__ == "__main__":
    cli()
