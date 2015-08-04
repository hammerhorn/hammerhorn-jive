#!/usr/bin/env python
"""
User inputs a frequency (e.g., 5e14 is in the visible light range).
The program outputs a description of EM radiation at the given frequency.
"""
import argparse
import sys

try:
    from Tkinter import TclError
except ImportError:
    from tkinter import TclError

from cjh.config import Config
from cjh.waves import EMWave

__author__ = 'Chris Horn <hammerhorn@gmail.com>'


def _parse_args():
    """Parse arguments"""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        '-s', '--shell', type=str, help='bash, dialog, sh, Tk, wx, zenity')
    if __name__ == '__main__':
        args = parser.parse_args()
    else:
        args = None
    return args

ARGS = _parse_args()
CONFIG = Config()
if ARGS is not None and ARGS.shell is not None:
    SHELL = CONFIG.launch_selected_shell(ARGS.shell)
else:
    SHELL = CONFIG.start_user_profile()


def main():
    SHELL.welcome('Waves', 'demonstration of my Wave class')
    hz = ''

    if SHELL.interface == 'Tk':
        SHELL.msg.config(
            bg='black', fg='white', width=200, font=('courier', 9, 'bold'))
        SHELL.main_window.config(bg='black')
        SHELL.center_window(height_=100, width_=300)
        SHELL.main_window.title('EM Radiation (Hz)')
    while True:
        try:
            freq_string = SHELL.input('Frequency in Hz: ')
            hz = float(freq_string)
            #break
        except ValueError:
            sys.exit('ERROR: {} is not a float.').format(freq_string)
        emw = EMWave(hz)
        #if SHELL.interface in ["bash", "sh"]:
        SHELL.output(str(emw))
      # else:
        if SHELL.interface == 'Tk':
            #SHELL.(str(emw))
            color = str(emw).split()[0]

            # These colors are illustrative as opposed to scientific or
            # mathematical.
            fgcolor = 'black'
            if color == 'red':
                bgcolor = '#ffcccc'
            elif color == 'orange':
                bgcolor = '#ffddc0'
            elif color == 'yellow':
                bgcolor = '#ffffbb'
            elif color == 'green':
                bgcolor = '#ccffcc'
            elif color == 'blue':
                bgcolor = '#ccccff'
            elif color == 'cyan':
                bgcolor = '#bbffff'
            elif color == 'indigo':
                bgcolor = '#E1BEFA'
            elif color == 'violet':
                bgcolor = 'purple'
            else:
                bgcolor = 'black'
                fgcolor = 'white'
            try:
                SHELL.main_window.config(bg=bgcolor)
                SHELL.msg.config(bg=bgcolor, fg=fgcolor)
            except TclError:
                pass

if __name__ == '__main__':
    main()
