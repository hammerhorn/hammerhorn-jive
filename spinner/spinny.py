#!/usr/bin/env python
import os, time

import cjh.cli as cli

__author__ = 'Chris Horn <hammerhorn@gmail.com>'

if __name__ == '__main__':
    cli.write('\033[?25l')
    try:
        while True:
            cli.write('/')
            time.sleep(.075)
            cli.write('\b|')
            time.sleep(.075)
            cli.write('\b\\')
            time.sleep(.075)
            cli.write('\b-')
            time.sleep(.075)
            cli.write('\b')
    finally:
        cli.write('\033[?25h')
