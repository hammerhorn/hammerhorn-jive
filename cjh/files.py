#!/usr/bin/python

import glob, os

from cjh.cli import Cli, ListPrompt
from cjh.lists import ItemList

class Fileman(object):
    @classmethod
    def pwd(cls, getstr=False):
        """
        Emulate 'pwd' command
        """
        string = os.getcwd()
        if getstr:
            return string
        else: print(string)

    @classmethod
    def mc(cls):
        list_prompt = ListPrompt(['..'] + cls.ls(opts=['B'], get_list=True))
        if len(list_prompt) > Cli.height():
            Cli.less(str(list_prompt))
        response = Cli.make_page(header=cls.pwd(getstr=True), func=list_prompt.input)
        if response == 1:
            os.chdir(list_prompt[response - 1])
            cls.mc()
        elif list_prompt[response - 1].endswith('/'):
            os.chdir(list_prompt[response - 1][:-1])
            cls.mc()
        else: return list_prompt[response - 1]

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
                Cli.less(string)
            else: Cli.write(string.strip())
        else:
            return dir_list + file_list
