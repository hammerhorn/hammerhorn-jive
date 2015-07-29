#!/usr/bin/env python
"""
Draw tonerow

Generate an ASCII diagram of a 12-tone tonerow (musical serialism).
    use: tonerow.py | draw_row.py [-h] [-s SHELL]
"""
__author__ = 'Chris Horn <hammerhorn@gmail.com>'

import argparse

from cjh.cli import Cli
from cjh.config import Config


################
#  PROCEDURES  #
################
def _parse_args():
    """
    Parse arguments: -h (help), -s (bash, Tk, etc.)
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('-s', '--shell', type=str)
    return parser.parse_args()


##########
#  DATA  #
##########
if __name__ == '__main__':
    ARGS = _parse_args()
else:
    ARGS = None
CONFIG = Config()
if ARGS is not None and ARGS.shell is not None:
    SHELL = CONFIG.launch_selected_shell(ARGS.shell)
else:
    SHELL = CONFIG.start_user_profile()


## Set up Tk window ##
if SHELL.interface in ['Tk']:
    SHELL.center_window(width_=400, height_=300)
    SHELL.msg.config(font=('mono', 9, 'bold'))

#if SHELL.interface in ['dialog']:
#    w, h = 46, 24


##########
#  MAIN  #
##########
def main():
    """
    Takes  a space-delimited int list (e.g., '1 2 3 4 5 6 7 8 9 10 11
    12') as input; generates and ouputs an ASCII diagram.

    * It might be good to define more functions.
    """
#    SHELL.welcome('Draw Tonerow', 'draw a diagram of a 12-tone row')
    in_str = Cli().input(prompt='')
    str_list = in_str.split()
    int_list = [int(s) for s in str_list]
    out_str = '\n'
    out_str += '\n ' + str(int_list)
    out_str += '\n' + '=' * 41 + '\n'
    out_str += '\n'

    for row in range(12):
        str_row = ' {:>2} '.format(12 - row)

        for index in range(12):
            if int_list[index] == 12 - row:
                str_row += '[X]'
            else:
                str_row += '. .'

        out_str += str_row + '\n'

    out_str += '\n'
    SHELL.output(out_str)

if __name__ == '__main__':
    main()
