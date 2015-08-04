#!/usr/bin/env python
#coding=utf8
"""
Outputs pi, pi times a number, or pi over a number.

use: pi.py [-o] dividend
         or
     pi.py multiplicend

options: --nox
"""
__author__ = 'Chris Horn <hammerhorn@gmail.com>'
import decimal, sys

from cjh.config import Config
from cjh.cli import Cli

CONFIG = Config()

if '--nox' in sys.argv:
    SHELL = Cli()
    del sys.argv[sys.argv.index('--nox')]
else:
    SHELL = CONFIG.start_user_profile()

#if {'-h', '--help'} & set(sys.argv):
#    SHELL.output(__doc__)
#    sys.exit(0)

LONG_PI = decimal.Decimal('3.14159265358979323846')

title_str = 'pi '

if SHELL.interface == 'Tk':
#    SHELL.msg.config(width=200, bg='white', font=('times',12))
    SHELL.msg.config(bg='white', font=('courier',12, 'bold'))
#    SHELL.center_window(height_=50)
    SHELL.main_window.config(bg='white')


if __name__ == '__main__':
    #if len(sys.argv[1:]) == 0:
    #    #SHELL.output(LONG_PI)
    #    ans = LONG_PI
    #    title_str += '= '
    if len(sys.argv[1:]) == 1:

        if sys.argv[1] in ['-h', '--help']:
            Cli.output(__doc__)
            #SHELL.main_window.mainloop()
            sys.exit(0)

        multiplicend = decimal.Decimal(sys.argv[1])
        ans = LONG_PI * multiplicend
        title_str += '* {} ='.format(multiplicend)


    elif len(sys.argv[1:]) == 2 and {'-o', '--over'} & set(sys.argv[1:]):
        dividend = decimal.Decimal(sys.argv[2])
        ans = LONG_PI / dividend
        title_str += '/ {} ='.format(dividend)

    else:
        ans = LONG_PI
        title_str += '= '
    #if ans: 
    print(ans)

    if SHELL.interface == 'Tk':
        ans_str = str(ans) + '…'
        SHELL.output(ans_str)
        msg_width = len(ans_str) * 10
        width = msg_width + 40
        SHELL.msg.config(width=msg_width)
        SHELL.center_window(width_=width, height_=50)
        SHELL.main_window.title(title_str)
        SHELL.main_window.mainloop()
