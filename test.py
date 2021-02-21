import argparse
import sys


def hit_implementation():
    if sys.implementation == "cpython":
        print("hit", sys.implementation.name)
    elif sys.implementation == "pypy":
        print("hit", sys.implementation.name)


def hit_platform():
    if sys.platform == "linux":
        print("hit", sys.platform)
    elif sys.platform == "darwin":
        print("hit", sys.platform)
    elif sys.platform == "win32":
        print("hit", sys.platform)


def hit_version():
    if sys.version_info[:2] == (2, 7):
        print("hit", sys.implementation.name, sys.version_info)

    if sys.version_info[:2] == (3, 5):
        print("hit", sys.implementation.name, sys.version_info)

    if sys.version_info[:2] == (3, 6):
        print("hit", sys.implementation.name, sys.version_info)

    if sys.version_info[:2] == (3, 7):
        print("hit", sys.implementation.name, sys.version_info)

    if sys.version_info[:2] == (3, 8):
        print("hit", sys.implementation.name, sys.version_info)

    if sys.version_info[:2] == (3, 9):
        print("hit", sys.implementation.name, sys.version_info)


def main(raw_args):
    parser = argparse.ArgumentParser()
    parser.add_argument("--cover-it", action="store_true")

    args = parser.parse_args(raw_args)

    if args.cover_it:
        print("covering one more line")
    else:
        hit_implementation()
        hit_platform()
        hit_version()


sys.exit(main(raw_args=sys.argv[1:]))
