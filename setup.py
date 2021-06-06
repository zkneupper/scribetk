#!/usr/bin/env python
# -*- coding: UTF-8 -*-

"""The setup script."""


from setuptools import setup, find_packages


setup(
    python_requires=">=3.6",
    name="video_subtitler",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    include_package_data=True,
    entry_points={"console_scripts": ["video_subtitler = video_subtitler:cli"]},
)
