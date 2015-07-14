#!/usr/bin/env python
"""
Displays sytem info.  Works with bash or Tk.
"""
__author__ = 'Chris Horn <hammerhorn@gmail.com>'

from cjh import cli
from cjh.config import Config

cli.Cli()
CONFIG = Config()
if __name__ == '__main__':
    SHELL = CONFIG.start_user_profile() #move mainloop statement into main(
else: SHELL = cli.Cli()

if SHELL.interface in ['wx', 'Tk']:
    SHELL.center_window(width_=475, height_=230)

if SHELL.interface == 'Tk':
#if type(SHELL) == 'cjh/tk_template.TkTemplate':
    SHELL.msg.config(bg='black', fg='chartreuse', font=('mono', 9), width=500)
    SHELL.main_window.config(bg='black')
    SHELL.main_window.title(cli.Cli.hostname)

def main():
    """
    Output system info; if using bash, use animated text.
    """
    if SHELL.interface == 'Tk':
        SHELL.view_info()
        SHELL.main_window.mainloop()
    elif SHELL.interface in ['sh', 'bash']:
        string = cli.Cli.ul('Shell Info', symbol='-', width=12, position=0)
        string += cli.Cli.view_info(get_str=True)
        cli.tty(string)
        print('\n')

if __name__ == '__main__':
    main()
