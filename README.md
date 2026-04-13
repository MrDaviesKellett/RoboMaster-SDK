# RoboMaster-SDK

[![Gitter](https://badges.gitter.im/RoboMaster-SDK/community.svg)](https://gitter.im/RoboMaster-SDK/community?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge)

<img src="docs/source/images/robomaster.jpg" width="600">

Learn more about the RoboMaster Education Robot: https://www.dji.com/robomaster-ep

RoboMaster Developer Guide: https://robomaster-dev.rtfd.io/

Gitee link for RoboMaster SDK download: https://gitee.com/xitinglin/RoboMaster-SDK

## Python support

This fork targets **CPython 3.14 and newer**.

PyPI distribution name: **`robomaster-sdk-modern`**.

The original DJI repository was built around Python 3.6-3.8 era tooling. This fork updates the package metadata, runtime compatibility, and media-extension build path for modern interpreters.

## Source installation

Install from PyPI:

```bash
python -m pip install robomaster-sdk-modern
```

Install from a local checkout:

```bash
python -m pip install .
```

Install the optional QR-code helper used by `examples/01_robot/05_sta_conn_helper.py`:

```bash
python -m pip install MyQR
```

## Media streaming support

Video and audio streaming use the `libmedia_codec` extension module.

- `setup.py` installs the pure-Python package dependencies.
- `setup_with_lib.py` builds the SDK together with `libmedia_codec`.
- `lib/libmedia_codec` now expects a modern external `pybind11` installation instead of the vendored legacy snapshot.

Build prerequisites for source installs with media support:

- CMake 3.15+
- `pybind11` 3.0.3+
- FFmpeg and Opus development libraries on Linux/macOS
- Visual C++ build tools on Windows

## Compatibility changes in this fork

- Replaced `audioop` usage with a NumPy-based PCM resampler because `audioop` was removed in Python 3.13.
- Replaced `netifaces` and `netaddr` subnet discovery with `psutil` plus the standard library.
- Updated package minimums to versions that publish Python 3.14-compatible wheels.

## Release workflow

`pyproject.toml` is now the canonical build metadata for the forked distribution.

Build and upload with:

```bash
python -m pip install .[release]
python -m build
python -m twine upload dist/*
```
