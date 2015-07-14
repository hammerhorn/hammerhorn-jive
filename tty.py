#!/usr/bin/env python
"""A test of the Cli.tty method.  Writes text to the screen one char at a time,
like a teletype.

*alter Cli.tty() so that it automatically wraps text."""

import datetime
import textwrap

import cjh.cli as cli
from cjh.text_fill import TextGen

__author__ = 'Chris Horn <hammerhorn@gmail.com>'
__license__ = 'GPL'

STRING = textwrap.fill(
        TextGen.chunk(),
        width=60,
        initial_indent=' ' * 5,
        subsequent_indent=' ' * 5)


def main():
    """
    Prints date and then a chunk of filler text.  Text "streams" onto
    the screen.
    """
    print('\n')  # pylint: disable=C0325
    today = datetime.datetime.today()
    now = today.strftime('%c')  # Make syre this is a portable date format.
    cli.tty(' ' * 35 + now)
    print('\n' * 2)  # pylint: disable=C0325
    cli.tty(STRING)
    print('\n' * 3)  # pylint: disable=C0325

if __name__ == '__main__':
    main()
