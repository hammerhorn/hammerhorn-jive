#!/usr/bin/env python
"""
Convert text containing newlines to a space-delimited list; for use in
shell scripts.

(* 'chomp' function should be moved to class Cli.)
"""
__author__ = 'Chris Horn <hammerhorn@gmail.com>'

import argparse
import sys


__author__ = 'Chris Horn <hammerhorn@gmail.com>'
__license__ = 'GPL'


def main():
    """
    Read from stdin, convert newlines to spaces, strip the trailing
    space, and write to stdout.
    """
    # if help flag found, print help and exit
    parser = argparse.ArgumentParser(description=__doc__)
    parser.parse_args()

    text = sys.stdin.read()
    text = text.replace('\n', ' ')
    text = text.strip()
    sys.stdout.write(text)
    sys.stdout.flush()

if __name__ == '__main__':
    main()
