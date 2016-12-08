#!/usr/bin/env python
#coding=utf8
"""
VECTOR SUM - Find the sum of two 2D vectors. (currently reads from stdin only)
"""
#
#vector_sum.py [mag1] [ang1] [mag2] [ang2]
#(* The result is not correct.)
#"""

#import argparse
import decimal
import sys

from cjh import cli
from cjh import notebook as ntbk
from cjh.angles import Angle
from cjh.config import Config
from cjh.kinematics import Vector
#from cjh.scalars import Unit

__author__ = 'Chris Horn <hammerhorn@gmail.com>'
__license__ = 'GPL'

def _parse_args():
    """
    Parse arguments
    """
#    parser = argparse.ArgumentParser(description=__doc__)
#    parser.add_argument('-C', action='store_true')
#    parser.add_argument('--nox', action='store_true')

    if {'-h', '--help'} & set(sys.argv):
        cli.Cli.output(
            'usage: {}'.format(sys.argv[0]) +\
            ' [-h] [-C] [--nox] [mag1] [th1] [mag2] [th2]')
        cli.Cli.output(__doc__)
        sys.exit(0)
    elif '-C' in sys.argv:
        #if NTBK is True:
        ntbk.notebook("""    - embellish help screen
    - Could be re-written with argparse, but SHELL.arg() has its own advantages
    - radians""")
#        NTBK = True
    elif '--nox' in sys.argv:
        return True
#    parser.add_argument("NUMBERS", help="numbers to be processed", nargs="*")

#    parser.add_argument(
#            'integers', metavar='int', nargs='*', type=int,
#            help='an integer to be summed')

#    if __name__ == '__main__':
#        args = parser.parse_args()
#    else: args = None
#   args = None
#    return args



#ARGS = _parse_args()
#NTBK = False
NOX = False
NOX = _parse_args()
sys.argv = [arg for arg in sys.argv if not arg.startswith('-')]
#print(sys.argv)
#sys.exit()

CONFIG = Config()
#try:

#except:
#   print()
#sys.exit()

#if ARGS is not None and ARGS.nox is True:
if NOX is True:
    SHELL = cli.Cli()
else:
    SHELL = CONFIG.start_user_profile()
    if SHELL.interface in ['wx', 'Tk']:
        SHELL.center_window()

#if ARGS.C is True:
#if NTBK is True:
#    ntbk.notebook('    - embellish help screen\n    - Could be re-written with
# argparse, but SHELL.arg() has its own advantages')

PROMPTS = ['magnitude(1): ', 'θ(1) (°): ', 'magnitude(2): ', 'θ(2) (°): ']

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
    #else:
    #    loop_flag = False
    while loop_flag is True:
        if SHELL.interface == 'Tk' or len(sys.argv[1:]) != 0:
            loop_flag = False
        if loop_flag is True:
            cli.Cli.output('')
        mag1 = decimal.Decimal(SHELL.arg(*PROMPTS))

        cli.write(' ' * 2)#temporary fix
        theta1 = decimal.Decimal(SHELL.arg(*PROMPTS))
        if loop_flag is True:
            cli.Cli.output('')
        mag2 = decimal.Decimal(SHELL.arg(*PROMPTS))

        cli.write(' ' * 2)#temporary fix
        theta2 = decimal.Decimal(SHELL.arg(*PROMPTS))
        cli.Cli.output('')

        angle1 = Angle(theta1, 'deg')
        vector1 = Vector(mag1, angle1)

        angle2 = Angle(theta2, 'deg')
        vector2 = Vector(mag2, angle2)

        vector_sum = vector1 + vector2
        vector_sum.theta = vector_sum.theta.deg()

        SHELL.output('{}\n'.format(vector_sum))
        if SHELL.interface not in ['bash', 'sh']:
            SHELL.main_window.mainloop()

if __name__ == '__main__':
    main()
