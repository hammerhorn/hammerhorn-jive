"""
Contains modules for:
    - providing equivalent dialogs in bash, dialog, sh, SL4A, Tk, wx,
      and zenity which will run under Python 2 or Python 3.
    - providing some basic physics/math data types: Disp(lacement),
      Velocity, Polynom(ial), (Monomial) Term
    - working with dice, and go boards
    - working with musical tones
    - calculating paychecks based on an hourly wage.

This package uses the 'config.json' file to control configuration.

Attributes:
----------
shell - can be bash or Tk
terminal - name of terminal emulator, e.g., 'terminator -x '
editor - default text editor, e.g., emacs, vi, gedit, ...
"""
__author__ = "Chris Horn <hammerhorn@gmail.com>"
