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

This is now the canonical install path. Media streaming support is provided through the PyPI dependency `av`, which already ships cross-platform FFmpeg-backed wheels.

Install from a local checkout:

```bash
python -m pip install .
```

Install the optional QR-code helper used by `examples/01_robot/05_sta_conn_helper.py`:

```bash
python -m pip install MyQR
```

## Media streaming support

Video and audio streaming now use the `av` Python package by default.

- `av` publishes CPython 3.14 wheels for Linux, macOS, and Windows with FFmpeg bundled.
- `libmedia_codec` remains supported as a legacy fallback backend for advanced/source users, but it is no longer required for normal package installs.
- The default PyPI package no longer needs a custom native wheel pipeline just to enable camera/audio features.

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
