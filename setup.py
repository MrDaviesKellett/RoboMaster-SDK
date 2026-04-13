
"""
RoboMaster SDK is based on the Python language and is suitable for the Python SDK software library
 of the RoboMater series.
Currently applicable to RoboMaster EP and Tello Edu and other products, it provides a rich API interface,
including: motion control, flight control, intelligent identification, lighting effect settings, data push,
video streaming and audio streaming APIs. And the design follows the principle of being as simple as possible,
and can be quickly used to facilitate learning and teaching. Based on each API interface,
there are code examples, you can refer to our developer documentation robomaster-dev.readthedocs.io.
"""

from setuptools import setup, find_packages
import os.path
import sys
if sys.version_info < (3, 14):
    sys.exit("RoboMaster SDK requires Python 3.14 or later")

curr = os.path.abspath(os.path.dirname(__file__))


def fetch_version():
    with open(os.path.join(curr, 'src', 'robomaster', 'version.py')) as f:
        ns = {}
        exec(f.read(), ns)
        return ns


version_data = fetch_version()
version = version_data['__version__']


setup(
    name='robomaster-sdk-modern',
    version=version,
    description="Community-maintained RoboMaster Python SDK fork for Python 3.14+",
    long_description=__doc__,
    long_description_content_type="text/markdown",
    author='EDU SDK TEAM',
    license='Apache License, Version 2.0',
    zip_safe=True,
    keywords='dji robomaster sdk robot drone'.split(),
    url="https://robomaster-dev.rtfd.io/",
    python_requires=">=3.14",
    package_dir={'': 'src'},
    packages=find_packages('src'),
    package_data={
      'robomaster': ['LICENSE.txt', 'README.md']
    },
    install_requires=[
        'numpy >= 2.3.4',
        'opencv-python >= 4.13.0.92',
        'psutil >= 7.2.2',
    ],
    extras_require={
        'qrcode': ['MyQR >= 2.3.1'],
    },
    classifiers=[
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: 3.14',
    ],
)
