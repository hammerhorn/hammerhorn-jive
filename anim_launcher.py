#!/usr/bin/env python
"""
simple ASCII-mation launcher

A launcher for simple animations made using either
<class cjh.geometry.Graph> or <class cjh.igo.Goban>.

usage: anim_launcher.py [-h] [--nox] [-t DELTAT] [-d DELTAD] [-z SIZE]
                        [-f FILE] [-q]
"""
import argparse
import subprocess

try:
    import Tkinter as tk
    import tkFileDialog
except ImportError:
    try:
        import tkinter as tk
        from tkinter import filedialog as tkFileDialog
    except ImportError:
        pass
try:
    import wx
except ImportError:
    pass

from cjh.cli import Cli
from cjh.config import Config

__author__ = 'Chris Horn <hammerhorn@gmail.com>'
__license__ = 'GPL'


################
#  PROCEDURES  #
################
def _parse_args():
    """
    Parse arguments
    (see above)
    """
    parser = argparse.ArgumentParser(description='Simple ASCIImation Launcher')
    parser.add_argument(
        '--nox', action='store_true', help='text-based interface')
    parser.add_argument('-t', '--deltat', type=float, help='time interval')
    parser.add_argument(
        '-d', '--deltad', type=float, help='displacement interval')
    parser.add_argument('-z', '--size', type=int, help='board size')
    parser.add_argument(
        '-f', '--file', type=str,
        help='goban animation file (a python program)')
    parser.add_argument(
        '-q', action='count',
        help='-q,-qq   suppress welcome message/splash screen')
    if __name__ == '__main__':
        return parser.parse_args()
    else:
        return None


def _set_parameters():
    """
    Set minimum time and distance intervals.
    """
    if ARGS is not None and ARGS.deltat is not None:
        t_interval = ARGS.deltat
    else:
        t_interval = .1

    if ARGS is not None and ARGS.deltad is not None:
        d_interval = ARGS.deltad
    else:
        d_interval = 2

    if ARGS is not None and ARGS.size is not None:
        size = ARGS.size
    elif SHELL.platform in ['android']:
        size = 7
    else:
        size = 19

    if ARGS is not None and ARGS.file is not None:
        cmd_list = [ARGS.file]

#    else: cmd_list = [SHELL.arg({'EN':'module to launch', 'EO':'modulo por kom
#encigi'}[LANG])]
#    else: cmd_list = [SHELL.arg({'EN':'module to launch', 'EO':'modulo por kom
#encigi'}[LANG])]

    elif SHELL.interface == 'Tk':
        cmd_list = [tkFileDialog.askopenfile(
            parent=SHELL.main_window, mode='r', filetypes=[(
            'Python files', '*.py')], title={
            'EN': 'Choose a file', 'EO': 'Elektu dosieron'}[LANG]).name]
    else:
        cmd_list = []
    return (t_interval, d_interval, size, cmd_list)


def launch_module(cmd_list):
    """
    Play the animation.
    """
    if SHELL.interface == 'Tk':
        cmd = [word.encode(
            'utf-8') for word in CONFIG.config_dict['terminal'].split()] +\
            cmd_list
    else:
        cmd = cmd_list

#    cmd[-1] = './%s' % cmd[-1]
    #print('Command is "{}"'.format(cmd))
    #Cli().wait()

    proc = subprocess.Popen(cmd)
    proc.wait()

## Add a time counter? ##

##########
#  DATA  #
##########

## Prepare environment ##


#if __name__ == '__main__':
#    if len(sys.argv[1:]) == 0:
#        sys.argv.append('-h')

ARGS = _parse_args()
CONFIG = Config()
LANG = CONFIG.get_lang_key()

if ARGS is not None and ARGS.nox is True:
    SHELL = Cli()
else:
    SHELL = CONFIG.start_user_profile()
    if SHELL.interface in ['Tk']:
        SHELL.main_window.title(
            {'EN': 'asciimation player',
             'EO': 'ASCII bildfilm-komencigilo'}[LANG])

if SHELL.interface in ['wx', 'Tk']:
    SHELL.center_window(height_=50, width_=180)

if SHELL.interface is 'Tk':
    SHELL.msg.destroy()
    PLAY = tk.Button(
        SHELL.main_window, text={'EN': 'Play', 'EO': 'Ek'}[LANG],
        command=lambda: launch_module(CMD_LIST))
    PLAY.pack(fill=tk.BOTH, expand=1)
elif SHELL.interface is 'wx':
    PANEL = wx.Panel(SHELL.main_window, -1)
    PLAY = wx.Button(PANEL, -1, 'Play', pos=(50, 20))
    PLAY.SetDefault()

## Set animation parameters ##

##########
#  MAIN  #
##########
if __name__ == '__main__':
    if ARGS is not None and ARGS.q is None:
        SHELL.welcome('Simple ASCIImation Launcher',
            """
            A launcher for simple animations made using either cjh.Graph or
            cjh.Goban.
            """)

    T_INTERVAL, D_INTERVAL, SIZE_, CMD_LIST = _set_parameters()


def main():
    """
    Print a welcome message on first run.  If shell is Tk or wx, create a
    PLAY button.
    """

    if SHELL.interface is 'Tk':
        PLAY.focus_set()
        SHELL.main_window.mainloop()

    elif SHELL.interface is 'wx':
        SHELL.start_app()

    else:
        launch_module(CMD_LIST)

if __name__ == '__main__':
    main()
