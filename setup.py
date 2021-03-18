#!/usr/bin/env python
from setuptools import setup
from truck_telemetry import version

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="truck_telemetry",
    version=version.FULL,
    description="SCS Telemetry for EuroTruckSimulator 2 and AmericanTruckSimulator",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Dreagonmon",
    author_email="531486058@qq.com",
    url="https://github.com/dreagonmon/truck_telemetry",
    install_requires=[],
    packages=['truck_telemetry', "truck_telemetry.telemetry_version"],
    keywords=["development"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
    ],
    python_requires='>=3.6',
)

# python mpypack\cli.py