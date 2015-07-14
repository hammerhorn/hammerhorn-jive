#!/usr/bin/python
"""
sentences/paragraph in generated paragraphs

This script was created to test the distribution of the number of
sentences/paragraph produced by <class cjh.text_fill.TextGen>.
Works with: bash, Tk, dialog

usage: bell.py [-h] [--nox] [-q]
"""
#    optional arguments:
#      -h, --help  show this help message and exit
#      --nox       text-based interface
#      -q          suppress welcome message
#"""

import argparse
import array

try:
    import Tkinter as tk
except ImportError:
    try:
        import tkinter as tk
    except ImportError:
        print('Error importing Tk.')  # pylint: disable=C0325

from cjh.cli import Cli
from cjh.config import Config
from cjh.text_fill import TextGen

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
    parser = argparse.ArgumentParser(description='Sentences per paragraph')
    parser.add_argument(
        '--nox', action='store_true', help='text-based interface')
    parser.add_argument(
        '-q', action='store_true', help='suppress welcome message')
    return parser.parse_args()


def _generate_results():
    """
    Generate "paragraphs" using my text_gen.chunk() method
    and make a list of the number of sentences in each one.
    """

    def count_sentences():
        """
        Returns an array of the number of sentences in each paragraph.
        """
        i_array = array.array('i')
        for _ in range(CEILING - 1):
            TEXT_GEN.chunk()
            i_array.append(TEXT_GEN.sentence_count)
        return i_array

    def format_results(int_list):
        """
        Format the results and output.
        """
        string = ''
        for j in range(2, max(int_list)):
            string += {
                'EN': '{}-sentence paragraphs: {:>3,}\n',
                'EO': 'paragrafoj havante {} frazojn: {:>3,}\n'}[LANG].format(
                j, int_list.count(j))
        return string

    def output_results(string):
        """
        Output 'string' and wait.
        """
        #Probably this could be more elegant
        if SHELL.interface == 'Tk':
            frame.config(relief='sunken', border=2)
            SHELL.msg.config(bg='white', font=('mono', 9))
        if SHELL.interface == 'dialog':
            SHELL.output(string, height=11, width=30)
        else:
            SHELL.output(string)

        #print(string)
        if SHELL.interface in ['bash', 'sh']:
            Cli.wait()
            print('')  # pylint: disable=C0325

    int_array = count_sentences()
    string = format_results(int_array)
    output_results(string)


##########
#  DATA  #
##########
if __name__ == '__main__':
    ARGS = _parse_args()
else:
    ARGS = None
CONFIG = Config()
LANG = CONFIG.get_lang_key()
if ARGS is not None and ARGS.nox is True:
    SHELL = Cli()
else:
    SHELL = CONFIG.start_user_profile()
CEILING = 1000  # number of paragraphs to be generated
TEXT_GEN = TextGen()  # object which writes the paragraphs

########
#  Tk  #
########
if SHELL.interface == 'Tk':
    SHELL.main_window.title(
        {'EN': 'Sentences/pgraph in {} pgraphs',
        'EO': 'Frazoj/pgrafo en {} pgrafoj'}[LANG].format(CEILING))

    if LANG == 'EN':
        SHELL.center_window(width_=250, height_=200, x_offset=0)
#        SHELL.msg.config(width=250, font=('sans', 8))
    elif LANG == 'EO':
        SHELL.center_window(width_=300, height_=200, x_offset=0)
#        SHELL.msg.config(width=300, font=('sans', 8))
    SHELL.msg.destroy()
    frame = tk.Frame(SHELL.main_window)
    SHELL.msg = tk.Message(frame, textvariable=SHELL.msgtxt)
    SHELL.msg.pack()
    frame.pack(padx=15, pady=10)
    #figure out how to adjust the locale
    button = tk.Button(
        SHELL.main_window, text={'EN': 'Generate {:,} paragraphs',
        'EO': 'Generi 1.000 paragrafoj'}[LANG].
        format(CEILING), command=_generate_results)
    button.pack(padx=1, pady=1, fill='both', expand=1)
    button.focus_set()


##########
#  MAIN  #
##########

def main():
    """
    Print a greeting on first run, then start the program.
    """
    if ARGS.q is False:
        SHELL.welcome(description="""
This script was created to test the distribution of sentences/"chunk"
(i.e., paragraph of dummy output) produced by class
cjh.text_fill.TextGen.
""")

    if SHELL.interface in ['Tk']:
        SHELL.main_window.mainloop()
    elif SHELL.interface in ['wx']:
        SHELL.start_app()
    else:
        print('')  # pylint: disable=C0325
        while True:
            _generate_results()

if __name__ == '__main__':
    main()
