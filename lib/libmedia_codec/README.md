# libmedia_codec

`libmedia_codec` is the optional native extension used by RoboMaster video and audio streaming.

## Python support

This fork targets **CPython 3.14+**.

## Build requirements

- CMake 3.15+
- `pybind11` 3.0.3+
- C++11 compiler
- FFmpeg and Opus development libraries on Linux/macOS
- Visual C++ build tools on Windows

## Build from source

From the repository root:

```bash
python setup_with_lib.py build_ext --inplace
```

Or build the extension package directly:

```bash
cd lib/libmedia_codec
python -m pip install .
```

The build now uses the external `pybind11` package from PyPI instead of the vendored legacy copy that shipped with the original DJI repository.
