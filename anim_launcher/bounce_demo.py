#!/usr/bin/env python
"""
Animation #1

This is the format of animations which can be launched with
'anim_launcher' module.

*This should be modified to utilize cursor movement rather than clearing
the whole screen between frames.

* animate1() or something could be a method of Graph?
"""
import argparse
import os
import time

from cjh.cli import Cli
from cjh.igo import Goban

__author__ = 'Chris Horn <hammerhorn@gmail.com>'
__license__ = 'GPL'


def _parse_args():
    """
    Parse arguments
    (see above)
    """
    parser = argparse.ArgumentParser(description='A Simple Animation')
    parser.add_argument('-t', '--deltat', type=float, help='time interval')
    parser.add_argument(
        '-d', '--deltad', type=float, help='displacement interval')
    parser.add_argument('-z', '--size', type=int, help='board size')
    if __name__ == '__main__':
        args = parser.parse_args()
    else:
        args = None
    return args

# Set all Parameters
ARGS = _parse_args()
if ARGS is not None and ARGS.deltat is not None:
    T_INTERVAL = ARGS.deltat
else:
    T_INTERVAL = 0.1

if ARGS is not None and ARGS.deltad is not None:
    D_INTERVAL = ARGS.deltad
else:
    D_INTERVAL = 2

if ARGS is not None and ARGS.size is not None:
    SIZE_ = ARGS.size
else:
    SIZE_ = 19


def main():
    """
    This particular file shows a point oscillating left and right along
    the x-axis.
    """
    goban = Goban(size=SIZE_, sh_obj=Cli(), adjust_ssize=-8)
    current_frame_no = 0

    while True:
        for i in range(-(goban.max_domain), goban.max_domain + 1,
            int(round(D_INTERVAL))):
            goban.fill('empty')
            goban.plot_point(i, 0, 'white')
            current_frame_no += 1
            Cli.print_header('+f{}'.format(current_frame_no))
            print((str(goban).rstrip()))  # pylint: disable=C0325
            time.sleep(T_INTERVAL)

        for i in range(-(goban.max_domain - 1), (goban.max_domain),
            int(round(D_INTERVAL))):
            goban.fill('empty')
            goban.plot_point(-i, 0, 'black')
            current_frame_no += 1
            Cli.print_header('+f{}'.format(current_frame_no))
            print((str(goban).rstrip()))  # pylint: disable=C0325
            time.sleep(T_INTERVAL)

if __name__ == '__main__':
    os.system('tput civis')
    try:
        main()
    finally:
        os.system('tput cnorm')
