#!/usr/bin/env python
#coding=UTF-8
"""
Unit & Scalar classes
"""
import abc
import copy
import decimal
import json

from cjh.cli import Cli
from cjh.dialog_gui import DialogGui
from cjh.things import Thing

__author__ = 'Chris Horn <hammerhorn@gmail.com>'
__license__ = 'GPL'


def read_json_file(filename):
    file_ptr = open(filename, 'rb')
    buffer_ = file_ptr.read().decode('utf-8')
    return json.loads(buffer_)


class Unit(Thing):
    """
    Takes care of all "heavy lifting" needed for working with units
    """

    unit_dict = read_json_file('units.json')

    def __init__(self, short_name="units"):
        """
        I tried doing this as a list iterator, but the compiler kept
        thinking label was an object rather than a string, so I now
        implement it as a while loop with a try block.  Meh...ugly and
        overly-complex
        """
        super(Unit, self).__init__()
        not_done = True
        while not_done:
            try:
                self.label = self.__class__.unit_dict[short_name]
                not_done = False
            except KeyError:
                print("'{}' not found in list: {}".format(
                    short_name, Unit.unit_dict.keys()))
                long_name = Cli().input(
                    "What does '{}' stand for? ".format(short_name))
                Unit.unit_dict.update({short_name: long_name})
        self.abbrev = short_name

    def __repr__(self):
        if (len(self.abbrev) == 0) or ((self.label) == (self.abbrev)):
            return self.label
        else:
            return '{} ({})'.format(self.label, self.abbrev)

    def __len__(self):
        return len(self.label)

    def __call__(self, val):
        return Scalar(val, self)

    @property
    def name(self):
        """set unit name"""
        return self.label

    @name.setter
    def name(self, name):
        """
        currently takes long or short name;
        this might be a problem in the future
        """
        vals = list(self.unit_dict.values())
        if name in self.unit_dict:
            self.label = self.unit_dict[name]
            self.abbrev = name
        elif name in vals:
            self.label = name
            self.abbrev = list(self.unit_dict.keys())[vals.index(name)]


class Minusable(object):
    """
    Provides generic negativity, subtraction for any class in which '*'
    is defined.
    """

    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def __init__():
        pass

    def __neg__(self):
        return self * -1

    def __sub__(self, other):
        return self + -other


class Scalar(Thing, Minusable):
    """
    A float, 'self.mag', paired with Unit object 'self.units'
    """
    def __init__(self, d=0.0, unit_abbrev='units'):
        """
        Perhaps not as robust as it should be.
        """
        super(Scalar, self).__init__()
        self.mag = decimal.Decimal(d)

        # If it's a str, no problem....
        if type(unit_abbrev) == str:
            self.units = Unit(unit_abbrev)

        # Otherwise, hope its a Unit object.
        else:
            self.units = unit_abbrev

    def __repr__(self):
        return '{} {}'.format(round(self.mag, 9), self.units.abbrev)

    def __abs__(self):
        new_obj = copy.deepcopy(self)
        new_obj.mag = abs(new_obj.mag)
        return new_obj

    def __add__(self, other):
        if self.check_units(other):
            new_obj = copy.deepcopy(self)
            new_obj.mag += other.mag
            return new_obj

    def __mul__(self, number):
        new_obj = copy.deepcopy(self)
        new_obj.mag *= decimal.Decimal(number)
        return new_obj

    def __rmul__(self, number):
        return self * number

    def __div__(self, other):
        new_obj = copy.deepcopy(self)
        try:
            new_obj.mag /= decimal.Decimal(other)
            return new_obj
        except TypeError:
            if self.check_units(other):
                new_obj.mag /= other.mag
                return new_obj.mag

    def __pow__(self, exp):
        new_obj = copy.deepcopy(self)
        new_obj.mag **= decimal.Decimal(exp)
        return new_obj

    def __eq__(self, other):
        if self.check_units(other):
            if self.mag == other.mag:
                return True
            else:
                return False

    def __gt__(self, other):
        if self.check_units(other):
            if self.mag > other.mag:
                return True
            else:
                return False

    def __ge__(self, other):
        if self.check_units(other):
            if self.mag >= other.mag:
                return True
            else:
                return False

    def __lt__(self, other):
        if self.check_units(other):
            if self.mag < other.mag:
                return True
            else:
                return False

    def __le__(self, other):
        if self.check_units(other):
            if self.mag <= other.mag:
                return True
            else:
                return False

    def check_units(self, other):
        """This needs fixed."""
        if not self.units == other.units:
            title = 'UnitsError'
            message = 'class Scalar can only compare Scalars with like units'
            if Cli.interface == 'SL4A':
                DialogGui.message(message, heading=title)
            else:
                print(title + ': ' + message)
        else:
            return True
