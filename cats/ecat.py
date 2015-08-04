#!/usr/bin/env python
"""
Acts like 'cat' if input is from stdin, acts like 'echo' when input is
from command-line args.
"""
__author__ = 'Chris Horn <hammerhorn@gmail.com>'

import sys

from cjh.cli import Cli


def main():
    """
    Get input from either command line args or from stdin, and echo it
    back to stdout.
    """
    text = ""
    Cli()
    if len(sys.argv[1:]) > 0:
        for arg in sys.argv[1:]:
            text = text + arg + ' '
        print((text.rstrip()))  # pylint: disable=C0325
    else:
        try:
            while True:
                print((Cli.input()))  # pylint: disable=C0325
        except EOFError:
            pass

if __name__ == '__main__':
    main()
