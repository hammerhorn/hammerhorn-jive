#!/usr/bin/env python
"""
View the available "skins" for class Goban.
"""

__author__ = 'Chris Horn <hammerhorn@gmail.com>'

import json, os

from cjh.cli import Cli
from cjh.igo import Goban
from cjh.lists import PlainList

SHELL = Cli()
SKIN_LIST = [sk for sk in os.listdir('skins') if sk.endswith('json')]
SKIN_LIST.sort(key=str.lower)
LIST_OBJ = PlainList(SKIN_LIST)

def main():
    """
    Lets user browse and preview skins for the Goban class.
    """
    goban = Goban(sh_obj=SHELL, size=9)

    if __name__ == '__main__':
        while True:
            choice = Cli.make_page(func=lambda: SHELL.list_menu(LIST_OBJ))
            skinfile = LIST_OBJ[choice - 1]
            try:
                if SHELL.py_version == 2:
                    goban.skin_dict = json.load(open('skins/' + skinfile, 'rb'))
                elif SHELL.py_version == 3:
                    file_ptr = open('skins/{}'.format(skinfile), 'rb')
                    text_buffer = file_ptr.read().decode('utf-8')
                    goban.skin_dict = json.loads(text_buffer)
            except IOError:
                Cli.text_splash(Cli.box("File Error with '{}'".format(
                    skinfile)), duration=0)
                SHELL.wait()
                continue
            goban.cursor = [0, 0]
            Cli.text_splash("== Now give '{}' a try! ==".format(
                skinfile), duration=1, flashes=4)
            goban.view_edit()

main()
