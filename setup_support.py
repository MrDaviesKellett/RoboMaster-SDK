"""
Shared packaging helpers for the RoboMaster SDK distribution.
"""

import os
import platform
import re
import subprocess
import sys

from setuptools import Extension
from setuptools.command.build_ext import build_ext

try:
    import pybind11
except ImportError:
    pybind11 = None


PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))
MIN_PYTHON = (3, 14)


def ensure_supported_python():
    if sys.version_info < MIN_PYTHON:
        sys.exit("RoboMaster SDK requires Python 3.14 or later")


def ensure_pybind11():
    if pybind11 is None:
        sys.exit(
            "RoboMaster SDK requires pybind11 >= 3.0.3 to build libmedia_codec. "
            "Install it with 'python -m pip install pybind11>=3.0.3'."
        )


def fetch_version():
    with open(os.path.join(PROJECT_ROOT, "src", "robomaster", "version.py")) as file_obj:
        namespace = {}
        exec(file_obj.read(), namespace)
        return namespace["__version__"]


class CMakeExtension(Extension):
    def __init__(self, name, sourcedir=""):
        super().__init__(name, sources=[])
        self.sourcedir = os.path.abspath(sourcedir)


class CMakeBuild(build_ext):
    def run(self):
        try:
            out = subprocess.check_output(["cmake", "--version"])
        except OSError as exc:
            raise RuntimeError(
                "CMake must be installed to build the following extensions: "
                + ", ".join(extension.name for extension in self.extensions)
            ) from exc

        if platform.system() == "Windows":
            version = re.search(r"version\s*([\d.]+)", out.decode())
            cmake_version = tuple(int(part) for part in version.group(1).split("."))
            if cmake_version < (3, 15, 0):
                raise RuntimeError("CMake >= 3.15.0 is required on Windows")

        for extension in self.extensions:
            self.build_extension(extension)

    def build_extension(self, extension):
        extdir = os.path.abspath(os.path.dirname(self.get_ext_fullpath(extension.name)))
        if not extdir.endswith(os.path.sep):
            extdir += os.path.sep

        cmake_args = [
            "-DCMAKE_LIBRARY_OUTPUT_DIRECTORY=" + extdir,
            "-DPYTHON_EXECUTABLE=" + sys.executable,
            "-Dpybind11_DIR=" + pybind11.get_cmake_dir(),
        ]

        cfg = "Debug" if self.debug else "Release"
        build_args = ["--config", cfg]

        if platform.system() == "Windows":
            cmake_args += [f"-DCMAKE_LIBRARY_OUTPUT_DIRECTORY_{cfg.upper()}={extdir}"]
            if sys.maxsize > 2 ** 32:
                cmake_args += ["-A", "x64"]
            build_args += ["--", "/m"]
        else:
            cmake_args += ["-DCMAKE_BUILD_TYPE=" + cfg]
            build_args += ["--", "-j2"]

        env = os.environ.copy()
        env["CXXFLAGS"] = '{} -DVERSION_INFO=\\"{}\\"'.format(
            env.get("CXXFLAGS", ""),
            self.distribution.get_version(),
        )
        build_temp = self.build_temp + "_" + extension.name
        if not os.path.exists(build_temp):
            os.makedirs(build_temp)
        subprocess.check_call(["cmake", extension.sourcedir] + cmake_args, cwd=build_temp, env=env)
        subprocess.check_call(["cmake", "--build", "."] + build_args, cwd=build_temp)


def media_data_files():
    if platform.system() != "Windows":
        return []
    return [
        ("lib/site-packages", ["lib/libmedia_codec/src/ffmpeg-dll/avcodec-58.dll"]),
        ("lib/site-packages", ["lib/libmedia_codec/src/ffmpeg-dll/avutil-56.dll"]),
        ("lib/site-packages", ["lib/libmedia_codec/src/ffmpeg-dll/swresample-3.dll"]),
        ("lib/site-packages", ["lib/libmedia_codec/src/ffmpeg-dll/swscale-5.dll"]),
        ("lib/site-packages", ["lib/libmedia_codec/src/opus-dll/opus.dll"]),
    ]


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
        "ext_modules": [CMakeExtension("libmedia_codec", "./lib/libmedia_codec/")],
        "cmdclass": {"build_ext": CMakeBuild},
        "zip_safe": False,
        "data_files": media_data_files(),
    }
