#!/usr/bin/env python
"""
Gets a filename from the command line and opens the image in a Tk window.
"""
import sys

try:
    import Tkinter as tk
except:
    import tkinter as tk

from PIL import ImageTk, Image

__author__ = 'Chris Horn <hammerhorn@gmail.com>'
__license__ = 'GPL'


def main():
    """
    Create an app window and stick an image to it.  If running as main,
    launch main loop.
    """
    root = tk.Tk()
    root.title('Simple Tkinter Image Viewer')

    if __name__ == '__main__':
        img = ImageTk.PhotoImage(Image.open(sys.argv[1]))
    else:
        img = None

    label = tk.Label(root, image=img)
    label.pack(side='bottom', fill='both', expand='yes')
    if __name__ == '__main__':
        root.mainloop()

main()
