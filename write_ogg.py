#!/usr/bin/env python
"""
Produces an OGG file from a list of frequencies.

Dependencies: sox

(* This should be done with fewer system calls.  It should be possible to
acheive the same effect with one or two lines.  SHELL.yesorno() and
SHELL.fatal_error() should be created.)
"""
import os
import subprocess
import sys

from cjh.config import Config

__author__ = 'Chris Horn <hammerhorn@gmail.com>'

# GLOBALS
CONFIG = Config()
SHELL = CONFIG.start_user_profile()

# If '-c', the output will be a chord; otherwise it will be a melody.
if '-c' in sys.argv:
    CHORD_FLAG = True
    del sys.argv[sys.argv.index('-c')]
else:
    CHORD_FLAG = False


def main():
    """
    Takes a list of frequencies in Hz as args, writes each tone to a WAV
    file, mixes them down to an OGG file, and then deletes the WAV files.
    """
    # If '-h', print a help message and exit.
    if '-h' in sys.argv or '--help' in sys.argv:
        SHELL.output(__doc__)
        sys.exit(0)

    # Writes a WAV file for each frequency in args.
    try:
        for count in range(len(sys.argv[1:])):
            command = 'sox -n {}.wav synth .3 squ {} vol 1 2> /dev/null'.format(
                count, sys.argv[count + 1])
            proc = subprocess.Popen(command, shell=True)
            proc.wait()
            #SHELL.notify('Wrote {}.wav'.format(count))
    except (OSError, subprocess.CalledProcessError):
        sys.exit('Writing of WAV files failed.  Exiting.')

    # Mixes or concatenates the tones to a OGG file, 'out.ogg'.
    command = 'sox '
    if CHORD_FLAG is True:
        command += '-m '
    for count in range(len(sys.argv[1:])):
        command += '{}.wav '.format(count)
    command += ' out.ogg 2> /dev/null'

    try:
        proc = subprocess.Popen(command, shell=True)
        proc.wait()
        SHELL.report_filesave('out.ogg')
    except (OSError, subprocess.CalledProcessError):
        if os.path.exists('out.ogg'):
            os.remove('out.ogg')
        # remove glob wav
        sys.exit("Attempt to create 'out.ogg' failed.")
    finally:
        # Clean up the WAV files we created.
        #SHELL.notify('Cleaning up WAV files')
        for count in range(len(sys.argv[1:])):
            if os.path.exists('{}.wav'.format(count)):
                os.remove('{}.wav'.format(count))

if __name__ == '__main__':
        main()
