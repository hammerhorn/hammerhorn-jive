#!/usr/bin/env python
"""
Allow the user to preview the available fonts for toilet (or figlet).
"""
import argparse
import os
import subprocess
import sys

from cjh.cli import Cli
from cjh.config import Config
from cjh.lists import PlainList

__author__ = 'Chris Horn <hammerhorn@gmail.com>'
__license__ = 'GPL'


##  PROCEDURES  ##
def _parse_args():
    """
    Parse arguments
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('--nox', action='store_true')
    if __name__ == '__main__':
        args = parser.parse_args()
    else:
        args = None
    return args

#def menu_func():
#    return SHELL.list_menu(LIST_OBJ)

##  MAIN  ##

# Prepare environment
ARGS = _parse_args()
CONFIG = Config()
if ARGS is not None and ARGS.nox is True:
    sys.argv = [i for i in sys.argv if not i.startswith('-')]
    SHELL = Cli()
else:
    Cli()
    SHELL = CONFIG.start_user_profile()
    if SHELL.interface in ['Tk', 'wx']:
        SHELL.center_window()

FONT_OPTIONS = os.listdir('/usr/share/figlet')
FONT_OPTIONS = [line for line in FONT_OPTIONS if not line.endswith('.flc')]
FONT_OPTIONS.sort()
LIST_OBJ = PlainList(FONT_OPTIONS)

if len(sys.argv[1:]) == 0:
    PHRASE = 'Hello'
else:
    PHRASE = sys.argv[1]


def main():
    """
    Gets the user's choice and gives them a preview.
    """
    _first_pass = True
    art = ''
    if __name__ == '__main__':
        while True:
            if SHELL.interface in ['dialog'] and not _first_pass:
                Cli.wait()
            else:
                _first_pass = False
            #selection = Cli.make_page(obj='\n' + art, func=menu_func)
            selection = Cli.make_page(
                obj='\n' + art, func=lambda: SHELL.list_menu(LIST_OBJ))
            if selection == -1:
                break
            figlet_font = FONT_OPTIONS[selection - 1]
            art = subprocess.check_output('toilet --gay -f {} "{}"'.format(
                figlet_font, PHRASE), shell=True)

main()
