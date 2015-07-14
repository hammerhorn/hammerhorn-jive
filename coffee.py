#!/usr/bin/env python
#coding=UTF-8
"""
Takes an argument in the form of ss or mm:ss, uses mmss.jar to convert
it and uses the time module to maintain accuracy.  Default time span is
5 minutes 30 minutes.

  use: coffee.py [-h] [-q] TIME_STR

where TIME_STR is of the form SS, :SS, MM:, or MM:SS.

* I think there are portable libraries for voice synth?  This script
should be modified to not depend on mmss.jar and to convert bytes to
string if running under python3.
"""
__author__ = 'Chris Horn <hammerhorn@gmail.com'

import argparse, datetime, os, subprocess, sys, time, traceback

import cjh.cli as cli

################
#  PROCEDURES  #
################
def _parse_args():
    """
    -h             get help on these options
    -q, --quiet    suppress audible alert
    TIME_STR       (seconds), :(seconds), (minutes):, or (minutes):(seconds)
    """
    parser = argparse.ArgumentParser(description="""
        Accurate Coffee Timer.  Takes an argument is the form SS, MM:, or
        MM:SS.  Default time = 5:30)""")
    parser.add_argument('-q', '--quiet', help='no sound', action='store_true')

    #supposedly there is an equivalent generator expression which would be
    #better
    if len([i for i in sys.argv[1:] if not i.startswith('-')]) > 0 or\
        (set(['-h', '--help']) & set(sys.argv)):
        parser.add_argument('time_str', type=str)
        return parser.parse_args()

def alert():
    """
    Print a visual alert using the toilet(/figlet) command.
    Print an audible alert using espeak speech synthesizer.
    """
    
    proc = subprocess.Popen('toilet "Done"', shell=True)
    proc.wait()
    
    today = datetime.datetime.today()
    now = today.strftime('%l:%M:%S %P')
    print('Finished at {}'.format(now))
    
    if ARGS is not None and ARGS.quiet == False:
        try:
            proc2 = subprocess.Popen(
                'play -n synth .5 sin 1000 vol 0.05 > /dev/null 2>&1', shell=True)
            proc2.wait()
        except (OSError, subprocess.CalledProcessError) as e: #if system call fails???
            cli.Cli.term_fx('up', 'Problem in sox:')
            print(traceback.format_exc()) #pylint: disable=C0325
        try:
            proc1 = subprocess.Popen('espeak -v en-us "Your coffee is ready"', shell=True)
            proc1.wait()
        except (OSError, subprocess.CalledProcessError) as e: #if system call fails???
            cli.Cli.term_fx('up', 'Problem in espeak:')
            print(traceback.format_exc()) #pylint: disable=C0325            


###############
#  CONSTANTS  #
###############
if __name__ == '__main__':# and ARGS.time_str is not None:
    ARGS = _parse_args()
else: ARGS = None

if ARGS is not None and ARGS.time_str is not None:
    TIME_STR = ARGS.time_str
else: TIME_STR = '330'

if TIME_STR[0] == ':':
    TIME_STR = '0' + TIME_STR

if TIME_STR.isdigit():
    SECONDS = float(TIME_STR)
else: SECONDS = float(subprocess.check_output(\
   './mmss.py {}'.format(TIME_STR), shell=True))

_SINCE = time.time()


##########
#  MAIN  #
##########
def main():
    """
    Starts the countdown timer, continually double-checking against clock
    time to maintain accuracy.
    """
    cli.Cli()
    remaining = SECONDS
    
    string = (subprocess.check_output('./mmss.py {}'.format(
        int(remaining)), shell=True)).decode('utf-8')
    cli.write('\033[?25l')
    cli.write('{} remaining'.format(string.rstrip()))
    while remaining >= 0:
        time.sleep(.5)
        remaining = SECONDS - time.time() + _SINCE
        string = (subprocess.check_output('./mmss.py {}'.format(
            int(remaining)), shell=True)).decode('utf-8')
        
        cli.write('\r{}'.format(string.strip()))
    alert()


    
if __name__ == '__main__':
    try:
        main()
    finally:
        cli.write('\033[?25h')
