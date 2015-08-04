#!/usr/bin/python
#coding=utf-8
import os, sys

from cjh.cli import Cli
from cjh.doc_format import Paragraph, Section
from cjh.things import Thing

class LatexObj(Thing):
    def import_file(self, filename):
        def read_file_lines():
            """
            Read in lines from file.
            """

            def file_error():
                """
                If no regular file exists, print an error message and exit.
                """
                current_dir = os.getcwd()
                if filename in ['.', '..', '/'] or filename in os.listdir(
                    current_dir):
                    error = '{}: {}: Is a directory'
                else:
                    error = '{}: {}: No such file or directory'
                    sys.exit(error.format(sys.argv[0], filename))

            try:
                f = open(filename)
                self.lines = f.readlines()
                f.close()
            except IOError:
                file_error()

        def strip_whitespace():
            """
            Get rid of whitespace on the left and right.
            """
            for line in self.lines:
                self.lines[self.lines.index(line)] = line.strip()

        def strip_comments():
            """
            Remove comments, i.e., lines starting with '%'
            """
            line_count = len(self.lines)
            lines_to_delete = []

            for indx in range(line_count):
                if len(self.lines[indx]) > 0 and self.lines[indx][0] == '%':
                    lines_to_delete.append(indx)
            for i in lines_to_delete:
                del self.lines[i]
                for l in range(1, len(lines_to_delete)):
                    lines_to_delete[l] -= 1

        read_file_lines()
        strip_whitespace()
        strip_comments()

    def __init__(self, file_, margin=10):

        def _initialize_fields():
            self.margin = margin
            self.width = Cli.width() - margin * 2
            self.tabpoints = margin, self.width
            self.author = None
            self.title = None
            self.date = ''
            self.buffer = ''
            self.lines = []
            self.pgraph_no = 0
            self.section_no = 0
            self.p_list = []
            self.s_list = []

        super(LatexObj, self).__init__()
        _initialize_fields()
        self.import_file(file_)
        self.scan_lines()

    def make_title(self):
        """
        Print a nice title page.
        """
        if self.title:
            s = ''
            s += ('\n' * (Cli.height() / 2 - 2))
            s += (('__' + self.title + '__').replace(' ', '_').center(
                Cli.width()))
            if self.author:
                s += '\n\n' + 'by'.center(
                Cli.width()) + '\n\n' + self.author.center(Cli.width())
            s += ('\n' * (Cli.height() / 2 - 2))
            s += ('-' * Cli.width())
            if self.section_no == 0:
                s += ('\n' * 4)
            return s
        else: return '[No title]'

    def print_toc(self):
        """
        Create a table of contents and print to the screen.
        """
        s = ""
        any_visible = False
        for x in range(len(self.s_list)):
            if self.s_list[x].heading[0].isdigit()\
                and self.s_list[x].heading[0] != '0':
                any_visible = True
        if any_visible == True:
            s += ''
            s += "CONTENTS".center(Cli.width())
            s += ''

            for section in self.s_list:
                if section.heading[0].isdigit() and section.heading[0] != '0':
                    s += section.heading.center(Cli.width())
                s += '\n'
            s += ((('-' * (Cli.width() / 2)).center(Cli.width()) + '\n') * 1)
            s += ('\n')
            s += ((('-' * (Cli.width() / 2)).center(Cli.width()) + '\n') * 1)
            s += ('\n')
        return s

    def print_sections(self):
        s = ''
        s += ('\n' * int(self.tabpoints[0]/3.0)) #top margin == left margin / 3
        if len(self.s_list) >= 1 and len(self.s_list[0].pgraph_list) > 0:
            s += str(self.s_list[0])
        for x in range(1, len(self.s_list)):
            s += str(self.s_list[x])
        return s

    def __str__(self):
        s = ''
        s += self.make_title()
        s += self.print_toc()
        s += self.print_sections()
        return s

    def store_paragraph(self, no_indent):
        """
        Use contents of 'buffer' to construct a new Paragraph object,
        and we clear 'buffer' to read in the next paragraph of text.
        """
	#print "begin store_paragraph()"
        self.pgraph_no += 1
        if len(self.buffer) > 0:
            self.easy_subs()

            #self.strip_unknown_tags()

            paragraph = Paragraph(self.buffer, self.tabpoints[1], no_indent)
            paragraph.set_lmargin(self.tabpoints[0])
            #print "add to section"
            self.s_list[len(self.s_list) - 1] += paragraph
            self.buffer = ""
	#print "end store_paragraph()"

    def easy_subs(self):
        """
        reimplement using a dictionary
        """
        self.buffer = self.buffer.replace('\\\\', '\n')
        self.buffer = self.buffer.replace(r'\dots', '(...)')
        self.buffer = self.buffer.replace("\\'a", 'á')
        self.buffer = self.buffer.replace("\\'i", 'í')
        self.buffer = self.buffer.replace('---', '—')
        self.buffer = self.buffer.replace('--', '–')
        self.buffer = self.buffer.replace("``", '“')
        self.buffer = self.buffer.replace("''", '”')
        self.buffer = self.buffer.replace("'", '’')
        self.buffer = self.buffer.replace('`', '‘')
        self.buffer = self.buffer.replace('\\^C', 'Ĉ')
        self.buffer = self.buffer.replace('\\^c', 'ĉ')
        self.buffer = self.buffer.replace('\\^G', 'Ĝ')
        self.buffer = self.buffer.replace('\\^g', 'ĝ')
        self.buffer = self.buffer.replace('\\^H', 'Ĥ')
        self.buffer = self.buffer.replace('\\^h', 'ĥ')
        self.buffer = self.buffer.replace('\\^J', 'Ĵ')
        self.buffer = self.buffer.replace('\\^j', 'ĵ')
        self.buffer = self.buffer.replace('\\^S', 'Ŝ')
        self.buffer = self.buffer.replace('\\^s', 'ŝ')
        self.buffer = self.buffer.replace('\\u{u}', 'ŭ')

    def strip_unknown_tags(self):
        """
        If an unknown tag is detected in 'buffer', attempt to remove it
        gracefully.
        """
        while(self.buffer.find('\\') >= 0) and self.buffer[self.buffer.find(
            '\\') + 2] != '\n':
            if (self.buffer.find('section') == self.buffer.find('\\') + 1) or \
                (self.buffer.find('title') == self.buffer.find('\\') + 1) or \
                len(self.buffer[self.buffer.find('\\'):
                self.buffer.find('}') + 1]) == 0:
                break
            self.buffer = self.buffer[:self.buffer.find('\\')] +\
                self.buffer[self.buffer.find('}') + 2:]

    def open_new_section(self, h=''):
        """
        Create a new section, and reset 'pgraph_no'
        """
        self.pgraph_no = 0
        self.s_list.append(Section(h))

    def parse_section_tag(self, line):
        """
        Append a new empty Section, and process heading number.
        """
        #print "begin parse_section_tag()"
        if line.find(r'\section{') >= 0:
            self.section_no += 1
            self.open_new_section(str(self.section_no) + '. ' + line[(line.find(
                r'\section{') + 9):(line.find('}'))])
        elif line.find(r'\section*{') >= 0:
            self.open_new_section(line[(line.find(r'\section*{') + 10):(
                line.find('}'))])
        else: sys.exit('Error in string ' + r'\section')
        line = line[(line.find('}') + 1):]

    def scan_lines(self):
        """
        Scan each line in 'lines'
        """
        #print "begin scan_lines()"
        for line in self.lines:
           #print 'begin loop: "{}"'.format(line)

	   #if line not empty
            if line != '' and line != '\n':
               #get title
                if line.find('\\title') >= 0:
                    self.title = line[(line.find('{') + 1):(line.find('}'))]

                elif line.find('\\author') >= 0:
                    self.author = line[(line.find('{') + 1):(line.find('}'))]

               # If '\section' tag is detected, create a new section and add an
#entry to the table of contents.
                elif line.find(r'\section') >= 0:
                    self.parse_section_tag(line)

                elif line.find(r'\hrule') >= 0:
                    self.buffer = '-' * Cli.width()
                    self.store_paragraph(True)

               # If the current line is  not empty, append it to the buffer.
                else:
                    if len(self.s_list) == 0 and len(line) != 0:
                        Section.count = -1
                        self.open_new_section() # Introduction")
		       #print "section=0"

                    self.buffer += (line + ' ')

           # If it's a blank line, we store the Paragraph and prepare to read in
#a  new one.
           #    strip_unknown_tags()
            else: self.store_paragraph(False)



##def process_text():
##    global lines
##    global section_no
##    global line_no
##    global screen
##    if lines[line_no].find('\textbf{') >= 0:
##        section_no += 1
##        screen.bold_write(lines[line_no][(lines[line_no].find('\{') + 8):(
#lines[line_no].find('}'))])
##    elif lines[line_no].find('\section*{') >= 0:
##        open_new_section(lines[line_no][(lines[line_no].find('\section*{') +
#10):(lines[line_no].find('}'))])
##    else:
##        sys.exit("Error in string " + "\section")
##    lines[line_no] = lines[line_no][(lines[line_no].find("}") + 1):]
