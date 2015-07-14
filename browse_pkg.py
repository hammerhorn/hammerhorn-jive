#!/usr/bin/python
#coding=utf-8
"""
View source code of all modules in package 'cjh'.

Works with: bash, Tk, dialog
"""
import argparse
import os
import subprocess

try:
    import Tkinter as Tk
except ImportError:
    try:
        import tkinter as Tk
    except ImportError:
        pass

from cjh.config import Config
from cjh.lists import PlainList
from cjh import cli

__author__ = 'Chris Horn <hammerhorn@gmail.com>'
__license__ = 'GPL'


###############
#  FUNCTIONS  #
###############
def _parse_args():
    """
    Parse arguments
    """
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('-s', '--shell', type=str)
    parser.add_argument('-q', '--quiet', action='store_true')
    return parser.parse_args()


def show_code(mod_name):
    """
    Write source code to the screen.
    """
    if SHELL.interface in ['sh', 'SL4A']:
        cli.Cli.hrule()
        print(cli.Cli.ul(mod_name + '.py:'))  # pylint: disable=C0325
        cli.Cli.cat(files=['{}/{}.py'.format(BASEDIR, mod_name)])
        cli.Cli.wait()
        cli.Cli.clear()
    else:
        filename = '{}/{}.py'.format(BASEDIR, mod_name)
        if SHELL.interface in ['zenity']:
            SHELL.outputf(file=filename)
        else:
            cli.less(cli.get_src_str(file_=filename))


def show_in_new_terminal(mod_name):
    """
    show source in new window
    """
    cmd_list = ['highlighter.py', '{}/{}.py'.format(BASEDIR, mod_name)]
    if SHELL.interface == 'Tk':
        cmd = [word.encode('utf-8')
            for word in CONFIG.config_dict['terminal'].split()
            ] + cmd_list
        cmd = ' '.join(cmd)
    else:
        cmd = cmd_list
    proc = subprocess.Popen(cmd, shell=True)
    proc.wait()


###############
#  CONSTANTS  #
###############

# Parse command-line arguments
if __name__ == '__main__':
    ARGS = _parse_args()
else:
    ARGS = None

CONFIG = Config()

if ARGS and ARGS.shell:
    SHELL = CONFIG.launch_selected_shell(ARGS.shell)
else:
    SHELL = CONFIG.start_user_profile()

LANG = CONFIG.get_lang_key()

# Set the appropriate filepath
if SHELL.platform is 'android':
    BASEDIR = ('/storage/sdcard0/com.hipipal.qpyplus/lib/python2.7/' +
        'site-packages/cjh')
else:
    BASEDIR = 'cjh'

# Remove extension, sort, and create ListPrompt obj
MODULE_LIST = [_module.split('.')[0] for _module in os.listdir(BASEDIR) if
    _module.endswith('.py') and not _module.startswith('_')]
MODULE_LIST.sort()
MOD_LIST_OBJ = PlainList(MODULE_LIST)


###############
#  SET UP Tk  #
###############

# Under Tk, Create Drop-down menu
if SHELL.interface is 'Tk':
    SHELL.create_menu()
    SHELL.msg.destroy()
    SHELL.msgtxt = Tk.StringVar()
    SHELL.msg = Tk.Message(textvar=SHELL.msgtxt)
    SHELL.msgtxt.set(
        {'EN': __doc__,
        'EO': "Legi fontokodon de ĉiuj moduloj el la pakaĝo 'cjh'."}[LANG])
    SHELL.msg.config(width=200, font=('sans', 9, 'bold'))
    SHELL.msg.pack(pady=0)
    SHELL.center_window(width_=220, height_=185, y_offset=150, x_offset=0)
    SHELL.main_window.wm_title(
        {'EN': 'Simple PyModule Viewer', 'EO': 'cjh Fontokodo-Legilo'}[LANG])

    variable = Tk.StringVar(SHELL.main_window)
    variable.set({'EN': 'Select a module', 'EO': 'Elektu modulon'}[LANG])
    option_menu = Tk.OptionMenu(SHELL.main_window, variable, *MODULE_LIST)
    option_menu.pack(pady=10)

    Tk.Button(
        text={'EN': 'Go', 'EO': 'Fontokodo'}[LANG],
        command=lambda: show_in_new_terminal(variable.get())).pack()


def main():
    """
    Show Welcome dialog on first run; allow user to select a module from
    package 'cjh' and display the code, in color if possible.
    """
    if ARGS is not None and ARGS.quiet is False:
        SHELL.welcome(description="""View source code of all modules in package
        'cjh'.""")

    if SHELL.interface in ['Tk']:
        SHELL.main_window.mainloop()
    else:  # bash, etc....
        while True:
            number = cli.Cli.make_page(
                func=lambda: SHELL.list_menu(MOD_LIST_OBJ))
            show_code(MOD_LIST_OBJ[number - 1])

if __name__ == '__main__':
    main()
