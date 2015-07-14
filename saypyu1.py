#!/usr/bin/env python
#coding=utf-8
"""
Uses a JSON dictionary to replace words with other words.  Useful for
converting between writing systems or doing word-for-word translations.
"""
__author__ = 'Chris Horn <hammerhorn@gmail.com>'

import json

from cjh.cli import Cli


def read_json_file(filename):
    """
    Find the config.json file and load the specified shell.
    """
    file_handler = open(filename, 'rb')
    string = file_handler.read().decode('utf-8')
    translate_key = json.loads(string)
    return translate_key

TRANSLATE_KEY = read_json_file('en_saypyu.json')

Cli()


def main():
    """
    Get stdin, echo translation to stdout.
    """
    Cli.clear()
    while True:
        words = [word.strip('.').strip().lower()
            for word in Cli.input().split()
        ]
        if words == [':get-list']:
            list_ = [w.encode('ascii') for w in list(TRANSLATE_KEY.keys())]
            print('\n{}'.format(
                sorted(list_, key=str.lower)))  # pylint: disable=C0325
            continue
        output = ''

        for word in words:
            output += (TRANSLATE_KEY[word] + ' ')

        print('{}.\n'.format(
            output.encode(
            'utf-8').capitalize().strip()))  # pylint: disable=C0325

if __name__ == '__main__':
    main()
