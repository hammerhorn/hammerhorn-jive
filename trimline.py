#!/usr/bin/env python
#coding='utf-8'
"""
Removes trailing whitespace.  * Add text-wrapping.
"""
import argparse
import pydoc
import sys
import traceback

from cjh.cli import Cli

__author__ = 'Chris Horn <hammerhorn@gmail.com>'
__license__ = 'GPL'


def _parse_args():
    """Parse arguments"""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('filename', type=str, help='file to process')
    if __name__ == '__main__':
        args = parser.parse_args()
    else:
        args = None
    return args


def main():
    """
    Reads in a specified file, removes trailing whitespace, and re-saves.
    """
    # Open file and store lines as str list
    try:
        file_handler = open(ARGS.filename, 'r+')
    except IOError:
        print(traceback.format_exc())  # pylint: disable=C0325
        sys.exit()

    lines_of_text = file_handler.readlines()
    file_handler.seek(0)

    # Preview and write text back to file and close file
    print(lines_of_text)  # pylint: disable=C0325
    Cli.wait()
    string = ''
    preview_string = ''
    for index, _ in enumerate(lines_of_text):
        string += lines_of_text[index].rstrip() + '\n'
        preview_string = string.strip() + Cli.term_fx('b', 'EOL')
    pydoc.pipepager(preview_string, cmd='less -R')
    try:
        char = Cli.get_keypress('Write to file?')
        assert char == 'y'
        file_handler.write(string)
    except AssertionError:
        print('File not saved.  Good bye.')  # pylint: disable=C0325
    finally:
        file_handler.close()

Cli()
ARGS = _parse_args()

if __name__ == '__main__':
    main()
