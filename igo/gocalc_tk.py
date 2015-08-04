#!/usr/bin/env python
#coding=UTF-8
"""
A windowed Tk version of the go_test program.
"""
__author__ = 'Chris Horn <hammerhorn@gmail.com>'

import argparse, pickle

try:
    import Tkinter as tk
    import tkFileDialog
except ImportError:
    import tkinter as tk
    import tkinter.filedialog as tkFileDialog

from cjh.cli import Cli
from cjh.igo import Goban
from cjh.tk_template import TkTemplate

def _parse_args():
    """
    Provides these arguments:
    """
    parser = argparse.ArgumentParser(description="""
        A mock-up of a graphical version of go_test.py.""")
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
    if __name__ == '__main__':
        args = parser.parse_args()
    else: args = None
    return args

def _set_size():
    """
    make this a constant
    """
    if ARGS is not None and ARGS.size is not None:
        size_ = ARGS.size
    elif SHELL.platform == 'android':
        size_ = 9
    else: size_ = 19
    return size_

def _setup():
    """
    Load a pickle file if specified, otherwise create a new Graph
    object.
    """
    if ARGS is not None and ARGS.infile is not None:
        graph_ = pickle.load(open(ARGS.infile, 'rb'))
    else: graph_ = new_graph()
    return graph_

def _set_filenames():
    """
    set filename for output pickle file
    """
    if ARGS is not None and ARGS.outfile is not None:
        basename = ARGS.outfile
        filename = (ARGS.outfile + '.p')
    else:
        basename = 'output'
        filename = 'save.p'
    return basename, filename

def _status_bar():
    """declare Tk status bar"""
    global st_bar
    st_bar = tk.Frame(SHELL.main_window, relief=tk.SUNKEN, border=1)
    st_bar.pack(side=tk.BOTTOM, fill=tk.X, pady=2, padx=2)

def _define_menu():
    """
    Define a menu bar for our window.
    """
    SHELL.mainmenu = tk.Menu(SHELL.main_window, tearoff=0)

    ## 'File' Menu ##
    filemenu = tk.Menu(SHELL.mainmenu, tearoff=0)
    filemenu.add_command(
        label='Discard & Start New', command=new_graph, underline=16)

    savemenu = tk.Menu(filemenu, tearoff=0)

    # this should be moved into the geometry class
    def save_p():
        """Tk actions needed to save as pickle"""
        filename = tkFileDialog.asksaveasfilename(
            parent=SHELL.main_window, title='Choose a file', filetypes=[(
            'Pickle files', '*.p')])

        local_name = filename.split('/')[-1]
        basename = local_name.split('.')[0] #this could be a problem
        graph.save_p_file(basename)

    def save_txt():
        """Save as text diagram."""
        filename = tkFileDialog.asksaveasfilename(
            parent=SHELL.main_window, title='Choose a file')

        local_name = filename.split('/')[-1]
        basename = local_name.split('.')[0] #this could be a problem
        graph.write_txt(basename)

    savemenu.add_command(label='pickle', underline=0, command=save_p)
    savemenu.add_command(label='SGF', underline=0, state=tk.DISABLED)
    savemenu.add_separator()
    savemenu.add_command(label='Export as text', underline=0, command=save_txt)

    def load_p_file():
        """load pickle file with Tk"""
        global graph
        graph = SHELL.open_p_file()
        SHELL.msgtxt.set(
            Cli.ul(graph.label.title(), width=SIZE*2+6) + str(graph))
        graph.sh_obj = SHELL

    openmenu = tk.Menu(filemenu, tearoff=0)
    openmenu.add_command(label='pickle', underline=0, command=load_p_file)
    openmenu.add_command(label='SGF', underline=0, state=tk.DISABLED)

    filemenu.add_cascade(label='Open', menu=openmenu, underline=0)
    filemenu.add_cascade(label='Save As', menu=savemenu, underline=0)
    filemenu.add_separator()
    filemenu.add_command(
        label='Quit', command=SHELL.main_window.destroy, underline=0)
    SHELL.mainmenu.add_cascade(label='File', menu=filemenu, underline=0)

    ## 'Edit' Menu ##
    planemenu = tk.Menu(SHELL.mainmenu, tearoff=0)
    planemenu.add_checkbutton(label='Locked', state=tk.DISABLED)
    planemenu.add_command(label='Fill/clear', command=fill, underline=0)
    SHELL.mainmenu.add_cascade(label='Edit', menu=planemenu, underline=0)

    ## 'Function' Menu ##
    funcmenu = tk.Menu(SHELL.mainmenu, tearoff=0)

    def plot_circle():
        """
        Calls color-chooser dialog, and dialog prompts, then plots
        circle.
        """
        color = graph.color_chooser()
        graph.prompt_circle(color)
        SHELL.msgtxt.set(
            Cli.ul(graph.label.title(), width=SIZE*2+6) + str(graph))

    def plot_ellipse():
        """
        Calls color-chooser dialog, and dialog prompts, then plots
        circle.
        """
        color = graph.color_chooser()
        graph.prompt_ellipse(color)
        SHELL.msgtxt.set(
            Cli.ul(graph.label.title(), width=SIZE*2+6) + str(graph))

    def plot_wave():
        """
        Calls color-chooser dialog, and dialog prompts, then plots
        wave.
        """
        color = graph.color_chooser()
        graph.prompt_wave(color)
        SHELL.msgtxt.set(
            Cli.ul(graph.label.title(), width=SIZE*2+6) + str(graph))

    def plot_point():
        """
        Calls color-chooser dialog, and dialog prompts, then plots
        point.
        """
        color = graph.color_chooser()
        graph.prompt_point(color)
        SHELL.msgtxt.set(
            Cli.ul(graph.label.title(), width=SIZE*2+6) + str(graph))

    def add_polynomial():
        """
        Dispatches appropriate dialogs, then plots
        polynomial, adding it to the polynmial list.
        """
        graph.add_polynomial()
        SHELL.msgtxt.set(
            Cli.ul(graph.label.title(), width=SIZE*2+6) + str(graph))

    shapemenu = tk.Menu(funcmenu, tearoff=0)
    ellipsemenu = tk.Menu(shapemenu, tearoff=0)
    ellipsemenu.add_command(label='Ellipse', command=plot_ellipse, underline=0)
    ellipsemenu.add_command(label='Circle', command=plot_circle, underline=0)

    shapemenu.add_cascade(label='Ellipse', menu=ellipsemenu, underline=0)
    shapemenu.add_command(label='Sine wave', command=plot_wave, underline=0)

    funcmenu.add_command(
        label='Add polynomial', command=add_polynomial, underline=0)
    funcmenu.add_command(
        label='View attached polynomials', command=graph.list_functs,
        underline=0)
    funcmenu.add_separator()
    funcmenu.add_cascade(label='Add shape', menu=shapemenu, underline=4)
    funcmenu.add_command(label='Add point', command=plot_point, underline=4)
    SHELL.mainmenu.add_cascade(label='Function', menu=funcmenu, underline=1)

    scoringmenu = tk.Menu(SHELL.mainmenu, tearoff=0)
    SHELL.mainmenu.add_cascade(label='Scoring', menu=scoringmenu)

    SHELL.main_window.config(menu=SHELL.mainmenu)

def _position_callback(event):
    """
    Writes the position of the cursor to the statusbar.
    """
    SHELL.main_window.focus_set()
    var1.set(
        'hovering at {}, {} ({},{})'.format(event.x, event.y, *pixel2cartesian(
        event.x, event.y)))

def _click_callback(event):
    """
    Feedback to click event, i.e., places a stone/plots a point at the
    spot clicked.
    """
    SHELL.main_window.focus_set()
    var1.set('clicked at {}, {}'.format(event.x, event.y))
    cartes_tuple = pixel2cartesian(event.x, event.y)
    color_ = graph.plane[cartes_tuple[0] + (graph.size // 2)][
        (graph.size // 2) - cartes_tuple[1]].marker
    if color_ == 'black':
        color_ = 'white'
    elif color_ == 'white':
        color_ = 'empty' # THE CLASS SEEMS TO TAKE CARE OF HOSHI, etc.
    elif color_ in ['empty', 'hoshi', 'x_axis', 'origin', 'y_axis']:
        color_ = 'black'
    graph.plot_point(*cartes_tuple, color=color_)
    SHELL.msgtxt.set(Cli.ul(graph.label.title(), width=SIZE*2+6) + str(graph))

def _key(event):
    """gives feedback to keypresses on the status bar"""
    var1.set('pressed {}'.format(repr(event.char)))

def create_mainwin():
    """
    Set the attributes of the main window.
    """
    SHELL.main_window.title('Goban Art-Calc')
    SHELL.main_window.geometry('400x485+400+300')
    SHELL.msg.config(
        fg='black', bg='#FFEE99', font=('mono', 10), width=465, border=2,
        relief=tk.RAISED)

def new_graph():
    """
    Load JSON skinfile if specified and create a new goban instance
    """
    if ARGS is not None and ARGS.skin is not None:
        plane = Goban(sh_obj=SHELL, size=SIZE, skinfile=ARGS.skin)
    else: plane = Goban(size=SIZE, sh_obj=SHELL)
    SHELL.msgtxt.set(Cli.ul(plane.label.title(), width=SIZE*2+6) + str(plane))
    return plane

def fill():
    """
    Call the graphs fill() method and refresh the text of the message
    widget.
    """
    graph.fill(graph.color_chooser())
    SHELL.msgtxt.set(Cli.ul(graph.label.title(), width=SIZE*2+6) + str(graph))

def pixel2cartesian(x_pix, y_pix):
    """
    Converts a tuple of pixel numbers to an (x, y) ordered pair.
    """
    cartesian_x = 0.0 + (x_pix - CENTER[0])/LETTER_SIZE
    cartesian_y = 0.0 - (y_pix - CENTER[1])/LETTER_SIZE
    if cartesian_y > 0:
        cartesian_y -= .5
    elif cartesian_y < 0:
        cartesian_y += .5
    return int(round(cartesian_x)), int(round(cartesian_y))

##############
## BEGINNNG ##
##############
ARGS = _parse_args()
SHELL = TkTemplate()
SIZE = _set_size()
BASENAME, FILENAME = _set_filenames()

graph = _setup()
create_mainwin()
_define_menu()
_status_bar()

var1 = tk.StringVar()

#CENTER = (188, 234) #for fontsize 10
#CENTER = (140, 185) #for 13 x 13
#CENTER = (125, 170) #for 11 x 11
#CENTER = (108, 150) #for 9 x 9

CENTER = (36 + 8 * graph.size, 82 + 8 * graph.size)

LETTER_SIZE = 16.0  #for fontsize 10

status_bar_label = tk.Label(st_bar, textvariable=var1)
status_bar_label.pack(side=tk.RIGHT)

SHELL.main_window.bind('<Key>', _key)
SHELL.main_window.bind('<Motion>', _position_callback)
SHELL.main_window.bind('<Button-1>', _click_callback)

if __name__ == '__main__':
    tk.mainloop()
