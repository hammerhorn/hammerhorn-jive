#!/usr/bin/env python
#coding=utf8
"""
An attractive clock for your terminal.
"""
import datetime
import random
import subprocess
import time

try:
    import Tkinter as tk
except ImportError:
    import tkinter as tk

from cjh import cli
from cjh.config import Config

__author__ = 'Chris Horn <hammerhorn@gmail.com>'
__license__ = 'GPL'

cli.Cli()
CONFIG = Config()
SHELL = CONFIG.start_user_profile()
MONTH_DICT = {
    'January': 'januaro',
    'February': 'februaro',
    'March': 'marto',
    'April': 'aprilo',
    'May': 'majo',
    'June': 'junio',
    'July': 'julio',
    'August': 'aŭgusto',
    'September': 'septembro',
    'October': 'oktobro',
    'November': 'novembro',
    'December': 'decembro'}

if SHELL.interface == 'Tk':
    SHELL.msg.config(border=2, relief='raised', font=('helvetica', 18, 'bold'),
        bg='#fff', width=200)
    SHELL.main_window.config(bg='dark green')
    SHELL.center_window(width_=300, height_=125)
    SHELL.main_window.title('horloĝo')


def main_loop_bash():
    """
    Check the time, refresh the clock.
    """
    while True:
        _today = datetime.datetime.today()
        now = _today.strftime('%l:%M %P')
        now = now[:-1] + 'tm'
        cmd = 'echo "{}"|toilet --gay'.format(now)  # hmmm
        try:
            string = subprocess.check_output(cmd, shell=True)
        except(OSError, subprocess.CalledProcessError):
            print("unix shell not available or " +
                  "'toilet' not available")  # pylint: disable=C0325
        en_month = _today.strftime('%B')
        month = MONTH_DICT[en_month]
        string += '\t{} estas por Stevie!!!\n\n'.format(month.capitalize())
        SHELL.output(string)
        time.sleep(1)
        cli.Cli.clear(11)


def main_loop_dialog():
    """
    Check the time, refresh the clock.
    """
    while True:
        _today = datetime.datetime.today()
        now = _today.strftime('%l:%M %P')
        now = now[:-1] + 'tm'
        string = now
        SHELL.output(string)
        time.sleep(1)


def main_loop_tk():
    """
    Check the time, refresh the clock.
    """
    message = tk.Message(
        border=2, relief='raised', font=('courier', 14, 'italic', 'bold'),
        width=270, bg='yellow', fg='blue', text="{} estas por Stevie!!!".format(
        _month.capitalize()))
    message.pack()
    now = _today.strftime('%l:%M:%S %P')
    now = now[:-1] + 'tm'
    SHELL.msgtxt.set(now)

    def update(hex_red, hex_green, hex_blue):
        """update the time and the background color."""
        today = datetime.datetime.today()
        now = today.strftime('%l:%M:%S %P')
        now = now[:-1] + 'tm'
        SHELL.msgtxt.set(now)

        red1 = int(hex_red, 16) + random.randint(-5, 5)
        if red1 > 255:
            red1 = 255
        elif red1 < 0:
            red1 = 0

        blue1 = int(hex_blue, 16) + random.randint(-5, 5)
        if blue1 > 255:
            blue1 = 255
        elif blue1 < 0:
            blue1 = 0

        green1 = int(hex_green, 16) + random.randint(-5, 5)
        if green1 > 255:
            green1 = 255
        elif green1 < 0:
            green1 = 0

        red2 = ('%x' % red1).rjust(2, '0')
        blue2 = ('%x' % blue1).rjust(2, '0')
        green2 = ('%x' % green1).rjust(2, '0')

        hex_string = '#{}{}{}'.format(red2, green2, blue2).upper()
        SHELL.main_window.config(bg=hex_string)
        SHELL.main_window.after(100, lambda: update(red2, green2, blue2))

    SHELL.main_window.after(100, lambda: update('00', '64', '00'))
    SHELL.main_window.mainloop()


def main():
    global _month, _today
    _today = datetime.datetime.today()
    en_month = _today.strftime('%B')
    _month = MONTH_DICT[en_month]

    if SHELL.interface in ['bash', 'sh']:
        main_loop_bash()
    elif SHELL.interface == 'dialog':
        main_loop_dialog()
    elif SHELL.interface == 'Tk':
        main_loop_tk()

if __name__ == '__main__':
    main()
