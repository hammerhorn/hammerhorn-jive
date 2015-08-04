#!/usr/bin/env python
"""
Takes a frequency in Hertz and tells you what form of EM radiation exists
at that frequency.
"""
import decimal

import Tkinter as tk

from cjh.tk_template import TkTemplate
from cjh.waves import EMWave

__author__ = 'Chris Horn <hammerhorn@gmail.com>'
__license__ = 'GPL'


def calc():
    """Get entry from field and calculate the color."""
    input_str = entry.get()
    try:
        hertz = float(input_str)
    except ValueError:
        SHELL.msgtxt.set('Type Error')
        return -1
    hertz = decimal.Decimal(hertz)
    emw = EMWave(hertz)
    SHELL.msgtxt.set(str(emw))
    try:
        SHELL.msg.config(bg=str(emw).split()[0])
    except tk.TclError:
        SHELL.msg.config(bg='#D9D9D9')

SHELL = TkTemplate()
SHELL.main_window.title('EM Spectrum by Hz')
SHELL.msg.config(font=('sans', 12))

frame = tk.Frame(SHELL.main_window)
label = tk.Label(frame, text='Hz')
entry = tk.Entry(frame, width=6)
button = tk.Button(frame, text='Analyze wave', command=calc)

frame.pack()
label.pack(side='left')
entry.pack(side='left')
button.pack(padx=20)
SHELL.center_window(height_=220, width_=250)

if __name__ == '__main__':
    SHELL.main_window.mainloop()
