#!/usr/bin/python
"""
create bold text

Prompts user for a string, and then echos it back--in a bold font.
If using Tk, text will appear on a bold banner.

usage: bold.py [-h] [--nox]
"""
import argparse

from cjh.cli import Cli
from cjh.config import Config

__author__ = 'Chris Horn <hammerhorn@gmail.com>'
__license__ = 'GPL'


def _parse_args():
    """
    Parse arguments

    optional arguments:
      -h, --help  show this help message and exit
      --nox       text-based interface
    """
    parser = argparse.ArgumentParser(
        description=
        'Prompts user for a string, and then echos it back--in a bold font.')
    parser.add_argument(
        '--nox', action='store_true', help='text-based interface')
    if __name__ == '__main__':
        return parser.parse_args()
    else:
        return None


##########
#  DATA  #
##########

ARGS = _parse_args()
CONFIG = Config()
if ARGS is not None and ARGS.nox is True:
    SHELL = Cli()
else:
    SHELL = CONFIG.start_user_profile()

LANG = CONFIG.get_lang_key()
AVG_CHAR_WIDTH = 31


##########
#  MAIN  #
##########

def main():
    """
    Prompt user for a string, then echo it back in bold.
    """
    Cli()
    # Input
    txt = SHELL.input(
        {'EN': 'Something to bolden: ', 'EO': 'Teksto por grasigi: '}[LANG])

    # Output
    if SHELL.interface in ['sh', 'bash', 'dialog', 'SL4A', 'zenity']:
        Cli.term_fx('bp', txt)
    elif SHELL.interface in ['Tk']:
        total_width = len(txt) * AVG_CHAR_WIDTH + 45

        SHELL.center_window(height_=90, width_=total_width, y_offset=100)
        SHELL.main_window.config(bg='white')
        SHELL.msg.config(
            bg='white', width=total_width, font=('serif', 36, 'bold', 'italic'))
        SHELL.msgtxt.set(txt)
        SHELL.main_window.title(txt)
        SHELL.main_window.mainloop()

if __name__ == '__main__':
    main()
