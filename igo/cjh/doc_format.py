#!/usr/bin/env python
#coding=UTF-8
import textwrap

from cjh import cli
from cjh.things import Thing

__author__ = 'Chris Horn <hammerhorn@gmail.com>'
__license__ = 'GPL'

class Paragraph(Thing):

    ## CLASS VARIABLES ##
    invisibles = False
    no_indent = False
    cli.Cli()

    ## METHODS ##
    def __init__(
        self, text_str, width=int(round(cli.Cli.width() * .9)), no_indent=False):
        self.__class__.no_indent = no_indent
        super(Paragraph, self).__init__()
        self.width = width
        text_str = textwrap.dedent(text_str).strip()
        self.buffer = text_str
        self.set_lmargin()

    def __add__(self, other):
        return Section(p_list=[self, other])

    def __str__(self):
        lines2 = list(self.word_wrap)
        pstr = '\n'
        if self.__class__.invisibles == True:
            pstr += '¶'
        else: pstr += ' '
        pstr += ' ' * (self.lmargin - 1) + lines2[0] + '\n'
        for index in range(1, len(lines2)):
            pstr += ' ' * self.lmargin + lines2[index] + '\n'
        return pstr

    def __mul__(self, multi):
        plist = []
        for _ in range(multi):
            plist.append(self)
        return Section(p_list=plist)

    def __getitem__(self, index):
        '''
        list() or [] will give you a list of sentences
        '''
        buf = ''
        for line in self.naive_wrap:
            buf += line
        ls = buf.split('.')
        ls = [sentence.lstrip('_ ') + '.' for sentence in ls]
        return ls[index]

    def __len__(self):
        ''' number of sentences '''
        tmp = []
        count = 0
        while True:
            try:
                count += 1
                tmp.append(self.__getitem__(count))
            except IndexError:
                break
        return len(tmp)

    def set_lmargin(self, fill=4):
        self.lmargin = fill

    def cat(self, para2):
        tmp_str1 = ""
        tmp_str2 = ""
        noindent = True
        for line in self.naive_wrap:
            tmp_str1 += line
        if len(tmp_str1) > 0 and tmp_str1[0] == '_':
            noindent = False
            tmp_str1 = tmp_str1.lstrip('_')
        for line in para2.naive_wrap:
            tmp_str2 += line
            tmp_str2 = tmp_str2.lstrip('_')
        return Paragraph(\
            tmp_str1.rstrip() + "  " + tmp_str2, no_indent=noindent)

    @property
    def wc(self):
        return len(self.buffer.split())

    @property
    def naive_wrap(self):
        buf = self.buffer
        lines = []
        line_cnt = len(buf) / self.width + 1
        for _ in range(line_cnt):
            if len(buf) >= self.width:
                lines.append(buf[0:self.width - 1])
                buf = buf[self.width - 1:]
            else: lines.append(buf)
        for index, line in enumerate(lines):
            if index != 0 and line[0] == ' ':
                lines[index] = lines[index].lstrip()
        return lines

    @property
    def word_wrap(self):
        buf = self.buffer
        if self.__class__.no_indent == True:
            i = ''
        else: i = ' ' * 5
        lines = textwrap.fill(\
            buf, width=self.width, initial_indent=i).split('\n')
        return lines

class Section(Thing):
    def __init__(self, hstr='', p_list=[]):
        super(Section, self).__init__()
        if len(hstr) == 0:
            self.heading = "{}.".format(self.__class__.count)
        else: self.heading = hstr
        self.pgraph_list = p_list

    def __getitem__(self, index):
        return self.pgraph_list[index]

    def __add__(self, pgraph):
        #s = Section()
        self.pgraph_list.append(pgraph)
        return self
        #self.plist = self.pgraph_list[:]
        #selfplist.append(pgraph)
        #Section.count -= 1
        #return Section(p_list=plist)

    def __str__(self):
        pstr = ""
        if len(self.pgraph_list) >= 1:
            pstr = " " * (self.pgraph_list[0].lmargin)
        else: pstr = " " * 5
        pstr += self.heading.upper() + "\n"
        pstr += "\n"
        for pgraph in self.pgraph_list:
            pstr += str(pgraph)
        pstr += "\n"
        return pstr + "\n"

#class Pager(Thing):
#    def __init__(self, text):
#        self.screen = Terminal()
#        self.lines = text.split('\n')

#    def __str__(self):
        #if len(self.lines) < self.screen.width():
#        return str(len(self.lines) % self.screen.width())
