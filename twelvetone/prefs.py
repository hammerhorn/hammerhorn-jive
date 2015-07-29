#!/usr/bin/env python
"""
Reads from and write to the config file, 'config.json'.
"""
import argparse

from cjh.cli import Cli
from cjh.config import Config

__author__ = 'Chris Horn <hammerhorn@gmail.com>'


def _parse_args():
    """
    Parse command-line arguments
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('-s', type=str, help='set shell')
    parser.add_argument('-e', type=str, help='set editor')
    parser.add_argument('-t', type=str, help='set terminal')
    parser.add_argument('-l', type=str, help='set language')
    parser.add_argument('-v', action='count')
    args = parser.parse_args()
    return args

if __name__ == '__main__':
    ARGS = _parse_args()
else:
    ARGS = None

CONFIG = Config()
FILENAME = 'cjh/config.json'

#make more efficient
if 'shell' in list(CONFIG.config_dict.keys()):
    shell = CONFIG.config_dict['shell']
else:
    shell = None

if 'editor' in list(CONFIG.config_dict.keys()):
    editor = CONFIG.config_dict['editor']
else:
    editor = None

if 'terminal' in list(CONFIG.config_dict.keys()):
    terminal = CONFIG.config_dict['terminal']
else:
    terminal = None

if 'language' in list(CONFIG.config_dict.keys()):
    language = CONFIG.config_dict['language']
else:
    language = None


def main():
    """
    Writes requested modifications to the 'config.json' file, and sends
    some kind of feedback to stdout.
    """
    if ARGS.s is not None:
        CONFIG.write_to_config_file(shell=ARGS.s)
    if ARGS.e is not None:
        CONFIG.write_to_config_file(editor=ARGS.e)
    if ARGS.t is not None:
        CONFIG.write_to_config_file(terminal=ARGS.t)
    if ARGS.l is not None:
        CONFIG.write_to_config_file(language=ARGS.l)

#    config_dict = {'shell':shell}
#    with open(filename, 'w') as outfile: json.dump(
#        config_dict, outfile, indent=2)

    string = ''

    if (ARGS.v >= 1 and ARGS.s is not None) or not (
        ARGS.e or ARGS.s or ARGS.t or ARGS.l):
        string += "\n   shell: '{}'".format(shell)
    if (ARGS.v >= 1 and ARGS.e is not None) or not (
        ARGS.e or ARGS.s or ARGS.t or ARGS.l):
        string += "\n  editor: '{}'".format(editor)
    if (ARGS.v >= 1 and ARGS.t is not None) or not (
        ARGS.e or ARGS.s or ARGS.t or ARGS.l):
        string += "\nterminal: '{}'".format(terminal)
    if (ARGS.v >= 1 and ARGS.l is not None) or not (
        ARGS.e or ARGS.s or ARGS.t or ARGS.l):
        string += "\nlanguage: '{}'".format(language)
    if len(string) > 0:
        print(string + '\n')  # pylint: disable=C0325

    if (ARGS.v >= 2) or (
        not (ARGS.e or ARGS.s or ARGS.t or ARGS.l) and ARGS.v >= 1):
        Cli.view_source(FILENAME)
    if ARGS.s or ARGS.e or ARGS.t or ARGS.l:
        Cli.report_filesave(FILENAME)

if __name__ == '__main__':
    main()
