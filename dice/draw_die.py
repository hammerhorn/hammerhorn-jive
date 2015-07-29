#!/usr/bin/env python
"""
Reads an int from the command line or input prompt and draws the die.
Works with bash or Tk.

(* This does not work.)
"""
__author__ = 'Chris Horn <hammerhorn@gmail.com>'

from cjh.config import Config
from cjh.die import Die

SHELL = Config().start_user_profile()
if SHELL.interface in ['Tk', 'wx']:
    SHELL.center_window(height_=100, width_=150)


def main():
    """
    Get an int from the pipeline or from user input, and draw the die.
    """
    die = Die()
    if __name__ == '__main__':
        die.value = int(SHELL.arg())
        die.draw_face(shellib=SHELL)

main()
