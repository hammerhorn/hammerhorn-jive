#!/usr/bin/env python
"""
Python 2 or 3
"""
import sys

try:
    import Tkinter as tk
except ImportError:
    try:
        import tkinter as tk
    except ImportError:
        pass

from cjh import config

CONFIG = config.Config()
SHELL = CONFIG.start_user_profile()

def main():
    """
    Emulates the cat command.
    """
    if SHELL.interface == 'Tk':
        textbox = tk.Text(SHELL.main_window, font=('courier', 9), bg='black', fg = '#0F0')
        SHELL.center_window(height_=400, width_=600)
        SHELL.msg.destroy()
        textbox.pack(expand=1, fill=tk.BOTH)

    try:
        if len(sys.argv[1:]) >= 1:
            for filename in sys.argv[1:]:
                file_ptr = open(filename)
                buf = file_ptr.read()
                file_ptr.close()
                if SHELL.interface == 'Tk':
                    textbox.insert('1.0', buf)
        else:
            buf = SHELL.input()
            if SHELL.interface == 'Tk':
                textbox.insert('1.0', buf)
            while True:
                try:
                    buf += '\n' + SHELL.input()
                except EOFError:
                    break
                finally:
                    if SHELL.interface == 'Tk':
                        textbox.delete('1.0', tk.END)
                        textbox.insert('1.0', buf)

    except (IOError, AttributeError) as e:
        pass

    finally:
        print(buf)  # pylint: disable=C0325

if __name__ == '__main__':
    main()
