#!/usr/bin/env python
# -*- coding: UTF-8 -*-

"""The setup script."""


from setuptools import setup, find_packages


setup(
    python_requires=">=3.6",
    name="scribetk",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    include_package_data=True,
    package_data={"src": ["src/*"]},
    # package_data = {
    #     '': ['*'],
    # },
    # package_data = {
    #     'media': ['*'],
    #     'static': ['*'],
    #     'templates': ['*'],
    # },
    # data_files=[
    # 	('media', ['*']),
    #     ('static', ['*']),
    #     ('templates', ['*']),
    # ],
    entry_points={"console_scripts": ["scribetk = scribetk:cli"]},
)
