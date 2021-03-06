#!/usr/bin/env python
"""
Contains class for simulating die-rolls.
"""
import time
from random import randint

from cjh import cli
from cjh.things import Thing

__author__ = 'Chris Horn <hammerhorn@gmail.com>'
__license__ = 'GPL'

class Die(Thing):
    """
    For simulated die-rolls.  "Sidedness" of die can be specified.
    """

    def __init__(self, sides=6):
        super(Die, self).__init__()
        self.face = []
        self.sides = sides
        self.label = '(d{})'.format(self.sides)
        self.value = randint(1, self.sides)
        self.clear_face()

    def __call__(self):
        """
        prints diagram to screen and returns the value
        """
        self.roll()
        if self.sides <= 6:
            print('') #pylint: disable=C0325
            self.clear_face()
            self.generate_face()
            self.draw_face()
        else: print(self.value) #pylint: disable=C0325
        return self.value

    def __str__(self):
        return self.label + ' ' + str(self.value)

    def __len__(self):
        return self.sides

    def __eq__(self, other):
        if type(other) == type(self):
            if self.value == other.value:
                return True
            else: return False
        elif type(other) == int:
            if self.value == other:
                return True
            else: return False
        else: return None

    def __gt__(self, other):
        if self.value > other.value:
            return True
        else: return False
        
#   def __add__(self, ):
#       sum_die = Die()
#       sum_die.value = self.value + other.value

#    def __iter__(self):
#        return self
#    def next()

    def clear_face(self):
        self.face = [' ----- ',
                     '|     |',
                     '|     |',
                     '|     |',
                     ' ----- ']

    def roll(self):
        self.value = randint(1, self.sides)

    def generate_face(self):
        self.clear_face()
        if   self.value == 1:
            self.face[2] = '|  *  |'
        elif self.value == 2:
            self.face[1] = '|    *|'
            self.face[3] = '|*    |'
        elif self.value == 3:
            self.face[1] = '|    *|'
            self.face[2] = '|  *  |'
            self.face[3] = '|*    |'
        elif self.value == 4:
            self.face[1] = '|*   *|'
            self.face[3] = '|*   *|'
        elif self.value == 5:
            self.face[1] = '|*   *|'
            self.face[2] = '|  *  |'
            self.face[3] = '|*   *|'
        elif self.value == 6:
            self.face[1] = '|*   *|'
            self.face[2] = '|*   *|'
            self.face[3] = '|*   *|'

    def draw_face(self, get_str=False, verbose=False, shellib=cli.Cli):
        self.generate_face()
        if verbose:
            string = str(self) + '\n'
        else: string = ""
        for index in range(5):
            string += self.face[index] + '\n'
        if get_str:
            return string
        else:
            if verbose:
                head = ' '
            else: head = self.label
        if shellib.interface == 'Tk':
            shellib.msg.config(font=('mono', 9, 'normal'))
        shellib.outputf(string, heading=head)

    def animate(self):
        tdelta = .08

        for _ in range(4):
            cli.Cli.print_header()

            self.roll()
            print('') #pylint: disable=C0325
            self.draw_face()

            time.sleep(tdelta)

            cli.Cli.print_header()
            time.sleep(tdelta)

        cli.Cli.print_header()
        return self()
