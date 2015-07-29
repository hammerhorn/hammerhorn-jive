#!/usr/bin/env python
# coding=UTF-8

import sys

from cjh.config import Config

CONFIG = Config()
SHELL = CONFIG.start_user_profile()


def main():
    try:
        SIDES = int(sys.argv[1])
        if(SIDES >= 3):
            string = 'In a figure with {} sides,\n'.format(SIDES)
            string += '\n\tsum of all angles = {}°\n'.format((SIDES - 2) * 180)
            string += '\t    average angle = {}°'.format(
                (SIDES - 2) * 180.0 / SIDES)
            SHELL.output(string)
            if SHELL.interface == 'Tk':
                SHELL.center_window(width_=300, height_=100)
                SHELL.msg.config(width=300)
                SHELL.main_window.mainloop()
        else:
            SHELL.message('You need at least 3 sides to form a polygon.')
    except IndexError:
        SHELL.message('\n\t Use: each_angle.py $NUMBER_OF_SIDES\n')

if __name__ == '__main__':
    main()
