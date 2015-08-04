#!/usr/bin/env python
"""
Alternate interface for 'Enum.jar'
depends: Enum.jar
"""
import argparse
import subprocess
import sys

__author__ = 'Chris Horn <hammerhorn@gmail.com>'
__license__ = 'GPL'


def _parse_args():
    """
    Parse Args
    """
    parser = argparse.ArgumentParser(description=
        "A wrapper for using 'Enum.jar'")
    return parser.parse_args()

if __name__ == '__main__':
    _parse_args()


def main():
    """
    Gets items from command line or cat-style input; display using
    Enum.jar.
    """
    command = 'echo "'
    if len(sys.argv[1:]) > 0:
        for arg in sys.argv[1:]:
            command += arg + '\n'
    else:
        for line in sys.stdin:
            command += line[:len(line) - 1] + '\n'
    command += '"'
    proc = subprocess.Popen(command + '|./Enum.jar', shell=True)
    proc.wait()

if __name__ == '__main__':
    main()
