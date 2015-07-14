#!/usr/bin/env python
#coding=UTF-8
"""
A simple text-based graphing calculator.
"""

import argparse
import os
import pickle
import subprocess

from cjh.cli import Cli
from cjh.config import Config
from cjh.igo import Goban
from cjh.lists import PlainList

__author__ = 'Chris Horn <hammerhorn@gmail.com>'


def _parse_args():
    """
    Provides these arguments:
    --infile, --size, --external, --outfile, --quiet, --skin
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--infile', type=str, help='load file')
    parser.add_argument('-s', '--size', type=int, help='plane size')
    parser.add_argument(
        '-e', '--external', type=str, help='external sgf viewer')
    parser.add_argument(
        '-o', '--outfile', type=str,
        help='basename[.txt], basename[.sgf], basename[.p]')
    parser.add_argument(
        '-q', '--quiet', help='suppress splashscreen', action='store_true')
    parser.add_argument(
        '--skin', type=str, help='a JSON file defining the symbol set')
    parser.add_argument('--shell', type=str, help='bash, Tk, or zenity')
    return parser.parse_args()


def graph_operations(cartesian):
    """
    Functions relating to the board: edit it, trash it, view it with an
    external viewer.
    """
    plane_response = Cli.make_page(
        'MENU: Plane', cartesian, lambda: SHELL.list_menu(PLANE_OPTS))

    if plane_response == 2:
        cartesian.view_edit()
    elif plane_response == 3:
        try:
            color = cartesian.color_chooser()
            cartesian.fill(color)
        except KeyboardInterrupt:
            pass
    elif plane_response == 4:
        if ARGS and ARGS.external:
            Cli.make_page(
                'FILE: {}.sgf'.format(BASENAME), cartesian,
                lambda: cartesian.write_sgf(BASENAME))

            # View board (with external app).  If gnugo is specified, append the
            #appropriate flags.
            if ARGS and ARGS.external == 'gnugo':
                proc = subprocess.Popen(
                    'gnugo --mode ascii --quiet -l {}.sgf'.format(BASENAME),
                    shell=True)
            else:
                proc = subprocess.Popen(
                    '{} {}.sgf'.format(ARGS.external, BASENAME), shell=True)
            proc.wait()

        # Trash board and create a new one the same size
        else:
            cartesian = _make_graph()
    elif plane_response == 5:
        cartesian = _make_graph()
    return cartesian


 ##############
 ## GRAPHING ##
 ##############

def refresh_main_table(cartesian):
    """
    Appends the line 'Press Ctrl-c to cancel' underneath the graph.
    """
    #global main_text
    text = str(cartesian)
    if SHELL.interface in ['bash']:
        text += '\nPress Ctrl-c to cancel'
    return text


def functions_menu(cartesian):
    """
    Add/View Functions
    """
    while True:
        funct_response = Cli.make_page(
            'MENU: Functions', cartesian, lambda: SHELL.list_menu(FUNCT_OPTS))
        if funct_response == 1:
            break
        elif funct_response == 2:
            # List attached functions--currently Polynoms only
            Cli.make_page('view functions', cartesian, cartesian.list_functs)
        elif funct_response == 3:
            # Auto-Shapes
            menu2 = PlainList(['..', 'ellipse', 'sine wave'])
            while True:
                sel2 = Cli.make_page(
                     'auto-shapes', cartesian, lambda: SHELL.list_menu(menu2))
                if sel2 == 1:
                    break
                if sel2 == 2:

                    # Ellipses/Circles
                    menu3 = PlainList(['..', 'circle', 'ellipse'])

                    # Perhaps the interface should not be like this and it
                    # should return all the way up to the 'Functions' menu?
                    # But maybe it's good as it is.
                    while True:
                        sel3 = Cli.make_page(
                             'plot an ellipse', cartesian,
                             lambda: SHELL.list_menu(menu3))
                        if sel3 == 1:
                            break
                        if sel3 == 2:
                            try:
                                color = cartesian.color_chooser()
                                Cli.make_page(
                                    'circles', cartesian,
                                    lambda: cartesian.prompt_circle(color))
                            except KeyboardInterrupt:
                                pass
                        elif sel3 == 3:
                            try:
                                color = cartesian.color_chooser()
                                Cli.make_page(
                                    'ellipse', cartesian,
                                    lambda: cartesian.prompt_ellipse(color))
                            except KeyboardInterrupt:
                                pass
                elif sel2 == 3:

                    # Sine Waves
                    try:
                        color = cartesian.color_chooser()
                        main_text = refresh_main_table(cartesian)
                        Cli.make_page(
                            'plot a sine wave', main_text,
                            lambda: cartesian.prompt_wave(color))
                    except KeyboardInterrupt:
                        pass

        elif funct_response == 4:
            cartesian.add_polynomial()
        elif funct_response == 5:
            try:
                color = cartesian.color_chooser()
                main_text = refresh_main_table(cartesian)
                Cli.make_page(
                    'plot a point', main_text, lambda: cartesian.prompt_point(
                    color))
            except KeyboardInterrupt:
                pass
    return cartesian


 #####################
 ## FILE OPERATIONS ##
 #####################

def work_with_p_files(cartesian):
    """
    Writes instance to pickle file or loads instance from pickle file.
    """
    #global file_list, pickle_list

    if ARGS and ARGS.infile:
        infile = ARGS.infile
    else:
        infile = 'save.p'

    current_dir = os.getcwd()
    file_list = os.listdir(current_dir)
    filemenu_list = ['..', 'save as pickle', 'open a pickle file']

    if infile in file_list:
        filemenu_list.append("reopen '" + infile + "'")
    menu1 = PlainList(filemenu_list)
    #pickle_list = []
    sel1 = Cli.make_page('pickle', cartesian, lambda: SHELL.list_menu(menu1))
    if sel1 == 2:
        cartesian.save_p_file(BASENAME)
    elif sel1 != 1:
        cartesian = Cli.open_p_file()
    return cartesian


def file_actions(cartesian):
    """
    work with files: open or save
    """
    sel1 = Cli.make_page(
        'MENU: File Actions', cartesian, lambda: SHELL.list_menu(FILE_OPTS))
    if sel1 == 2:
        cartesian.write_txt(BASENAME)
    elif sel1 == 3:
        cartesian.write_sgf(BASENAME)
    elif sel1 == 4:
        cartesian.save_p_file(BASENAME)
    elif sel1 == 5:
        cartesian = Cli.open_p_file()  # A = A.__class__.open_p_file()
    elif sel1 == 6:
        cartesian = work_with_p_files(cartesian)
    return cartesian


def _generate_plane_opts():
    """
    Generate [p]lane Menu
    """
    submenu_list = ['..', 'edit plane', 'fill/clear plane', 'trash plane']

    if ARGS and ARGS.external:
        desc = "write '{}.sgf' and open with {}".format(
            BASENAME, ARGS.external)
        submenu_list.insert(3, desc)
    return PlainList(submenu_list)


def _make_graph():
    """
    Initialize Graph Object
    """
    if ARGS is not None and ARGS.infile is not None:
        cartesian = pickle.load(open(ARGS.infile, 'rb'))
    elif ARGS is not None and ARGS.skin is not None:
        cartesian = Goban(SIZE, ARGS.skin, adjust_ssize=-16)
    else:
        cartesian = Goban(SIZE, sh_obj=SHELL, adjust_ssize=-16)
    return cartesian


#################
##  CONSTANTS  ##
#################

if __name__ == '__main__':
    # if -h flag present, display help and close
    ARGS = _parse_args()
else:
    ARGS = None

CONFIG = Config()

if ARGS is not None and ARGS.shell is not None:
    SHELL = CONFIG.launch_selected_shell(ARGS.shell)
else:
    SHELL = CONFIG.start_user_profile()

if ARGS is not None and ARGS.size is not None:
    SIZE = ARGS.size
elif SHELL.platform == 'android':
    SIZE = 9
else:
    SIZE = 19

if ARGS and ARGS.outfile:
    BASENAME = ARGS.outfile
    FILENAME = (ARGS.outfile + '.p')
else:
    BASENAME = 'output'
    FILENAME = 'save.p'

MAIN_OPTS = PlainList(['BOARD',
                    'FUNCTIONS',
                    'write sgf & SCORE',
                    'SAVE/RESTORE POSITION'])

PLANE_OPTS = _generate_plane_opts()
FUNCT_OPTS = PlainList([
    '..',
    'view attached polynomials',
    'AUTO-SHAPES',
    'add a polynomial',
    'add a point'
])
FILE_OPTS = PlainList(['..',
    'save graph image as text',
    'save as sgf',
    'save as pickle',
    'open a pickle file',
    'work with pickle files'])


###########
## START ##
###########
def main():
    """
    the main function
    """
    #fx_list = []

    if ARGS is not None and ARGS.quiet is False:
        SHELL.welcome(
            script_name='== simple graph calc ==',
            description='A simple text-based graphing calculator.')

    graph = _make_graph()

    # if there is an --infile, open graph in editor
    if ARGS is not None and ARGS.infile is True:
        graph.view_edit()

    # Main Loop
    while True:
        if SHELL.interface in ['bash']:
            Cli.clear()

        # Will this work on SL4A?
        main_response = Cli.make_page(
            'MENU: Main', graph, lambda: SHELL.list_menu(MAIN_OPTS))
        print(main_response)

        #use try keyboard interrupt
        if main_response == 1:
            graph = graph_operations(graph)
        elif main_response == 2:
            graph = functions_menu(graph)
        elif main_response == 3:
            graph.access_gnugo_functs(BASENAME)
        elif main_response == 4:
            graph = file_actions(graph)
        else:
            break

if __name__ == '__main__':
    main()
