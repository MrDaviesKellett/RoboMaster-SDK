"""
Compatibility wrapper for the historical media-enabled build entrypoint.

The standard `setup.py` and PyPI build path now include `libmedia_codec` by default.
"""

from setuptools import find_packages
from setuptools import setup

from setup_support import base_setup_kwargs
from setup_support import ensure_pybind11
from setup_support import ensure_supported_python


ensure_supported_python()
ensure_pybind11()

setup(
    long_description=__doc__,
    packages=find_packages("src"),
    package_data={"robomaster": ["LICENSE.txt", "README.md"]},
    **base_setup_kwargs(),
)
