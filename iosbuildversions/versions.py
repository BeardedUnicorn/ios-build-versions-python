import yaml

_builds = yaml.load(open("builds.yml"))


def get_builds():
    return _builds


def lookup_by_build(build):
    try:
        return _builds[build]
    except KeyError:
        return False

