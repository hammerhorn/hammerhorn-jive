#!/usr/bin/env python
#coding='utf-8'
"""
Interactively browse through available "cow" files, i.e., ASCII art for
cowsay.

If fortunes program is available, it will provide the text.  Otherwise,
the user must provide a string of text.
"""
__author__ = 'Chris Horn <hammerhorn@gmail.com>'

import os, subprocess, sys

from cjh.cli import Cli
from cjh.lists import PlainList
from cjh.config import Config

##################
##  PROCEDURES  ##
##################
def parse_help_flag():
    """
    if '-h', print help and exit
    """
    if '-h' in sys.argv or '--help' in sys.argv:
        print('use: cowscript [message]')
        sys.exit(0)

def define_text():
    """
    Use  /usr/games/fortunes if present.  Otherise, read from
    command-line args.
    """
    try:
        text = subprocess.check_output('fortune -s', shell=True)
    except (OSError, subprocess.CalledProcessError) as e:
        try:
            text = sys.argv[1]
        except IndexError:
            SHELL.message('use: cowscript [message]')
            sys.exit()
    text = text.replace('"', '\"')
    if text[-1] == '\n':
        text = text[:-1]
    return text.strip()

def make_list_obj():
    """
    Populate an AbstractList object with a list of available ASCII art
    files.
    """
    tmp_list = []
    cow_list = os.listdir('/usr/share/cowsay/cows')
    for cow in cow_list:
        cow = cow.split('.')[:-1]
        cow = '.'.join(cow)
        tmp_list.append(cow)
    cow_list = tmp_list
    cow_list.sort()
    return PlainList(cow_list)


############
##  DATA  ##
############
CONFIG = Config()
SHELL = CONFIG.start_user_profile()
LIST_OBJ = make_list_obj()
MENU_FUNC = lambda: SHELL.list_menu(LIST_OBJ)


############
##  MAIN  ##
############
def main():
    """
    Feed fortunes to the selected ASCII character.
    """
    parse_help_flag()
    Cli()
    cow = ''
    message1 = define_text()
    cow_num = Cli.make_page('UP NEXT: {}'.format(message1), '', MENU_FUNC)

    while True:
        message2 = message1
        message1 = define_text()
        cow = LIST_OBJ[cow_num - 1]
        ascii_cow = subprocess.check_output(
            'echo "{}"|cowsay -f {}'.format(message2, cow), shell=True)
        ascii_cow = "\n\n{}\n\n".format(ascii_cow)
        Cli.make_page('UP NEXT: {}'.format(message1), ascii_cow, Cli.wait)
        cow_num = Cli.make_page('UP NEXT: {}'.format(message1), '', MENU_FUNC)

if __name__ == '__main__':
    main()
