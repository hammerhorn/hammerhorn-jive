#!/usr/bin/python
#coding=utf-8
'''
 Module: shell
Classes: Shellib, Cli, DialogGui, Thing, AbstractList, PlainList, VerticalList, 
         ItemList, Enumeration, ListPrompt, TkDialog, TkInput, TkList
'''
#Standard Library Modules
import datetime, json, math, os, pickle, platform, subprocess, sys, textwrap, time, pydoc
from random import randint
#from tkinter.ttk import *
#Third-Party Modules

class Shellib(object):
    '''
    Intended as an abstract parent class.  Common methods needed by ANY shell, 
    graphical OR text-based.'''

    """Initialize class (i.e., static) variables"""
    os_name = os.name
    platform = platform.system()
    py_version = sys.version_info.major
    kernel, hostname, release, machine, processor = os.uname()

    """If android os, set platform"""
    global android
    try: 
        import androidhelper as android
        platform = 'android'
    except: 
        try:
            import android
            platform = 'android'
        except: pass

    """Try to import pygments library."""
    if platform != 'android':
        try:
            global highlight, PythonLexer, get_lexer_for_filename, TerminalFormatter
            from pygments import highlight
            from pygments.lexers import PythonLexer, get_lexer_for_filename
            from pygments.formatters import TerminalFormatter
        except: print("Could not import module 'pygments'.")

    @classmethod
    def view_info(cls, **kwargs):
        '''
        SYSTEM INFO: Displays contained info, formatted nicely
        '''
        minor_release = "Python {}.{}".format(cls.py_version, sys.version_info.minor)
        wxh = "{} x {}".format(cls.width(), cls.height())
        d = {'OS': cls.os_name, 
             'platform': cls.platform, 
             'release': platform.release(), 
             'version': minor_release, 
             'term/screen size': wxh,
             'kernel': cls.kernel,
             'hostname': cls.hostname,
             'release': cls.release,
             'machine': cls.machine,
             'processor': cls.processor}
        l = d.keys()
        l.sort()
        length = max([len(i) for i in l])
        fmt_str = "{:>" + str(length) + "}: {}"
        s = '\n'
        for i, v in enumerate(l): s += (fmt_str.format(v, d[v]) + '\n')
        s += '\n'
        cls.output(s, heading="Shell Info", width=500, height=250, x=0, y=0) 

    @classmethod
    def get_keypress(cls, prompt=''):
        if cls.interface == 'bash': #if bash is present or selected?
            cls.write(prompt)
            key =  subprocess.check_output("bash -c 'read -n 1 x; echo -e \"$x\"'".format(prompt), shell=True)
            if len(key) > 1 : key = key.strip()
            print('\b ')
        else: key = cls.input('{}'.format(prompt))
        return key.decode('utf-8')


    ########
    # ARGS #
    ########
    current_arg_index = 1
    
    @classmethod 
    def arg(cls, *prompt_list):
        if len(prompt_list) == 0: prompt_list = ('',)

        prompt_lengths = [len(prompt) for prompt in prompt_list]
        max_prompt_len = max(prompt_lengths)

        try:        
            val = sys.argv[cls.current_arg_index]
            cls.current_arg_index += 1
            return val
        except:
            while True:
                #try:
                val = cls.input((' {:>' + str(max_prompt_len) + '}: ').format(prompt_list[cls.current_arg_index - 1]))
                cls.current_arg_index += 1
                break
                #except: pass
            return val


    ##################
    #  FILE ACTIONS  #
    ##################
    @classmethod
    def SavePrompt(cls, filename, dir_name):
        '''
        Confirm filename to save as.
        '''
        print('\n')
        response = cls.get_keypress("Save as {}'{}'? ".format(dir_name, filename))
        while response != 'y':
            if response == 'n':
                print('')
                filename = cls.input('save to filename: ')
                break
        return filename

    @classmethod
    def open_p_file(cls, filename=None):
        '''
         Possible forms:
        =================
        obj = obj.open_p_file()
        obj = cls.open_p_file()
        obj = obj,open_p_file(filename)
        obj = cls.open_p_file(filename)
        '''
        cls.print_header('FILE: Open a pickle file')
        if filename != None: pass 
        else:
            file_list = os.listdir(os.getcwd())
            pickle_list = [file for file in file_list if file.endswith('.p')]

            #'''Prompt user for a filename, if none given'''
            open_menu = ListPrompt(pickle_list)
            open_menu.label = "Choose a file to open:"
            filename = pickle_list[open_menu.input() - 1]
        f = open(filename, 'rb')    
        return pickle.load(f)


    @classmethod
    def report_filesave(cls, filename, interactive=True, **kwargs):
        stats = os.stat(filename)
        message = "{} bytes written to '{}' on {}.".format(stats.st_size, filename, time.ctime(stats.st_ctime))
        if cls.interface == "SL4A": cls.notify(message)
        else:
            cls.output(message)
            if interactive == True: cls.wait()

    @classmethod
    def radioButtonDialog(cls, question, options):
        return cls.list_menu(AbstractList(options), question)


class Cli(Shellib):
    '''
    depends: tput, bcat.sh, ulcat.sh, coreutils: echo, read 
    '''
    # Use bash if available
    if 'bin' in os.listdir('/') and 'bash' in os.listdir('/bin'): interface = 'bash'
    elif Shellib.platform in ['Linux', 'android']: interface = 'sh'
    else: interface = 'unknown'


    ##############################
    # DO THINGS WITH SOURCE CODE #
    ##############################
    @classmethod
    def view_source(cls, src=sys.argv[0]):
        '''Display source'''
        #cls.hrule()
        cls.term_fx('npu', src)
        print(':')
        print(cls.get_src_str(src))

    @classmethod
    def get_src_str(cls, file=None, color=True):
        if file == None: file = sys.argv[0]
        f = open(file)
        code = f.read()
        if color: 
            lexer = get_lexer_for_filename(file)
            s = highlight(code, lexer, TerminalFormatter())
            return s
        else: return code  


    ##################
    # SHARED METHODS #
    ##################
    @classmethod
    def welcome(cls, script_name=sys.argv[0].split('/')[-1].split('.')[0].title(), description="", get_str=False):
        '''
        It would be good if this could capture the main docstring properly.
        '''
        cls.clear()
        #box_indent = 22 - (len(script_name) // 2)
        box_indent = 8
        # use ul.write instead?

        s = textwrap.dedent(description).strip()

        if cls.width() >= 40: w = 40
        else: w = cls.width() - 5

        s = textwrap.fill(s, initial_indent = ' ' * 5, subsequent_indent=' ' * 5, width=w)
        s = cls.box(script_name, position=box_indent) + s
        
        if get_str: return s
        else:
            #cls.print_header()
            print(s + '\n\n')
            cls.wait()
            cls.clear()
        print(cls.box(script_name, position=box_indent)) 

    @staticmethod
    def output(msg, heading=None, **kwargs):
        if heading: print(heading)
        print(msg)

    @classmethod
    def message(cls, msg, heading="", **kwargs):
        print("")
        if heading:
            cls.write(cls.ul(heading, position=1))
        cls.notify(msg) 
        cls.wait()
        print('')

    @classmethod
    def notify(cls, msg, *args, **kwargs):
        print('\n[{}] {}\n'.format(time.strftime('%l:%M:%S%P'), msg))

    @classmethod
    def outputf(cls, msg=None, heading="", width=None, height=None, file=None, **kwargs):
        print('')
        cls.output(msg + '\n', heading)

    @classmethod
    def input(cls, prompt='>', *args):
        if cls.py_version == 2: return raw_input(prompt)
        elif cls.py_version == 3: return input(prompt)

    @classmethod
    def wait(cls, text=None, gui=False):
        '''
        Wait for a key press
        '''
        if text == None:
            if cls.interface != 'bash': what2press = 'enter'
            else: what2press = 'a key'
            text = (" " * 5) + ":: Press {} ::".format(what2press)
        cls.get_keypress(text)
        print('')

    @classmethod
    def width(cls):
        if  cls.platform == 'android': return 36
        elif cls.interface == 'bash': return int(subprocess.check_output('tput cols', shell=True))
        else: return 80

    @classmethod
    def height(cls):
        if cls.interface == 'bash': return  int(subprocess.check_output("tput lines", shell=True))
        else: return 25

    @staticmethod
    def list_menu(list_obj, p="Make a selection:", t="Menu Widget"):
        lp = ListPrompt(list_obj.items)
        return lp.input()


    ######################
    # BASH-STYLE METHODS #
    ######################
    @classmethod
    def clear(cls, **kwargs):
        '''
        Clear screen; cross-platform
        '''
        if cls.os_name == 'posix': cls.write("\x1b[2J\x1b[H")
        elif cls.platform == 'Windows': os.system('cls')

    @classmethod
    def pwd(cls, getstr=False, gui=True):
        '''
        Emulate 'pwd' command
        '''
        s = os.getcwd()
        if getstr: return s
        else: print(s)

    @staticmethod
    def ls(*args):
        '''
        Emulate 'ls' command
        '''
        for f in os.listdir(os.getcwd()): 
            if not (('-B' in args) and (f[-1] == '~')):
                print(f)

    @classmethod
    def less(cls, *args, **kwargs):
        '''doesn't really work with files in subdirectories'''
        if 'file' in kwargs.keys():
        #arg = arg.strip() 
        #if arg in os.listdir('/home/cjhorn/bin'): 
            filename = kwargs['file']
            with open(filename, 'r') as f:
                text = f.read()
                f.close()
            #print text
            #os.system('less ' + filename)# this
        elif len(args) > 0:
            text = args[0]
  
        #else: sys.exit() #text = arg
        try: pydoc.pipepager(text, cmd='less -R')
#                #os.system('echo "' + text + '"|less') # this
        except: 
            try: pydoc.pager(text)
            except: 
                try: os.system('echo "{}"|more'.format(text))
                except:
                    print(text)
                    cls.wait()


    @staticmethod
    def cat(*files, **kwargs):

        def read_from_files(filelist):
            lines = []
            for file in filelist:
                f = open(file)
                lines += f.readlines()
                f.close()
            return lines

        if len(files) > 0: lines = read_from_files(files)
        else: lines = sys.stdin.readlines()
        tmp_lines = []
        if 'quiet' in kwargs.keys() and kwargs['quiet'] == True: suppress = True
        else: suppress = False    
        for line in lines:
            line = line.rstrip()
            tmp_lines.append(line)    
            if suppress == False: print(line)
        lines = tmp_lines
        if 'return_list' in kwargs.keys() and kwargs['return_list'] == True: return lines
        elif 'return_str' in kwargs.keys() and kwargs['return_str'] == True:
            s = ''
            for line in lines: s += line
            return s

  
    ###############################################
    # TERMINAL FONT EFFECTS (bold and underline)  #
    ###############################################
    @classmethod
    def write(cls, text):
        sys.stdout.write(text)
        sys.stdout.flush() 

    @classmethod
    def term_fx(cls, cmds, text):
        #alter this to use *args in addition to the str and 
        #tuple types that already work
        if 'p' in cmds:
            if 'b' in cmds:
                if 'u' in cmds:
                    if 'n' in cmds: cls.ul_b_write(text)
                    else: cls.ul_b_print(text)
                elif 'n' in cmds: cls.bold_write(text)
                else: cls.bold_print(text)
            elif 'u' in cmds:
                if 'n' in cmds: cls.ul_write(text)
                else: cls.ul_print(text)
            elif 'n' in cmds: cls.write(text)
            else: print(text)
 

    # These will be deprecated:
    @classmethod
    def bold_print(cls, text):
        '''
        non-bold on Windows
        '''
        cls.bold_write(text)
        print("")

    @classmethod
    def bold_write(cls, text):
        '''
        non-bold on Windows
        '''
        if cls.interface in ['bash']: os.system('echo -n "{}"|bcat.sh'.format(text))
        else: cls.write(text.upper())

    @classmethod
    def ul_print(cls, text):
        if cls.interface == 'bash': cls.ul_write(text + '\n')
        else: print(cls.ul(text))

    @classmethod
    def ul_write(cls, text):
        if cls.interface in ['bash']: os.system('echo -n "{}"|ulcat.sh'.format(text))
        else: cls.write("_{}_".format(text))

    @classmethod
    def ul_b_print(cls, text):
        os.system('echo "{}"|ulcat.sh|bcat.sh'.format(text))

    @classmethod
    def ul_b_write(cls, text):
        if cls.interface in ['bash']: os.system('echo -n "{}"|ulcat.sh|bcat.sh'.format(text))
        else: cls.write("_{}_".format(text.upper()))

    '''
    #    @classmethod
    #    def b_str(cls, text):
    #        return subprocess.check_output('echo "' + text + '"|bcat')
    '''

    ########################
    # PAGE LAYOUT ELEMENTS #
    ########################
    @classmethod
    def print_header(cls, message=None):
        cls.clear()
        if message == None: message = sys.argv[0]
        s = "[{}]".format(message)
        print(s)

    @classmethod
    def make_page(cls, header=None, obj='', func=lambda:0):
        cls.print_header(header)
        print(obj)
        return func()

    @classmethod                                                                                                                
    def text_splash(cls, text, duration=2.0, flashes=1, v_center=True):
        '''make it sleep while it does this on mobile'''
        def message_on():
            cls.clear(delay=False)
            if v_center: print("\n" * (cls.height() // 2 - 2))
            print(text.center(cls.width()))
            if flashes > 1: time.sleep(duration / (2.0 * flashes - 1.0))
            else: time.sleep(duration)

        def message_off():
            cls.clear(delay=False)
            if flashes > 1: time.sleep(duration / (2.0 * flashes - 1.0))
            else: time.sleep(duration)

        message_on()
        for flash in range(int(flashes) - 1):
            message_off()
            message_on()

    @classmethod
    def default_splash(cls, title=sys.argv[0].split('.')[0].split('/')[-1].title(), year=datetime.date.today().year, duration=.5):
        '''
        There is probably a simpler syntax for getting the default title....
        '''
        cls.text_splash(title, duration, 1)
        cls.text_splash('(ↄ){} Chris Horn'.format(int(year)), .5, 1)
        cls.clear(delay=False)


    ############
    # "TUITEX" #
    ############
    @staticmethod
    def emph(text):
        return "[[ {} ]]".format(text)

    @staticmethod
    def money(d):
        d = math.trunc(d * 100)
        return('${:,.2f}'.format(d/100.0))

    @classmethod
    def hrule(cls, width=None, symbols='-', centered=False, string=False):
        #, position=False): add position valuable                                                        \
        w = cls.width()
        if not width: width=int(w)
        elif (width < 1.0 and width >= 0.0) or (type(width) == float):
            width = int(round(w * width, 0))
        line = symbols * (width // len(symbols))
        if centered == True: line = line.center(w)
        if string == False:print(line)
        else: return "\n{}".format(line)

    @classmethod
    def ul(cls, text, symbol='=', position=None, width=None):
        text_width = len(text) + 2
        understroke = (symbol * (text_width // len(symbol)))
        sym_gen = iter(symbol)
        while len(understroke) < text_width: understroke += sym_gen.next()
        if position and position >= 0:
            indent_pad = ' ' * position
            understroke = indent_pad + understroke
            text = indent_pad + text
        else:
            if width: screen_width = width
            else: screen_width = cls.width()
            if position and position < 0: screen_width += (2 * position)
            understroke = understroke.center(screen_width)
            text = text.strip()
            text = text.center(screen_width)
            text = text[1:-1]
        return "\n  {}\n {}".format(text, understroke)

    @classmethod
    def box(cls, s, symbol='*', position=None):
        '''
        Print a one-line string surrounded by a border; 'symbol' keyword
        defines the str used for drawing the border, '*' is default; if
        'position' keyword >= 0, banner will be left-aligned and indented
        int 'position' spaces.  if 'position' keyword < 0 or is unused,
        banner will be centered and moved to the left by abs(position) no.
        of spaces.
        '''
        s = str(s)
        banner_width  = len(s) + 2 * (len(symbol) + 1)
        column_total  = cls.width()
        content = '\n'
        star_bar = (symbol * (banner_width // len(symbol)))
        sym_gen = iter(symbol)
        while len(star_bar) < banner_width: star_bar += sym_gen.next()
        padding = ' '
        messagef = symbol + padding + s + padding + symbol

        if position == None or position < 0:
            if position == None: position = 0
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

    @classmethod
    def ellipses(cls, msg):
        cls.write(msg)
        for i in range(4):
           time.sleep(.04)
           cls.write('.')



class DialogGui(Shellib):
    
    def __init__(self, *args): 
        "Create main window for graphical application. args[0] is the interface name, e.g., 'zenity'."
        if self.__class__.platform == 'android':
            self.__class__.interface = 'SL4A'
            self.__class__.droid = android.Android()
        else: 
            if len(args) >= 1: self.__class__.interface = args[0] 
            else: self.__class__.interface = ['dialog', 'zenity'][randint(0,1)]
        Cli.clear()
        Cli.ellipses('Starting {} interface.'.format(self.__class__.interface))                                              


    ##################
    # SHARED METHODS #
    ##################
    @classmethod
    def output(cls, msg, heading="Output", width=None, height=None, x=0, y=0):
        if cls.interface == 'dialog':
            if not width: width = 41
            if not height: height = 10
            w, h = width, height
            cls.message(msg, heading, w, h)
        elif cls.interface == "SL4A":
            cls.droid.dialogCreateAlert(title=heading, message=str(msg))
            cls.droid.dialogShow()
            cls.droid.dialogGetResponse()
            cls.droid.dialogDismiss()
        elif cls.interface == "zenity": cls.message(msg, heading)
 
    @classmethod
    def outputf(cls, msg=None, heading="", width=None, height=None, file=None):
        if cls.interface == 'dialog': cls.output(msg, heading, width, height)
        elif cls.interface == 'SL4A':
            print(heading + '\n')
            print(msg + '\n')
        elif cls.interface == "zenity":
            if file: os.system('zenity --text-info --filename={0} --font=mono --text={1} --title={1} --width=800 --height=700'.format(file, heading))
            if not file:

                #translate to python                                                                      
                #os.system('echo "{}" > tmp'.format(msg))
                #use 'with'?
                with open('tmp', 'w') as f:
                    f.write(msg)
                    f.close()

                os.system('zenity --text-info --filename=tmp --font=mono --text={0} --title={0}'.format(heading))

    @classmethod
    def input(cls, prompt ="Enter something:"):
        if cls.interface == "dialog":
            os.system('dialog --title "Inputbox - To take input from you" --backtitle "{}" --inputbox "{}" 8 40 2> tmp'.format(sys.argv[0], prompt))
            s = Cli.cat('tmp', quiet=True, return_str=True)
            os.remove('tmp')
            return s.strip()
        elif cls.interface == "SL4A":
            try:
                response = cls.droid.dialogGetInput("Input", prompt)
                cls.droid.dialogDismiss()
                result = None
                if "which" in response: result = response["which"]
                if result == "negative": raise Exception("Aborted.")
                return response.result
            except "Aborted.": sys.exit()
        elif cls.interface == "zenity":
            cmd = 'zenity --entry --text "{}" --title "Input" > tmp'.format(prompt)
            os.system(cmd)
            s = Cli.cat('tmp', quiet=True, return_str=True)
            os.remove('tmp')
            return s.strip()
        
    @classmethod
    def wait(cls, msg="Continue"):
        if cls.interface in ["dialog"]: os.system('dialog --pause "{}" 10 40 3'.format(msg))
        else: cls.message(msg)

    @classmethod
    def width(cls):
        if cls.interface == "dialog": return Cli.height()
        elif cls.interface == 'zenity': return # Hmmm...

    @classmethod
    def height(cls):
        if cls.interface == "dialog": return Cli.height()
        elif cls.interface == 'zenity': return # Hmmm...

    @classmethod
    def welcome(cls, script_name=sys.argv[0].split('/')[-1].split('.')[0], description='', get_str=False):
        cls.message(description, script_name)

    @classmethod
    def message(cls, msg, heading="", width=40, height=10):
        if cls.interface in ["dialog"]: os.system('dialog --title "{}" --clear --msgbox "{}" {} {}'.format(heading, msg, height, width))
        elif cls.interface in ["SL4A"]:
            cls.droid.dialogCreateAlert(title=heading, message=str(msg))
            cls.droid.dialogSetPositiveButtonText('OK')
            cls.droid.dialogShow()
            cls.droid.dialogGetResponse()
            cls.droid.dialogDismiss()
        elif cls.interface in ["zenity"]:
            command = 'zenity --info --text="{}" --title="{}"'.format(msg, heading) # --width={} --height={}'.format(msg, heading, width, height)
            os.system("{}".format(command))

    @classmethod
    def list_menu(cls, list_obj, p="Make a selection:", t="Menu Widget"):
        if cls.interface in ['dialog']:
            list_str = ""
            for index, item in enumerate(list_obj.items):
                list_str += '{} "{}" '.format(index + 1, item)
                if index == 0: list_str += "on "
                else: list_str += "off "
            cmd_str = 'dialog --radiolist "{}" 25 30 {} {}2> tmp'.format(p, len(list_obj), list_str)
            os.system(cmd_str)
            s = Cli.cat('tmp', quiet=True, return_str=True)

            #this is an error?      
            try: return int(s)
            except: print("cmd_str: " + cmd_str)

        elif cls.interface in ["SL4A"]: return cls.radioButtonDialog(list_obj.label, list_obj.items)
        elif cls.interface in ["zenity"]:
            cmd = 'zenity --list --text="View list:" --column="{0}" --title="{0}" --height=300 --hide-header'.format(list_obj.label)
            for item in list_obj: cmd += ' "{}"'.format(item)
            ans_str = subprocess.check_output("bash -c '{}'".format(cmd), shell=True)
            number = list_obj.items.index(ans_str.decode('utf-8').split('|')[0].strip()) + 1
            return number

    @classmethod
    def SavePrompt(cls, filename, dir_name):
        if cls.interface == 'SL4A':
            cls.droid.dialogCreateAlert(message="Save as {}'{}'?".format(dir_name, filename))
            cls.droid.dialogSetPositiveButtonText('Yes')
            cls.droid.dialogSetNegativeButtonText('No')
            cls.droid.dialogShow()
            response = cls.droid.dialogGetResponse().result
            cls.droid.dialogDismiss()
            print("response = '{}'".format(response))
        else: Cli.SavePrompt(filename, dir_name)

    @classmethod
    def radioButtonDialog(cls, question, options):
        cls.droid.dialogCreateAlert(question)
        cls.droid.dialogSetSingleChoiceItems(options)
        cls.droid.dialogSetPositiveButtonText("OK")
        cls.droid.dialogSetNegativeButtonText("Cancel")
        cls.droid.dialogShow()
        response = cls.droid.dialogGetResponse().result
        if "which" in response: result = response["which"]
        if result == "negative": raise Exception("Aborted.")
        selectedItems = cls.droid.dialogGetSelectedItems().result
        cls.droid.dialogDismiss()
        return (selectedItems.pop() + 1)

    @classmethod
    def notify(cls, msg, **kwargs):
        if cls.interface in ["SL4A"]: cls.droid.makeToast(msg)
        elif cls.interface in ["zenity"]: os.system('zenity --notification --text "{}"'.format(msg))



class WindowedApp(Shellib):    
    '''
    This is a base class for my shell classes.  It does nothing on its own.
    '''
    def __init__(self, shell): 

        """Create main window for graphical application."""
        self.__class__.interface = shell                     
        self.declare_main_window()
        #self.create_menu()
        self.add_message_widget()

    @classmethod
    def declare_main_window(cls):#, width=500, height=25, x=0, y=400):
        return sys.argv[0].split('/')[-1].split('.')[0]

    ##################
    # SHARED METHODS #
    ##################
    @classmethod
    def wait(cls, msg="Continue"):
        cls.message(msg)

    @classmethod
    def welcome(cls, script_name=sys.argv[0].split('/')[-1].split('.')[0], description='', get_str=False):
        cls.message(description, script_name)

    @staticmethod
    def notify(msg):
        os.system('zenity --notification --timeout=1 --text "{}"'.format(msg))




class wx_Template(WindowedApp):

    def __init__(self):
        global wx
        try: import wx
        except: sys.exit("Could not import module 'wx'.")
        super(wx_Template, self).__init__('wx')

    @classmethod
    def declare_main_window(cls, width=500, height=25, x=0, y=400):
        mod_name = super(wx_Template, cls).declare_main_window()
        cls.app = wx.App()
        cls.main_window = wx.Frame(None, -1, mod_name)
        height = 25
        cls.centerWindow(w=width, h=height, x_offset=x, y_offset=y)        
        cls.main_window.Show()

    @classmethod
    def add_message_widget(cls): return

    @classmethod
    def create_menu(cls):
        cls.mainmenu = wx.MenuBar()
        cls.__create_exit_menu()
        cls.__create_language_menu()
        cls.main_window.SetMenuBar(cls.mainmenu)

    @classmethod   
    def __create_exit_menu(cls):
        cls.quit_menu = wx.Menu()
        qitem = cls.quit_menu.Append(wx.ID_EXIT, 'Quit', 'Quit program')
        cls.mainmenu.Append(cls.quit_menu, '&File')
        cls.main_window.Bind(wx.EVT_MENU, cls.__onQuit, qitem)

    @classmethod
    def __create_language_menu(cls):
        cls.languagemenu = wx.Menu()
        litems = []
        litems.append(cls.languagemenu.Append(wx.NewId(), 'English (en)', kind=wx.ITEM_RADIO))
        litems.append(cls.languagemenu.Append(wx.NewId(), 'Esperanto (eo)', kind=wx.ITEM_RADIO))
        cls.mainmenu.Append(cls.languagemenu, '&Language')

    @classmethod
    def __onQuit(cls, event):
        cls.main_window.Close()

    @classmethod
    def start_app(cls):
        cls.app.MainLoop()

    @classmethod
    def centerWindow(cls, w=400, h=0, x_offset=0, y_offset=200, win=None):
        if not win: win = cls.main_window
        win.Centre()
        win.SetSize((w, h))
        win.Move((y_offset, x_offset))      


class Tk_Template(WindowedApp):

    def __init__(self):
        global tkMessageBox, tkinter 
        try:
            import tkMessageBox
            import Tkinter as tkinter
        except:
            try:
                from tkinter import messagebox as tkMessageBox
                import tkinter
            except: sys.exit("Could not import module 'tkinter'.")
        super(Tk_Template, self).__init__('Tk')

    @classmethod
    def declare_main_window(cls, width=200, height=100, x=0, y=0):#, x=100, y=150):
        mod_name = super(Tk_Template, cls).declare_main_window()
        cls.main_window = tkinter.Tk()
        cls.main_window.wm_title(mod_name)
        #cls.main_window.call('wm', 'iconbitmap', cls.main_window._w, '../trees.xbm')
        #cls.main_window.wm_iconbitmap(bitmap='../trees.xbm')
        #if not height: height = 0
        cls.centerWindow(w=width, h=height, x_offset=x, y_offset=y)        

    @classmethod
    def add_message_widget(cls):
        cls.msgtxt = tkinter.StringVar()
        cls.msg = tkinter.Message(cls.main_window, textvariable=cls.msgtxt)
        cls.msg.pack(pady=10)

    @classmethod
    def create_menu(cls):
        cls.mainmenu = tkinter.Menu(cls.main_window, tearoff=0)
        cls.__create_exit_menu()
        cls.__create_language_menu()
        cls.main_window.config(menu=cls.mainmenu)

    @classmethod   
    def __create_exit_menu(cls):
        cls.filemenu = tkinter.Menu(cls.mainmenu, tearoff=0)
        cls.filemenu.add_command(label="Quit", command=cls.main_window.destroy)
        cls.mainmenu.add_cascade(label="File", menu=cls.filemenu)

    @classmethod
    def __create_language_menu(cls):
        cls.languagemenu = tkinter.Menu(cls.mainmenu, tearoff=0)
        cls.languagemenu.add_command(label="English (en)") 
        cls.languagemenu.add_command(label="Esperanto (eo)")
        cls.mainmenu.add_cascade(label="Language", menu=cls.languagemenu) 

    @classmethod
    def output(cls, msg, *args, **kwargs):
        #cls.centerWindow(h=100, w=150)
        cls.msgtxt.set(msg)
        cls.main_window.mainloop() #probably not good that this is here?

    @classmethod
    def popup(cls, msg, heading="Output", width=None, height=None, x=None, y=None):
        if not width: width = 200
        if not height: height = 90
        if not x: x = 0
        if not y: y = 0 
        d = TkDialog(cls.main_window, msg, heading, width, height)
        cls.centerWindow(w=width, h=height, x_offset=x, y_offset=y, win=d.top)
        cls.main_window.wait_window(d.top)
        #d.top.grab_set()                                                                            
        #d.focus_set()

    @classmethod
    def outputf(cls, msg=None, heading="", width=None, height=None, x_offset=0, y_offset=0, file=None):
        '''
        make the 'file' attribute work
        '''
        cls.output(msg, heading, width, height, x=x_offset, y=y_offset)

    #@classmethod
    #def notify(cls, msg, **kwargs):
    #    msg = msg.strip('"')

    #@classmethod
    #def notify(cls, msg):
    #    super(Tk_Template, cls).notify(msg)

    @classmethod
    def input(cls, prompt ="Enter something:"):
        d = TkInput(cls.main_window, prompt)
        cls.main_window.wait_window(d.top)
        s = d.val
        return s.strip()        

    @classmethod
    def width(cls):
        return cls.main_window.winfo_screenwidth()

    @classmethod
    def height(cls):
        return cls.main_window.winfo_screenheight()

    @classmethod
    def welcome(cls, script_name=sys.argv[0].split('/')[-1].split('.')[0], description='', get_str=False):
        cls.message(description, script_name)

    @classmethod
    def message(cls, msg, heading="", width=40, height=10):
        msg = msg.strip('"')
        tkMessageBox.showinfo(heading, msg)

    @classmethod
    def list_menu(cls, list_obj, p="Make a selection:", t="Menu Widget"):
        d = TkList(cls.main_window, list_obj, p, t)
        cls.main_window.wait_window(d.top)
        return d.val[0] + 1

    @classmethod
    def centerWindow(cls, w=200, h=100, x_offset=0, y_offset=200, win=None):
        if not win: win = cls.main_window
        #if w==None: w = 400
        #if h==None: h = 0
        #if x_offset==None: x_offset = 0
        #if y_offset==None: y_offset = 200

        sw = win.winfo_screenwidth()
        sh = win.winfo_screenheight()
        x = (sw - w) // 2 - x_offset
        y = (sh - h) // 2 - y_offset
        win.geometry('{}x{}+{}+{}'.format(w, h, x, y))


class Thing(object):
    '''
    Parent class for most classes in this package; 
    provides str 'label' and class int 'count' 
    Contains methods for saving as txt or pickle, and opening from pickle.
    '''
    count = 0
    
    def __init__(self):
        '''
        increments instance counter "count" and sets a default label.
        '''
        self.__class__.count += 1
        self.label = self.__default_label()
        #sys.stderr.write(" :: One <{}> object created, {}. :: \n".format(self.__class__.__name__, cli_lib.emph(self.label)))
        #time.sleep(.1)

        self.f = None

    def __default_label(self):
        '''
        Generates a generic label
        '''
        return "{} #{}".format(self.__class__.__name__.lower(), self.__class__.count)

    def __repr__(self):
        '''
        returns a str '[[ self.label ]]'
        '''
        return Cli.emph(self.label)

    def ul_label(self, w=None, p=None): 
        '''
        NEEDS IMPROVEMENT
        Gives label--underlined with '=' signs--as a string
        '''
        if not w: w = 2 + len(self.label)
        if not p: return Cli.ul(self.label.capitalize(), width=w)
        else: return Cli.ul(self.label.capitalize(), width=w, position=p)

    def __eq__(self, other):
        try: return (self.label == other.label)
        except AttributeError: return (self.label == other)

    def __ne__(self, other):
        return not (self == other)

    def _save(self, BASENAME, ext, save_func, sh_class=Cli):
        FILENAME = BASENAME + '.' + ext
        dir_name = Cli.pwd(getstr=True)
        if dir_name != '/': dir_name += '/'

        # See if exists

        # Confirm filename             
        try: FILENAME = sh_class.SavePrompt(FILENAME, dir_name)
        except KeyboardInterrupt: return
        f = open(FILENAME, 'wb+')
        save_func(f)
        f.close()
        sh_class.report_filesave(FILENAME)


    def write_txt(self, BASENAME, sh_class=Cli):
        '''
        Cast object as str and write to a txt file.
        '''
        if sys.version_info.major == 3:
            self._save(BASENAME, 'txt', lambda f:f.write(bytes(str(self) + '\n', 'UTF-8')), sh_class)
        elif sys.version_info.major == 2:
            self._save(BASENAME, 'txt', lambda f:f.write(str(self) + '\n'), sh_class)


    def save_p_file(self, BASENAME):
        '''
        Save instance as a pickle.  (Use Shell.open_p_file() to open.)
        '''
        self._save(BASENAME, 'p', lambda f:pickle.dump(self, f))


#######################
## LIST-type CLASSES ##
#######################
class AbstractList(Thing):
    def __init__(self, items, heading=None):
         super(AbstractList, self).__init__()
         if heading:
             self.show_heading = True 
             self.label = heading
         else: self.show_heading = False
         self.items = items

    def __str__(self):
        '''Prints either '[Empty List]' or nothing.'''
        s = ""
        if len(self) == 0: s += " [Empty List]\n"
        return s

    def __len__(self):
        return len(self.items)

    def __getitem__(self, index):
        return self.items[index]

    def sort(self):
        self.items.sort()

    def sorted(self):
        return self.items.sorted()


class PlainList(AbstractList):
    def __str__(self):
        s = '\n'
#        if len(self.label) > 0: s += self.label.upper() + ":"                  
        if self.show_heading: s += self.label.upper() + ":"
        s += super(PlainList, self).__str__()
        if len(self) > 0: s += str(self.items)
        return s


class VerticalList(AbstractList):
    def __str__(self, indent=0):
        s = ""
#        if len(self.label) > 0:
        if self.show_heading:
            s += self.ul_label(p=indent)
        else: s += '\n'
        s += super(VerticalList, self).__str__()
        return s + '\n'


class ItemList(VerticalList):
    def __str__(self):
        #if Terminal.mobile: bullet = '°'
        #if Shellib.interface == 'SL4A': bullet = '•'
        #else: bullet = '∙'
        bullet = '•'
        s = super(ItemList, self).__str__(1)
        if len(self) > 0:
            for i in range(len(self)):
                s += "  {} {}\n".format(bullet, self[i])
        return s


class Enumeration(VerticalList):
    def __str__(self):
        '''maybe this can be united with its parent method somehow'''
        s = super(Enumeration, self).__str__(0)
        if len(self) > 0:
             for i in range(len(self)):
                 s += "{:>2}. {}\n".format((i + 1), self[i])
        return s


class ListPrompt(Enumeration):
    def __init__(self, l, **kwargs):
        #self.mode = mode
        super(ListPrompt, self).__init__(l, "")
        if len(l) > 0:
            self.label = "Make a choice (1-{})".format(len(self))

    def input(self, prompt='>', hidden=False):
        #if self.mode == 'gui':
        #    try:
        #        result = Widget.radioButtonDialog("Menu", self.items)
        #        message = self.items[result - 1]
        #    except Exception:
        #        result = None
        #        message = "No answer"
        #    #Widget.Notification(message)
        #    return result
        #else:
        if len(self) > 10: 
            long = True
            prompt = 'Type a number and press [ENTER]: '
        if hidden == False:
            self.show_heading = True 
            print(self)
        else: 
            sys.stdout.write(self.label)
            sys.stdout.flush()
        if len(self) > 0:
            try:
                if long: sel_str = Cli.input(prompt)
                else: sel_str = Cli.get_keypress(prompt)
                if sel_str.isdigit(): sel = int(sel_str)
                else: sel = None
            except KeyboardInterrupt:
                print('')
                return None
            except: sel = None

            while sel == None or sel > len(self) or sel < 1 :
                try:
                    if (sel == None or sel < 1) and len(self) > 0 and len(self) < 10:
                        sel_str = Cli.get_keypress(prompt)
                    else: 
                        sel_str = Cli.input(prompt)
                    if sel_str.isdigit(): sel = int(sel_str)
                    else: sel = None
                except KeyboardInterrupt:
                    print('')
                    return None
                #except: pass
            return sel
        else: return None
            



######################                                                                                    
## Tk-BASED CLASSES ##                                                                                    
######################                                                                                    
class TkDialog:
    def __init__(self, parent, msg, heading="Dialog Widget", width=200, height=90):
        self.top = tkinter.Toplevel(parent)
        self.top.title(heading)
        Tk_Template.centerWindow(w=width, h=height, win=self.top)
        tkinter.Label(self.top, text=msg).pack(pady=10)
        b = tkinter.Button(self.top, text="OK", command=self.ok)
        b.pack(padx=5)
        b.focus_set()
        b.grab_set()

    def ok(self):
        self.top.destroy()


class TkInput():
    def __init__(self, parent, msg="Input", width=200, height=80):
        top = self.top = tkinter.Toplevel(parent)
        top.title("Input Widget")
        Tk_Template.centerWindow(win=top, w=width, h=height, x_offset=0, y_offset=-30)
        tkinter.Label(top, text=msg).pack()
        self.e = tkinter.Entry(top)
        self.e.pack()
        self.e.focus_set()
        b = tkinter.Button(top, text="OK", command=self.ok)
        b.pack(pady=5)

    def ok(self):
        self.val = self.e.get()
        self.top.destroy()
        return self.val


class TkList:
    def __init__(self, parent, list_obj, prompt="Make a selection:", title='Menu Widget'):
        msg = list_obj.label
        li = list_obj.items[::-1]
        top = self.top = tkinter.Toplevel(parent)
        top.title(title)
        Tk_Template.centerWindow(win=top, x_offset=0, h=250, w=200, y_offset=100)                                            
        tkinter.Label(top, text=prompt).pack()
        self.listb = tkinter.Listbox(top)
        self.listb.focus_set()
        for item in li:
            self.listb.insert(0,item)
        b = tkinter.Button(top, text="OK", command=self.ok)
        self.listb.select_set(0)
        self.listb.pack()
        b.pack(pady=5)

    def ok(self):
        self.val = self.listb.curselection()
        self.top.destroy()

'''                                                                                                       
class TkFrame(Frame):                                                                                     
    def __init__(self, parent):                                                                           
        Frame.__init__(self, parent) #, background="black")                                               
                                                                                                          
        self.parent = parent                                                                              
        #self.parent.title("Centered window")                                                             
        self.pack(fill=BOTH, expand=1)                                                                    
        self.centerWindow()                                                                               
                                                                                                          
    def centerWindow(self):                                                                               
        w = 290                                                                                           
        h = 150                                                                                           
                                                                                                          
        sw = self.parent.winfo_screenwidth()                                                              
        sh = self.parent.winfo_screenheight()                                                             
                                                                                                          
        x = (sw - w)/2                                                                                    
        y = (sh - h)/2                                                                                    
        self.parent.geometry('%dx%d+%d+%d' % (w, h, x, y))                                                
'''
