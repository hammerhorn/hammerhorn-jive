#!/usr/bin/env python
#coding=UTF-8
"""
Parent class for all shell template objects in this package.
Stores data about the system and common methods for user interaction.
"""
import datetime, glob, os, pydoc, subprocess, sys, textwrap, time

try:
    from pygments import highlight
    from pygments.lexers import get_lexer_for_filename
    from pygments.formatters.terminal import TerminalFormatter
except ImportError:
    pass

from cjh.lists import Enumeration, PlainList
from cjh.shell import Shellib

__author__ = 'Chris Horn <hammerhorn@gmail.com>'
__license__ = 'GPL'

###########################
#  MODULE-LEVEL FUNCTIONS #
###########################
def ellipses(msg):
    """
    Print message to stdout followed by an animated '....'.
    """
    write(msg)
    for _ in range(4):
        time.sleep(.04)
        write('.')

def emph(text):
    """
    returns '[[ some text ]]' as a str
    """
    return "[[ {} ]]".format(text)

def get_src_str(file_=None, color=True):
    """
    Returns file as ANSI colored string
    """
    if file_ == None:
        file_ = sys.argv[0]
    handler = open(file_)
    code = handler.read()
    if color:
        lexer = get_lexer_for_filename(file_)
        color_string = highlight(code, lexer, TerminalFormatter())
        return color_string
    else: return code

def less(*args, **kwargs):
    """
    *doesn't really work with files in subdirectories?  Should be tested.
    """
    if 'file_' in kwargs.keys():
        filename = kwargs['file_']
        with open(filename, 'r') as file_handler:
            text = file_handler.read()
            file_handler.close()
    elif len(args) > 0:
        text = ''
        for arg in args:
            text += (' ' + arg)
        text = text.lstrip()
    if os.path.exists('/usr/bin/less'):
        pydoc.pipepager(text, cmd='less -R')
    else: # does this work?
        pydoc.pager(text)

def money(dollars):
    """
    Takes a float and returns a str, formatted as dollars.
    """
    dollars = int(dollars * 100) / 100.0
    return'${:,.2f}'.format(dollars)

def tty(msg):
    """
    Type a message to stdout one letter at a time, like a teletype
    printout.
    """
    for char in msg:
        write(char)
        time.sleep(.02)

def write(text):
    """
    Writes something to stdout, suppressing final endline.
    """
    sys.stdout.write(text)
    sys.stdout.flush()


class Fileman(object):
    @classmethod
    def pwd(cls, getstr=False):
        """
        Emulate 'pwd' command
        """
        string = os.getcwd()
        if getstr:
            return string
        else: print(string) #pylint: disable=C0325

    @staticmethod
    def ls(*args, **kwargs):
        """
        Emulate 'ls' command
        """
        if len(args) == 0:
            cwd = os.getcwd()
            file_list = os.listdir(cwd)
        else:
            file_list = []
            for arg in args:
                file_list += glob.glob(arg)

        if 'opts' in kwargs and 'B' in kwargs['opts']:
            file_list = [
                file_ for file_ in file_list if not file_.endswith('~')
            ]

        file_list.sort(key=str.lower)
        dir_list = []

        if 'opts' in kwargs and 'F' in kwargs['opts']:
            for index, file_ in enumerate(file_list):
                if os.path.isdir(file_):
                    dir_list.append(file_ + '/')
                    del file_list[index]
                elif os.access(file_, os.X_OK):
                    file_list[index] = file_ + '*'

        if 'get_list' not in kwargs or kwargs['get_list'] is not True:
            string = ''
            for dir_ in dir_list:
                string += (dir_ + '\n')
            for file_ in file_list:
                string += (file_ + '\n')
            if len(dir_list) + len(file_list) + 1 > Cli.height():
                less(string)
            else: write(string.strip())
        else:
            return dir_list + file_list


class Cli(Shellib):
    """
    depends: tput, bcat.sh, ulcat.sh, coreutils: echo, read
    """

    def __init__(self):

        #Get OS and system info.
        super(Cli, self).__init__()

        #Use bash if available
        if 'bin' in os.listdir('/') and 'bash' in os.listdir('/bin'):
            self.__class__.interface = 'bash'
        elif self.__class__.platform in ['Linux', 'android']:
            self.__class__.interface = 'sh'
        else: self.__class__.interface = 'unknown'


    ##################
    # SHARED METHODS #
    ##################
    @classmethod
    def welcome(
        cls, script_name=sys.argv[0].split('/')[-1].split('.')[0].title(),
        description='', get_str=False):
        """
        It would be good if this could capture the main docstring properly.
        """
        formatted = textwrap.dedent(description).strip()
        if cls.width() >= 40:
            width_ = 40
        else: width_ = cls.width() - 5
        formatted = textwrap.fill(formatted, initial_indent=' ' * 5,\
                                  subsequent_indent=' ' * 5, width=width_)
        formatted = cls.ul(script_name, symbol='-', width=width_) +\
            '\n' + formatted
        print(formatted + '\n') #pylint: disable=C0325
        if get_str:
            return formatted
        elif cls.is_first_run():
            cls.default_splash()
            cls.clear()
            print(formatted + '\n') #pylint: disable=C0325
            cls.wait()
        cls.clear()
        cls.titlebar()

    @classmethod
    def output(cls, msg, heading=None): #, **kwargs): #add width and height
        """
        Print text to stdout with an optional heading.
        """
        if heading:
            print(heading) #pylint: disable=C0325
        print(msg) #pylint: disable=C0325

    @classmethod
    def message(cls, msg, heading=''): #, **kwargs): #add width and height
        """
        Like cls.notify(), but with an optional heading.
        """
        #print('') #pylint: disable=C0325
        if heading:
            write(cls.ul(heading, position=1))
        cls.notify(msg)
        cls.wait()
        #print('') #pylint: disable=C0325

    @classmethod
    def notify(cls, msg):#, *args, **kwargs):
        """
        Prints message like this:

        [+]"some message"
        """
        print('\n[+] "{}"\n'.format(msg)) #pylint: disable=C0325

    @classmethod
    def outputf(cls, msg=None, heading=""):
        """
        cls.output() + '\n'
        """
        print('') #pylint: disable=C0325
        cls.output(msg + '\n', heading)

    @classmethod
    def input(cls, prompt='>'): #, *args):
        """
        Get input using the appropriate version of Python.
        """
        if cls.py_version == 2:
            return raw_input(prompt)
        elif cls.py_version == 3:
            return input(prompt)

    @classmethod
    def get_keypress(cls, prompt=''):
        """
        Accepts one char of input.  If bash is available, it is not necessary to

        hit <ENTER>.
        """
        if cls.interface == 'bash': #if bash is present or selected?

            write(prompt)
            key = subprocess.check_output("bash -c 'read -n 1 x;\
                echo -en \"$x\"'".format(prompt), shell=True)
            if len(key) > 1:
                key = key.strip()
            print('\b ') #pylint: disable=C0325

        else: key = cls.input('{}'.format(prompt))[0]
        return key.decode('utf-8')

    @classmethod
    def wait(cls, text=None): #, gui=False):
        """
        Wait for a key press
        """
        os.system('tput civis')
        try:
            if text == None:
                if cls.interface != 'bash':
                    what2press = 'enter'
                else: what2press = 'a key'
                text = (" " * 5) + ':: Press {} ::'.format(what2press)
            cls.get_keypress(text)
            cls.clear(2)
        finally:
            os.system('tput cnorm')

    @classmethod
    def width(cls):
        """
        terminal width.  really only accurate for bash.
        """
        if cls.platform == 'android':
            return 36
        elif cls.interface == 'bash':
            return int(subprocess.check_output('tput cols', shell=True))
        else: return 80

    @classmethod
    def height(cls):
        """
        Terminal height.  Only accurate for bash.
        """
        if cls.interface == 'bash':
            return int(subprocess.check_output('tput lines', shell=True))
        else: return 25

    @classmethod
    def list_menu(cls, list_obj):#, prompt="Make a selection:"):#, t="Menu Widg
        """
        Synonym: ListPrompt.input()
        """
        #list_prompt = CompactMenu(list_obj.items)
        list_prompt = ListPrompt(list_obj.items)
        return list_prompt.input()


    ######################
    # BASH-STYLE METHODS #
    ######################
    @classmethod
    def clear(cls, *args): #, **kwargs):
        """
        Clear screen; cross-platform
        """
        if len(args) == 0:
            if cls.os_name == 'posix':
                write('\x1b[2J\x1b[H')
            elif cls.platform == 'Windows':
                proc = subprocess.Popen(['cls'])
                proc.wait()
        else: write('\033[1A\033[2K' * args[0])

    @staticmethod
    def cat(**kwargs):
        """
        This should be improved
        """
        def read_from_files(filelist):
            """
            Reads from files if any filenames given.
            """
            lines = []
            for file_ in filelist:
                filehandler = open(file_)
                lines += filehandler.readlines()
                filehandler.close()
            lines = [line.strip() for line in lines]
            return lines

        if 'files' in kwargs:
            lines = read_from_files(kwargs['files'])
        else:
            lines = []
            line = ''

            try:
                while True:
                    line = Cli.input(prompt='').rstrip()
                    lines += [line]
                    print(line) #pylint: disable=C0325
            except EOFError:
                pass

        if 'return_list' in kwargs.keys() and kwargs['return_list'] == True:
            return lines
        elif 'return_str' in kwargs.keys() and kwargs['return_str'] == True:
            string = ''
            for line in lines:
                string += (line + '\n')
            return string
        elif not ('quiet' in kwargs and kwargs['quiet'] == True):
            print('') #pylint: disable=C0325
            for line in lines:
                print(line) #pylint: disable=C0325


    ##############################
    # DO THINGS WITH SOURCE CODE #
    ##############################

    #merge these with cat?
    @classmethod
    def view_source(cls, src=sys.argv[0]):
        """
        Display source
        """
        cls.term_fx('npu', src)
        print(':') #pylint: disable=C0325
        print(get_src_str(src)) #pylint: disable=C0325

    ###############################################
    # TERMINAL FONT EFFECTS (bold and underline)  #
    ###############################################

    # This whole section could be greatly simplified.

    @classmethod
    def term_fx(cls, cmds, text):
        """
        p = print to stdout (otherwise, return as str)
        b = bold
        u = underline
        n = suppress newline
        """
        #alter this to use *args in addition to the str and
        #tuple types that already work
        if 'p' in cmds:
            if 'b' in cmds:
                if 'u' in cmds:
                    if 'n' in cmds:
                        cls.__ul_b_write(text)
                    else: cls.__ul_b_print(text)
                elif 'n' in cmds:
                    cls.__bold_write(text)
                else: cls.__bold_print(text)
            elif 'u' in cmds:
                if 'n' in cmds:
                    cls.__ul_write(text)
                else: cls.__ul_print(text)
            elif 'n' in cmds:
                write(text)
            else: print(text) #pylint: disable=C0325
        else:
            string = ''
            if 'b' in cmds:
                if 'u' in cmds:
                    if 'n' in cmds:
                        string = '\033[1m\0334m{}\033[0m'.format(text)
                    else: string = '\033[1m\0334m{}\033[0m'.format(text) + '\n'

                elif 'n' in cmds:
                    string = '\033[1m{}\033[0m'.format(text)
                else: string = '\033[1m{}\033[0m'.format(text) + '\n'
            elif 'u' in cmds:
                if 'n' in cmds:
                    string = '\033[4m{}\033[0m'.format(text)
                else: string = '\033[4m{}\033[0m'.format(text) + '\n'
            elif 'n' in cmds:
                string = text
            else: string = text + '\n'
            return string

    @classmethod
    def __bold_print(cls, text):
        """
        non-bold on Windows
        """
        cls.__bold_write(text)
        print('') #pylint: disable=C0325

    @classmethod
    def __bold_write(cls, text):
        """
        non-bold on Windows
        """
        if cls.interface in ['bash', 'sh']:
            proc = subprocess.Popen(
                r'echo "\033[1m{}\033[0m\c"'.format(text), shell=True)
            proc.wait()
        else: write(text.upper())

    @classmethod
    def __ul_print(cls, text):
        """
        with bash, prints underlined text, otherwise uses '-' chars
        """
        if cls.interface in ['bash', 'sh']:
            cls.__ul_write(text + '\n')
        else: print(cls.ul(text)) #pylint: disable=C0325

    @classmethod
    def __ul_write(cls, text):
        """
        On bash, writes underlined text to the screen with no trailing newline.
        """
        if cls.interface in ['bash', 'sh']:
            proc = subprocess.Popen(
                r'echo "\033[4m{}\033[0m\c"'.format(text), shell=True)
            proc.wait()
        else: write('_{}_'.format(text))

    @classmethod
    def __ul_b_print(cls, text):
        """
        On bash, writes underlined, bold text to the screen followed by a
        newline.
        """
        cls.__ul_b_write(text + '\n')

    @classmethod
    def __ul_b_write(cls, text):
        """
        On bash, writes underlined, bold text to the screen with no trailing
        newline.
        """
        if cls.interface in ['bash', 'sh']:
            proc = subprocess.Popen(
                r'echo "\033[4m\033[1m{}\033[0m\c"'.format(text), shell=True)
            proc.wait()
        else: write('_{}_'.format(text.upper()))


    ########################
    # PAGE LAYOUT ELEMENTS #
    ########################
    @classmethod
    def print_header(cls, message=None):
        """
        Clears screen; prints a bracketed heading in the
        top left of the screen.
        """
        cls.clear()
        if message == None:
            message = sys.argv[0]
        string = '[{}]'.format(message)
        print(string) #pylint: disable=C0325

    @classmethod
    def make_page(cls, header=None, obj='', func=lambda: 0):
        """
        Make a header, print something to the screen, and call a function.
        """
        cls.print_header(header)
        print(obj) #pylint: disable=C0325
        return func()

    @classmethod
    def text_splash(cls, text, duration=2.0, flashes=1, v_center=True):
        """
        make it sleep while it does this on mobile
        """
        def message_on():
            """
            centered string on a cleared screen, for an amount of time
            'duration'
            """
            cls.clear()
            if v_center:
                print('\n' * (cls.height() // 2 - 2)) #pylint: disable=C0325
            print(text.center(cls.width())) #pylint: disable=C0325
            if flashes > 1:
                time.sleep(duration / (2.0 * flashes - 1.0))
            else: time.sleep(duration)

        def message_off():
            """
            blank screen, for an amount of time 'duration'
            """
            cls.clear()
            if flashes > 1:
                time.sleep(duration / (2.0 * flashes - 1.0))
            else: time.sleep(duration)

        message_on()
        for _ in range(int(flashes) - 1):
            message_off()
            message_on()

    @classmethod
    def default_splash(cls,
        title=sys.argv[0].split('.')[0].split('/')[-1].title(),
        year=datetime.date.today().year, duration=.5):
        """
        There is probably a simpler syntax for getting the default title....
        """
        cls.text_splash(title, duration, 1)
        cls.text_splash('(ↄ){} Chris Horn'.format(int(year)), .5, 1)
        cls.clear()


    ############
    # "TUITEX" -- text effects #
    ############
    @classmethod
    def hrule(cls, width=None, symbols='-', centered=False, string=False):
        """
        Draw a horizontal line to the screen

        of 'width' size, made up of 'symbols' str, centered or not, to stdout
        or as a str.

        (*Add 'position' keyword.)
        """
        width_ = cls.width()
        if not width:
            width = int(width_)
        elif (width < 1.0 and width >= 0.0) or (type(width) == float):
            width = int(round(width_ * width, 0))
        line = symbols * (width // len(symbols))
        if centered == True:
            line = line.center(width_)
        if string == False:
            print(line) #pylint: disable=C0325
        else: return '\n{}'.format(line)

    @classmethod
    def ul(cls, text, symbol='=', position=None, width=None):
        """
        Return some text, as a str, underlined by some symbol ('=' by default).
        """
        text_width = len(text) + 2
        understroke = (symbol * (text_width // len(symbol)))
        sym_gen = iter(symbol)
        while len(understroke) < text_width:
            understroke += sym_gen.next()
        if position and position >= 0:
            indent_pad = ' ' * position
            understroke = indent_pad + understroke
            text = indent_pad + text
        else:
            if width:
                screen_width = width
            else: screen_width = cls.width()
            if position and position < 0:
                screen_width += (2 * position)
            understroke = understroke.center(screen_width)
            text = text.strip()
            text = text.center(screen_width)
            text = text[1:-1]
        return "\n  {}\n {}".format(text, understroke)

    # it would be good if this could be combined with stuff,
    # e.g., print_header()
    @classmethod
    def titlebar(cls, text=sys.argv[0].split('/')[-1].split('.')[0]):
        """
Writes some text--the name of the running script by default--centered,
in brackets, flanked by '='s.

        e.g.,
=================================[ some text ]=================================

        or
================================[ program_name ]===============================
        """
        bracketed = '[ ' + text + ' ]'
        length = (cls.width() - len(bracketed)) // 2
        hemibar = cls.hrule(length, symbols='=', string=True).strip()
        write(hemibar + bracketed + hemibar)
        total_len = 2 * len(hemibar) + len(bracketed)
        if total_len < cls.width():
            write('=')

    @classmethod
    def box(cls, msg, symbol='*', position=None, width=None):
        """
        Print a one-line string surrounded by a border; 'symbol' keyword
        defines the str used for drawing the border, '*' is default; if
        'position' keyword >= 0, banner will be left-aligned and indented
        int 'position' spaces.  if 'position' keyword < 0 or is unused,
        banner will be centered and moved to the left by abs(position) no.
        of spaces.
        """
        msg = str(msg)
        banner_width = len(msg) + 2 * (len(symbol) + 1)
        if width:
            column_total = width
        else: column_total = cls.width()
        content = '\n'
        star_bar = (symbol * (banner_width // len(symbol)))
        sym_gen = iter(symbol)
        while len(star_bar) < banner_width:
            star_bar += sym_gen.next()
        padding = ' '
        messagef = symbol + padding + msg + padding + symbol

        if position == None or position < 0:
            if position == None:
                position = 0
            column_total += (2 * position)
            star_bar = star_bar.center(column_total)
            messagef = messagef.center(column_total)
        else:
            indent_pad = ' ' * position
            star_bar = indent_pad + star_bar
            messagef = indent_pad + messagef

        star_bar += '\n'
        messagef += '\n'
        content += star_bar + messagef + star_bar
        return content


#######################
## MENU-type CLASSES ##
#######################
class CompactMenu(PlainList):
    def __init__(self, options):
        super(CompactMenu, self).__init__(options)
        self.label = sys.argv[0].split('/')[-1].capitalize() + ' commands:'

    def __str__(self):
        """work on this"""
        string = self.label
        options = self.items
        used_letters = ''
        for option in options:
            if not option[0] in used_letters:
                used_letters += option[0]
                option = '[{}]{}'.format(option[0], option[1:])
            #else:
            string += ' {},'.format(option)
        #string.rstrip()
        #string.rstrip(',')
        string = string[0:-1]
        return string

    def input(self):
        """Gets the users selection"""
        print(self) #pylint: disable=C0325
        Cli()
        char = Cli.get_keypress(sys.argv[0].split('/')[-1].lower() + '>')
        return char #this will be improved in future


class ListPrompt(Enumeration):
    """
    An enumeration that asks the user to make a choice.
    """

    def __init__(self, l):#, **kwargs):
        super(ListPrompt, self).__init__(l) #, '')  implement heading
        if len(l) > 0:
            self.label = 'Make a choice (1-{})'.format(len(self))

    def input(self, prompt='>', hidden=False):
        """
        Get a choice from the user.
        """
        if len(self) > 10:
            long_ = True
            prompt = 'Type a number and press [ENTER]: '
        else: long_ = False
        if hidden == False:
            self.show_heading = True
            if len(self) + 4 > Cli.height():
                self.label = Cli.term_fx('bn', "Press 'q'") #make this work
                self.label += ', then make a choice (1-{})'.format(len(self))

                # can i use less() here?
                pydoc.pipepager(str(self), cmd='less -R')

            else: print(self) #pylint: disable=C0325
        else: write(self.label)

        if len(self) > 0:
            try:
                if long_:
                    sel_str = Cli.input(prompt)
                else: sel_str = Cli.get_keypress(prompt)
                if sel_str.isdigit():
                    sel = int(sel_str)
                else: sel = None
            except KeyboardInterrupt:
                print('') #pylint: disable=C0325
                return None

            while sel == None or sel > len(self) or sel < 1:
                try:
                    if (sel == None or sel < 1) and\
                        len(self) > 0 and len(self) < 10:
                        sel_str = Cli.get_keypress(prompt)
                    else:
                        sel_str = Cli.input(prompt)
                    if sel_str.isdigit():
                        sel = int(sel_str)
                    else: sel = None
                except KeyboardInterrupt:
                    print('') #pylint: disable=C0325
                    return None
            return sel
        else: return None
