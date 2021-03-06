#!usr/bin/env python
#coding=utf-8

import os
import pickle
import sys

__author__ = 'Chris Horn'
__license__ = 'GPL'


class Thing(object):
    """
    Parent class for most classes in this package;
    provides str 'label' and class int 'count'
    Contains methods for saving as txt or pickle.
    """

    count = 0

    def __init__(self):
        """
        increments instance counter "count" and sets a default label.
        """
        self.__class__.count += 1
        self.label = self.__default_label()

    def __repr__(self):
        """
        returns a str 'self.label'
        """
        return self.label

    def __eq__(self, other):
        """How should this work?  What should it do?"""
        try:
            return self.label == other.label
        except AttributeError:
            return self.label == other

    def __ne__(self, other):
        return not self == other

    def __default_label(self):
        """
        Generates a generic label
        """
        return '{} #{}'.format(
            self.__class__.__name__.lower(), self.__class__.count)

    def _save(self, basename, ext, save_func, sh_class=None):
        """
        Open the file, perform the appropriate save action and close the file.
        """
        if sh_class is None:
            try:
                sh_class = self.sh_obj
            except AttributeError:
                sys.exit('Error in cjh.shell.Shellib object.')
                #sh_class = Cli()# <-----this is a problem!
        filename = basename + '.' + ext
        dir_name = os.getcwd()  # Fileman.pwd(getstr=True)
        if dir_name != '/':
            dir_name += '/'

        # See if exists

        if sh_class.interface != 'Tk':

            # Confirm filename

            try:
                filename = sh_class.save_prompt(filename, dir_name)
            except KeyboardInterrupt:
                return

        handler = open(filename, 'w')
        save_func(handler)
        handler.close()
        sh_class.report_filesave(filename)

    def write_txt(self, basename, sh_class=None):
        """
        Cast object as str and write to a txt file.
        """
        if sys.version_info.major == 3:
            self._save(
                basename, 'txt', lambda f: f.write(bytes(str(self) + '\n',
                'UTF-8')), sh_class)
        elif sys.version_info.major == 2:
            self._save(
                basename, 'txt', lambda f: f.write(str(self) + '\n'), sh_class)

    def save_p_file(self, basename):
        """
        Save instance as a pickle.  (Use Shell.open_p_file() to open.)
        """
        self._save(basename, 'p', lambda f: pickle.dump(self, f))


#    @staticmethod
#    def _ul(text, symbol='=', position=None, width=None):
#        """
#        Return some text, as a str, underlined by some symbol ('=' by default).
#        """
#        text_width = len(text) + 2
#        understroke = (symbol * (text_width // len(symbol)))
#        sym_gen = iter(symbol)
#        while len(understroke) < text_width:
#            understroke += sym_gen.next()
#        if position and position >= 0:
#            indent_pad = ' ' * position
#            understroke = indent_pad + understroke
#            text = indent_pad + text
#        else:
#            if width:
#                screen_width = width
#            elif cls.platform == 'android':
#                screen_width = 36
#            elif cls.interface == 'bash':
#                screen_width = int(subprocess.check_output(
#                    'tput cols', shell=True))
#        else: screen_width = 80
#            if position and position < 0:
#                screen_width += (2 * position)
#            understroke = understroke.center(screen_width)
#            text = text.strip()
#            text = text.center(screen_width)
#            text = text[1:-1]
#        return "\n  {}\n {}".format(text, understroke)


#    def ul_label(self, width_=None, pos=None):
#        """
#        Gives label--underlined with '=' signs--as a string
#        """
#        if width_ is None:
#            width_ = 2 + len(self.label)
#        if pos is None:
#            return self._ul(self.label.capitalize(), width=width_)
#        else: return self._ul(
#                self.label.capitalize(), width=width_, position=pos)
