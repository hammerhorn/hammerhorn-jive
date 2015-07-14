#!/usr/bin/env python
#coding=utf-8
"""
die-rolling simulator

Roll a single n-sided die.  Number of sides can be specified on the
command line; default is 6.
"""
__author__ = 'Chris Horn <hammerhorn@gmail.com>'

import argparse, sys

try:
    if sys.version_info.major == 2:
        import Tkinter as tk
    elif sys.version_info.major == 3:
        import tkinter as tk
except ImportError:
    sys.exit('Tk could not be loaded.  Ending program.')

from cjh.cli import Cli
from cjh.config import Config
from cjh.die import Die

################
#  PROCEDURES  #
################
def _parse_args():
    """
    Parse Args
    """
    parser = argparse.ArgumentParser(
        description='Variable-sided die simulator.')
    parser.add_argument(
        '-q', '--quiet', help='suppress ascii art', action='count')
    parser.add_argument(
        '-d', '--sides', type=int, help='number of sides on the current die')
    parser.add_argument(
        '-a', '--anim', action='store_true',
        help='animated effect (command-line only)')
    parser.add_argument(
        '-s', '--shell', type=str, help='bash, dialog, sh, Tk, zenity')
    return parser.parse_args()


def roll_and_output():
    """
    Roll die and show result
    """
    global _toggle

    if SHELL.interface == 'Tk':
        SHELL.msg.config(font=('mono', 10, 'bold'))
    die.roll()
    if ARGS.quiet > 2:
        sys.exit(0)
    elif ARGS.quiet == 2:
        SHELL.output(die.value)
    elif ARGS.quiet == 1:
        SHELL.output(die.__str__())
    elif SHELL.interface == 'Tk':
        _toggle = not _toggle # make this into a generator
        if _toggle is True:
            SHELL.msg.config(fg='#FF00FF')#, bg='black')
        else: SHELL.msg.config(fg='chartreuse')#, bg='black')
        SHELL.msgtxt.set(die.draw_face(verbose=True, get_str=True))
        SHELL.main_window.title(die)
    else:
        die.draw_face(verbose=True)


##########
#  DATA  #
##########
if __name__ == '__main__':
    ARGS = _parse_args()
else: ARGS = None

CONFIG = Config()
if ARGS and ARGS.shell:
    SHELL = CONFIG.launch_selected_shell(ARGS.shell)
else: SHELL = CONFIG.start_user_profile()
SHELL_NAME = SHELL.interface


lang_key = CONFIG.get_lang_key()

def change_lang(lang_code):
    global lang_key, main_menu
    lang_key = lang_code
    button.config(text={'EN':'Roll', 'EO':'Ruligi'}[lang_key])
    main_menu.destroy()
    main_menu = tk.Menu(SHELL.main_window, tearoff=0)
    lang_menu = tk.Menu(main_menu, tearoff=0)
    lang_menu.add_command(label='English', command=lambda: change_lang('EN'))
    lang_menu.add_command(label='Esperanto', command=lambda: change_lang('EO'))
    main_menu.add_cascade(
        label={'EN':'Language', 'EO':'Lingvo'}[lang_key], menu=lang_menu)
    main_menu.add_command(
        label={'EN':'Exit', 'EO':'Eliri'}[lang_key],
        command=SHELL.main_window.destroy)
    SHELL.msg.config(
        width=150, font=('mono', 12, 'bold'), bg='black', fg='white')
    SHELL.msgtxt.set(
        {'EN':'Click to roll.', 'EO':'Klaku por ruligi.'}[lang_key])
    SHELL.main_window.title({'EN':'dice', 'EO':'ĵetkuboj'}[lang_key])

# Set up Tk window
if SHELL.interface == 'Tk':
    if lang_key == 'EO':
        SHELL.main_window.title('ĵetkuboj')
    SHELL.main_window.config(bg='black')
    SHELL.msg.config(font=('mono', 12, 'bold'), bg='black', fg='white')
    SHELL.msgtxt.set(
        {'EN':'Click to roll.', 'EO':'Klaku por ruligi.'}[lang_key])

    button = tk.Button(
        SHELL.main_window, text={'EN':"Roll", 'EO':'Ruligi'}[lang_key],
        command=roll_and_output)
    button.config(
        underline=0, bg='black', fg='white', activeforeground='white',
        activebackground='black', relief=tk.FLAT, highlightcolor='white')
    button.pack(side='top')
    button.focus_set()

    main_menu = tk.Menu(SHELL.main_window, tearoff=0)
    lang_menu = tk.Menu(main_menu, tearoff=0)
    #english_checked = tk.IntVar()
    #esperanto_checked = tk.IntVar()
    #english = tk.Checkbutton(lang_menu, text='English', variable=english_check
#ed)
    #esperanto = tk.Checkbutton(lang_menu, variable=esperanto_checked)
    lang_menu.add_checkbutton(
        label='English', command=lambda: change_lang('EN'))
    lang_menu.add_checkbutton(
        label='Esperanto', command=lambda: change_lang('EO'))

    main_menu.add_cascade(
        label={'EN':'Language', 'EO':'Lingvo'}[lang_key], menu=lang_menu)
    main_menu.add_command(
        label={'EN': 'Exit', 'EO': 'Eliri'}[lang_key],
        command=SHELL.main_window.destroy)

#    menu.add_command(label='English')
#    menu.post(tk.event.x_root, tk.event.y_root)


def main_callback(event):
 #   SHELL.main_window.focus_set()
    main_menu.tk_popup(event.x_root, event.y_root, 0)
#    print "clicked at", event.x, event.y

#frame = Frame(root, width=100, height=100)
#frame.bind("<Key>", key)
if SHELL.interface == 'Tk': SHELL.main_window.bind('<Button-3>', main_callback)
#frame.pack()

if SHELL_NAME in ['wx', 'Tk']:
    SHELL.center_window(width_=200, height_=200, x_offset=100)

if ARGS and ARGS.sides > 0:
    die = Die(ARGS.sides)
else: die = Die()
_toggle = False

def main():
    """
    In a text environment, roll one die with or without animation,
    according to command-line flags.  In Tk, run the main loop.
    """
    if SHELL.interface == 'Tk':
        SHELL.main_window.mainloop()
    else:
        while True:
            if SHELL_NAME in ['bash', 'sh']:
                if ARGS is not None and ARGS.anim:
                    die.animate()
                else: roll_and_output()
            Cli.wait()
            Cli.clear(9)

if __name__ == '__main__':
    main()
