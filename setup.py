
"""
RoboMaster SDK is based on the Python language and is suitable for the Python SDK software library
 of the RoboMater series.
Currently applicable to RoboMaster EP and Tello Edu and other products, it provides a rich API interface,
including: motion control, flight control, intelligent identification, lighting effect settings, data push,
video streaming and audio streaming APIs. And the design follows the principle of being as simple as possible,
and can be quickly used to facilitate learning and teaching. Based on each API interface,
there are code examples, you can refer to our developer documentation robomaster-dev.readthedocs.io.
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
