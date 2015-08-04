#!/usr/bin/env python
"""
Select a source file, then view it with syntax highlighting.
"""
import argparse
import subprocess
import sys

try:
    import tkFileDialog
except ImportError:
    try:
        from tkinter import filedialog as tkFileDialog
    except:
        pass

from cjh.cli import Fileman
from cjh.config import Config
from cjh.lists import PlainList

__author__ = 'Chris Horn <hammerhorn@gmail.com>'


def _parse_args():
    """
    Scan for --shell option.
    """
    parser = argparse.ArgumentParser(description=__doc__)
    if __name__ == '__main__':
        parser.parse_args()


def view_file(file_):
    """
    View file with syntax-highlighting and paging.
    """
    proc = subprocess.Popen(
        'terminator -x highlighter.py {}'.format(file_), shell=True)
    proc.wait()

# If help flag found, print help and exit.
_parse_args()

# Get default UI name and load
CONFIG = Config()
SHELL = CONFIG.start_user_profile()


def main():
    """
    Display a greeting, view file if filename given, otherwise display
    zenity file dialog.
    """
    # Greeting
    SHELL.welcome('Simple Source Viewer', description=__doc__)

    # If filename given, view that file.
    if len(sys.argv[1:]) > 0:
        filename = sys.argv[1]
        view_file(filename)

    # Otherwise, use zenity to display a file dialog.
    else:
        while True:
            if SHELL.interface == 'zenity':
                filename = subprocess.check_output(
                    'zenity --file-selection', shell=True)
                filename = filename.strip()
            elif SHELL.interface == 'Tk':
                filename = str(tkFileDialog.askopenfilename(
                    parent=SHELL.main_window,
                    filetypes=[('Python files', '*.py')],
                    title='Choose a file')).split('/')[-1]
                if len(filename) == 0:
                    return 0
            elif SHELL.interface == 'bash':
                plain_list = PlainList([name for name in Fileman.ls(
                    opts='BF', get_list=True) if not name.endswith('/')])
                filename = plain_list[SHELL.list_menu(plain_list) - 1]
                if filename[-1] == '*':
                    filename = filename[:-1]
            view_file(filename)

if __name__ == '__main__':
    main()
