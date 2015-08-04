#!/usr/bin/env python
#coding='utf-8'
"""
New program
"""
import argparse

from cjh.cli import Cli
from cjh.igo import GameRecord, Goban
from cjh.lists import Enumeration

__author__ = 'Chris Horn <hammerhorn@gmail.com>'

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
Cli()

##########
#  MAIN  #
##########
def main():
    """
    Main function
    """
    record = GameRecord(ARGS.filename)

    game_list = record[:]
    game_label_list = [game.label for game in game_list]

    while True:
        int_response = Cli.list_menu(Enumeration(game_label_list))
        move_list = game_list[int_response - 1][:]
        print Enumeration(move_list)

        goban = Goban(game_list[int_response - 1].header_dict['SZ'])

        color = 'black'
        for move in move_list:
            Cli.wait()
            Cli.clear()
            print goban
            goban.place_stone(move.address[0], move.address[1], color)

            if color == 'black':
                color = 'white'
            elif color == 'white':
                color = 'black'

if __name__ == '__main__':
    main()
