#!/usr/bin/env python
"""
Inspired by the classic BASIC program by David Ahl.
"""

import math, sys, time

from cjh import cli

cli.Cli()
cli.Cli.clear()
print(' ' * 30 + 'SINE WAVE')
print(' ' * 15 + 'CREATIVE COMPUTING  MORRISTOWN, NEW JERSEY\n')
cli.Cli.wait()
print('\n' * 4)

toggle = 0
iter_count = 0
try:
    cli.write('\033[?25l')
    while True:
        s = iter_count / 4.0
        width = cli.Cli.width()
        indent = int((width - 10) * math.sin(s) + width - 8) // 2
        cli.write(' ' * indent)
        if(toggle == 1):
            print('CREATIVE')
            toggle = 0
        else:
            print('COMPUTING')
            toggle = 1
        time.sleep(.025)
        iter_count += 1
except KeyboardInterrupt:
    pass
finally:
    cli.write('\033[?25h')
