import unittest
import pytest
from iosbuildversions import lookup_by_build, _builds


class TestBuilds(unittest.TestCase):
    def test_lookup_by_build(self):
        assert lookup_by_build("") is False

        build = lookup_by_build("11D5127c")
        assert isinstance(build, dict)
        assert build["build"] == "11D5127c"
        assert build["beta"] is True
        assert build["final"] is False
        assert build["name"] == "iOS 7.1 beta 3"

        build = lookup_by_build("10A403")
        assert isinstance(build, dict)
        assert build["build"] == "10A403"
        assert build["beta"] is False
        assert build["final"] is True
        assert build["name"] == "iOS 6.0 Final"

    def test_builds_formed_correctly(self):
        for build in _builds:
            assert isinstance(_builds[build]["name"], str)
            assert isinstance(_builds[build]["final"], bool)
            assert isinstance(_builds[build]["beta"], bool)
            assert isinstance(_builds[build]["build"], str)
