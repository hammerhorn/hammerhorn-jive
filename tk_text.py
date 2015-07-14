#!/usr/bin/env python
"""
A simple Tk text editor
"""
import sys

try:
    import Tkinter as tk
    import tkFileDialog
except ImportError:
    try:
        import tkinter as tk
        from tkinter import filedialog as tkFileDialog
    except ImportError:
        sys.exit('Tk library not available.')

__author__ = 'Chris Horn <hammerhorn@gmail.com>'
__license__ = 'GPL'


def main():
    """
    Set up Tk objects.  If running as a main program, launch the main
    loop.
    """
    root = tk.Tk()
    root.title('Simple Tk Notepad')
    textbox = tk.Text(root, font=('courier', 9))
    textbox.pack(expand=1, fill=tk.BOTH)

    def open_file(filename=None):
        """
        Open file name specified.
        """
        if filename is None:
            file_ptr = tkFileDialog.askopenfile(
                parent=root, mode='r', title='Choose a file')
        else:
            file_ptr = open(filename, 'r')
        textbox.insert('1.0', file_ptr.read())
        file_ptr.close()

    def save():
        """
        Save to file name specified.
        """
        file_ptr = tkFileDialog.asksaveasfile(
            parent=root, mode='w', title='Choose a file')
        file_ptr.write(textbox.get('1.0', 'end'))
        file_ptr.close()

    # Define Main Menu
    mainmenu = tk.Menu(root, tearoff=0)
    filemenu = tk.Menu(mainmenu, tearoff=0)
    filemenu.add_command(label='Open', command=open_file, underline=0)
    filemenu.add_command(label='Save', command=save, underline=0)
    filemenu.add_separator()
    filemenu.add_command(label='Quit', command=root.destroy, underline=0)
    mainmenu.add_cascade(label='File', menu=filemenu, underline=0)
    root.config(menu=mainmenu)

    if __name__ == '__main__':
        if len(sys.argv) > 1:
            open_file(sys.argv[1])
        root.mainloop()

main()
