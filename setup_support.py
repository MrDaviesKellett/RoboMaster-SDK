"""
Shared packaging helpers for the RoboMaster SDK distribution.
"""

import os
import sys


PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))
MIN_PYTHON = (3, 14)


def ensure_supported_python():
    if sys.version_info < MIN_PYTHON:
        sys.exit("RoboMaster SDK requires Python 3.14 or later")


def fetch_version():
    with open(os.path.join(PROJECT_ROOT, "src", "robomaster", "version.py")) as file_obj:
        namespace = {}
        exec(file_obj.read(), namespace)
        return namespace["__version__"]




def base_setup_kwargs():
    return {
        "name": "robomaster-sdk-modern",
        "version": fetch_version(),
        "description": "Community-maintained RoboMaster Python SDK fork for Python 3.14+",
        "long_description_content_type": "text/markdown",
        "author": "EDU SDK TEAM",
        "license": "Apache License, Version 2.0",
        "keywords": "dji robomaster sdk robot drone".split(),
        "url": "https://robomaster-dev.rtfd.io/",
        "python_requires": ">=3.14",
        "package_dir": {"": "src"},
        "install_requires": [
            "av >= 16.1.0",
            "numpy >= 2.3.4",
            "opencv-python >= 4.13.0.92",
            "psutil >= 7.2.2",
        ],
        "extras_require": {
            "qrcode": ["MyQR >= 2.3.1"],
        },
        "classifiers": [
            "Programming Language :: Python :: 3",
            "Programming Language :: Python :: 3 :: Only",
            "Programming Language :: Python :: 3.14",
        ],
        "zip_safe": True,
    }
