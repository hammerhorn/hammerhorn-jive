#!/usr/bin/env python
import time

import cjh.cli as cli

__author__ = 'Chris Horn'
__license__ = 'GPL'

def spin():
    try:
        while True:
            cli.write('/')
            time.sleep(.25)
            cli.write('\b|')
            time.sleep(.25)
            cli.write('\b\\')
            time.sleep(.25)
            cli.write('\b-')
            time.sleep(.25)
            cli.write('\b')
    except KeyboardInterrupt: return
