#!/usr/bin/env python

import sys

try:
    if ':' in sys.argv[1]:
        mmss = tuple(sys.argv[1].split(':'))
        try:
            mins = int(mmss[0])
        except ValueError:
            mins = 0
        try:
            secs = float(mmss[1])
        except ValueError:
            secs = 0
        total_seconds = mins * 60 + secs
        print(total_seconds)

    else:
        total_seconds = float(sys.argv[1])
        mins = int(total_seconds) // 60
        secs = total_seconds % 60
        print('{:d}:{:02g}'.format(mins, secs))

except IndexError:
    print('Argument required.')
