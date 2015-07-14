#!/usr/bin/env python
"""
Inspired by the classic BASIC program by David Ahl.
"""

import math, sys, time

from cjh import cli

cli.Cli()
cli.Cli.clear()

# Print title
print(' ' * 30 + 'SINE WAVE')
print(' ' * 15 + 'CREATIVE COMPUTING  MORRISTOWN, NEW JERSEY\n')
cli.Cli.wait()
print('\n' * 4)

toggle = False
iter_count = 0
try:
    cli.write('\033[?25l')
    while True:
        s = iter_count / 4.0
        width = cli.Cli.width()
        indent = int((width - 10) * math.sin(s) + width - 8) // 2
        cli.write(' ' * indent)
        if(toggle == True):
            print('CREATIVE')
            toggle = False
        else:
            print('COMPUTING')
            toggle = True
        time.sleep(.025)
        iter_count += 1
except KeyboardInterrupt:
    pass
finally:
    cli.write('\033[?25h')
