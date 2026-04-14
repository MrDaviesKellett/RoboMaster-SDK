"""
Compatibility wrapper for the historical media-enabled build entrypoint.

The standard `setup.py` and PyPI build path now include `libmedia_codec` by default.
"""

import os
import sys

from setuptools import find_packages
from setuptools import setup

PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

from setup_support import base_setup_kwargs
from setup_support import ensure_supported_python


ensure_supported_python()

setup(
    long_description=__doc__,
    packages=find_packages("src"),
    package_data={"robomaster": ["LICENSE.txt", "README.md"]},
    **base_setup_kwargs(),
)
