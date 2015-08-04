#!/usr/bin/python
#coding=UTF-8
"""
Find the sum of two 2D vectors. (reads from command line and stdin)

VectorSum.py [mag1] [ang1] [mag2] [ang2]
(* The result is not correct.)
"""

__author__ = 'Chris Horn <hammerhorn@gmail.com>'

import argparse, decimal, sys

from cjh.angles import Angle
import cjh.cli as cli
from cjh.config import Config
from cjh.kinematics import Vector

def _parse_args():
    """
    Parse arguments
    """
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--nox', action='store_true')
    if __name__ == '__main__':
        args = parser.parse_args()
    else: args = None
    return args

ARGS = _parse_args()
sys.argv = [arg for arg in sys.argv if not arg.startswith('-')]
CONFIG = Config()
if ARGS is not None and ARGS.nox is True:
    SHELL = cli.Cli()
else:
    SHELL = CONFIG.start_user_profile()
    if SHELL.interface in ['wx', 'Tk']:
        SHELL.center_window()
PROMPTS = ['magnitude(1)', 'θ(1) (°)', 'magnitude(2)', 'θ(2) (°)']

def main():
    """
    Gets two pairs of magnitude and angle from command line or interactive
    prompt and perform vector addition.
    """
    # If no args, greet first-time user
    if len(sys.argv[1:]) == 0:
        SHELL.welcome(description="""
Find the sum of two 2D vectors (reads from command line and
standard input)

VectorSum.py [mag1] [ang1] [mag2] [ang2]
        """)
    loop_flag = True
    while loop_flag:
        if SHELL.interface == 'Tk':
            loop_flag = False
        print('') #pylint: disable=C0325
        mag1 = decimal.Decimal(SHELL.arg(*PROMPTS))

        cli.write(' ' * 2)#temporary fix
        theta1 = decimal.Decimal(SHELL.arg(*PROMPTS))
        print('') #pylint: disable=C0325
        mag2 = decimal.Decimal(SHELL.arg(*PROMPTS))

        cli.write(' ' * 2)#temporary fix
        theta2 = decimal.Decimal(SHELL.arg(*PROMPTS))
        print('') #pylint: disable=C0325

        angle1 = Angle(theta1, 'deg')
        angle2 = Angle(theta2, 'deg')

        vector1 = Vector(mag1, angle1)
        vector2 = Vector(mag2, angle2)
        vector_sum = vector1 + vector2
        SHELL.output(str(vector_sum))
        SHELL.main_window.mainloop()

if __name__ == '__main__':
    main()
