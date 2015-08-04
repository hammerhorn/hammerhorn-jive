#!/usr/bin/env python
#coding='utf-8'
"""
Display file with syntax highlighting.
"""
__author__ = 'Chris Horn <hammerhorn@gmail.com>'

import argparse

from cjh import cli

################
#  PROCEDURES  #
################
def _parse_args():
    """
    Parse arguments
    """
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('filename', type=str)

    if __name__ == '__main__':
        args = parser.parse_args()
    else: args = None
    return args


##########
#  DATA  #
##########
ARGS = _parse_args()


##########
#  MAIN  #
##########
def main():
    """
    Main function
    """
    #  Main
    # function
    #  here. 
    cli.less(cli.get_src_str(ARGS.filename))
if __name__ == '__main__':
    main()
