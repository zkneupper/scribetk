#!/usr/bin/env python
# -*- coding: utf-8 -*-


# import click
from video_subtitler import VideoSubtitlerAppWrapper


def main():
    debug = True
    filepath_video = "media/nasa_short.mp4"
    filepath_annotation = "media/annotation.json"

    app_instance = VideoSubtitlerAppWrapper(
        filepath_video=filepath_video, filepath_annotation=filepath_annotation,
    )

    app_instance.run(debug=debug)


if __name__ == "__main__":
    main()
