#!/usr/bin/env python
"""
This is a test/demonstration of my cjh.shell module and Thing class.

* 'Make a choice (1-1)' should be a y/n confirmation instead;
add KeyboardInterrupt functionality either here or in list class if possible;
Maybe the ListPrompt could be replaced by a sh.list_menu()
"""

import argparse, sys

from cjh.cli import Cli, ListPrompt
from cjh.config import Config
from cjh.lists import PlainList, Enumeration
from cjh.things import Thing

__author__ = 'Chris Horn <hammerhorn@gmail.com>'
__license__ = 'GPL'

def _parse_args():
    """
    Parse arguments
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('--nox', action='store_true')
    if __name__ == '__main__':
        args = parser.parse_args()
    else: args = None
    return args

def form(enum, selection, function):
    """
    print appropriate header and page content, then run function f
    """
    return Cli.make_page(
        header=MENU_OPTIONS[selection - 1], obj=str(enum), func=function)

def main():
    """
    user can create a collection of Thing objects
    """
    things = []
    label_pile = [str(thing) for thing in things]
    enum = Enumeration(label_pile, 'Inventory')

    # Start Screen
    SHELL.welcome(
        'Things',
        'This is a test/demonstration of my cjh.shell module and Thing class.')
    print('')  # pylint: disable=C0325
    selection = SHELL.list_menu(MAIN_MENU)

    while True:
        if selection == 1:
            name = form(
                enum, selection, lambda: SHELL.input('\nName of thing: '))
            something = Thing()
            something.label = name
            things.append(something)
        elif selection == 2:
            form(enum, selection, Cli.wait)
        elif selection == 3:
            discard_menu = ListPrompt(label_pile)
            if len(things) > 0:
                print('Choose a <Thing> to Discard.')  # pylint: disable=C0325
                discard = form(
                    enum, selection, lambda: discard_menu.input(hidden=True))
                things.remove(things[discard - 1])
        elif selection == 4:
            print('\n')  # pylint: disable=C0325
            sys.exit('Good bye.')

        label_pile = [str(thing) for thing in things]
        enum = Enumeration(label_pile, 'Inventory')
        selection = Cli.make_page(
            header='Main Menu', obj=str(enum) + Cli.hrule(
            width=.333, string=True),
            func=lambda: SHELL.list_menu(MAIN_MENU))


ARGS = _parse_args()
CONFIG = Config()

if ARGS is not None and ARGS.nox is True:
    SHELL = Cli()
else:
    SHELL = CONFIG.start_user_profile()
    if SHELL.interface in ['Tk', 'wx']:
        SHELL.center_window()
        
MENU_OPTIONS = ['Add a <Thing> to your pile.',
                'Hide this menu',
                'Discard a <Thing>.',
                'Exit']
MAIN_MENU = PlainList(MENU_OPTIONS)


if __name__ == '__main__':
    main()
