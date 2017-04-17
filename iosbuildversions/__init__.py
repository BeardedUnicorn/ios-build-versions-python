from __future__ import absolute_import

from iosbuildversions.builds import build_list as _builds


def get_builds():
    return _builds


def lookup_by_build(build):
    try:
        return _builds[build]
    except KeyError:
        return False
