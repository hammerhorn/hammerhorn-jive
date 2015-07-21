#!/usr/bin/env python
"""
Various dialogs, which can use various shells/toolkits.  Available
dialogs are: welcome, output, outputf, input, wait, message, list

$ widget.py [--OPTION] [TEXT]
"""
import argparse
import atexit

from cjh.config import Config
from cjh.lists import PlainList

__author__ = 'Chris Horn <hammerhorn@gmail.com>'
__license__ = 'GPL'


################
#  PROCEDURES  #
################
def _parse_args():
    """
    Parse command-line arguments.
    """
    parser = argparse.ArgumentParser(
        description='Test various dialogs from the command line.')
    parser.add_argument('--shell', '-s', type=str)
    parser.add_argument('--welcome', action='store_true', help='Welcome Dialog')
    parser.add_argument('--output', action='store_true', help='Output Dialog')
    parser.add_argument('--outputf', action='store_true', help='Outputf Dialog')
    parser.add_argument('--input', action='store_true', help='Input Dialog')
    parser.add_argument('--wait', action='store_true', help='Continue Dialog')
    parser.add_argument(
        '--notify', action='store_true', help='Notification Widget')
    parser.add_argument('--message', action='store_true', help='Message Dialog')
    parser.add_argument('--list', action='store_true', help='List Dialog')
    parser.add_argument('text', type=str, help='some text for captions')
    if __name__ == '__main__':
        args = parser.parse_args()
    else:
        args = None
    return args


def bye():
    """
    Marks the end of the program.  Maybe it could be moved to <cjh.shell.Cli>.
    """
    print('Goodbye.')  # pylint: disable=C0325


##########
#  DATA  #
##########
ARGS = _parse_args()
CONFIG = Config()
if ARGS is not None and ARGS.shell is not None:
    SHELL = CONFIG.launch_selected_shell(ARGS.shell)
else:
    SHELL = CONFIG.start_user_profile()
atexit.register(bye)


def main():
    """
    Display welcome message on first run, then display requested dialog
    box.
    """
#        sh.centerWindow(h=0, y_offset=200)

    if ARGS.welcome is True:
        SHELL.welcome(description=ARGS.text)

    if ARGS.message is True:
        SHELL.message(ARGS.text)

    if ARGS.output is True:
        if SHELL.interface == 'Tk':
            SHELL.center_window(height_=100, width_=200)
            SHELL.msg.config(width=200)
        SHELL.output(ARGS.text)
    #if sh.interface in ['bash', 'sh']:  sh.wait()

    if ARGS.input:
        answer = SHELL.input(ARGS.text)

        if SHELL.interface in ['zenity']:
            string = "You said \'{}\'."
        else:
            string = "You said '{}'."

        SHELL.output(string.format(answer))
        if SHELL.interface in ['bash']:
            SHELL.wait() #gui=False)

    if ARGS.wait:
        SHELL.wait(ARGS.text)

    if ARGS.outputf:
        SHELL.outputf(ARGS.text + ' ')

    if ARGS.notify:
        SHELL.notify(ARGS.text)

    if ARGS.list:
        if SHELL.interface in ['bash', 'sh']:
            SHELL.clear()
        if SHELL.interface in ['zenity', 'dialog']:
            string = "You chose \'{}\'."
        else:
            string = "You chose '{}'."
        list_ = PlainList(ARGS.text.split())
        answer = list_[SHELL.list_menu(list_) - 1]
        SHELL.output(string.format(answer))

    if SHELL == 'Tk':
        SHELL.main_window.mainloop()

#    if SHELL.interface in ["Tk"]:
#        SHELL.main_window.after(250, SHELL.main_window.destroy)

if __name__ == '__main__':
    main()
