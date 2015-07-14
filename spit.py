#!/usr/bin/env python
"""
Generate a requested number of paragraphs of dummy output.
"""
import sys

from cjh.cli import Cli
from cjh.doc_format import Paragraph
from cjh.text_fill import TextGen

__author__ = 'Chris Horn <hammerhorn@gmail.com>'

if __name__ == '__main__':
    # If help flag found, print usage and exit.
    if '-h' in sys.argv or '--help' in sys.argv:
        print(
    'use: spit.py [-h] [--nopager] [number_of_paragraphs]'
    )  # pylint: disable=C0325
        sys.exit(0)
    elif {'-n', '--nopager'} & set(sys.argv):
        PAGER = False
        sys.argv = [arg for arg in sys.argv if not arg.startswith('-')]
    else:
        PAGER = True


# set PARAS
if __name__ == '__main__' and len(sys.argv[1:]) > 0:
    PARAS = int(float(sys.argv[1]))
else:
    PARAS = 20


# dummy output chatter
def main():
    """
    Produce output and print to pager.
    """
    dummy = TextGen()
    print('')  # pylint: disable=C0325
    text_str = ''
    for _ in range(PARAS):
        pgraph = Paragraph(dummy.chunk(), int(Cli.width() * 0.6), True)
        pgraph.set_lmargin(Cli.width() // 5)
        text_str += str(pgraph)
    if PAGER is True:
        Cli.less(text_str)
    else:
        print(text_str)  # pylint: disable=C0325

if __name__ == '__main__':
    main()
