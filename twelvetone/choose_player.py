#!/usr/bin/env python
"""
A wrapper for 'write_ogg.py'.

Looks in /usr/bin for either ogg123 or mplayer and runs
write_ogg.py with the selected player.

(* Maybe this could be adapted to play on some library on Android.
Ultimately, this script should be incorporated into an integrated
twelvetone app.)
"""
__author__ = 'Chris Horn <hammerhorn@gmail.com>'

import os
import subprocess
import sys


def main():
    """
    See if mplayer or ogg123 is installed, read from 'tmp' and call
    write_ogg.py.
    """

    if {'-h', '--help'} & set(sys.argv):
        print(__doc__)  # pylint: disable=C0325
        sys.exit(0)

    # Run write-ogg and play the result with 'ogg123' if available.
    if os.path.exists('/usr/bin/ogg123'):
	# This is a problem:
        proc = subprocess.Popen(
            './write_ogg.py $(./listfreqs.jar < tmp 2> /dev/null) &&\
	    ogg123 out.ogg > /dev/null 2>&1', shell=True)
        proc.wait()
    # Otherwise, run write-ogg and play the result using 'mplayer'.
    elif os.path.exists('/usr/bin/mplayer'):
        proc = subprocess.Popen('./write_ogg.py $(cat tmp | ./listfreqs.jar) &&\
            mplayer out.ogg -af channels=2:2:0:1:0:0 > /dev/null 2>&1',
            shell=True)
        proc.wait()

    else:
        sys.exit("Sorry.  You need either 'ogg123' or 'mplayer' in order to\
        play audio.")

if __name__ == '__main__':
    main()
