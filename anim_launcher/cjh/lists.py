#!/usr/bin/env python
#coding=utf-8
import abc

from cjh.things import Thing


class AbstractList(Thing):
    """
    Abstract parent for all list-type objects in this package.
    * This should be modified to inherit from the native Python list.
    """
    __metaclass__ = abc.ABCMeta

    def __init__(self, items, heading=None):
        super(AbstractList, self).__init__()
        if heading:
            self.show_heading = True
            self.label = heading
        else:
            self.show_heading = False
        self.items = items

    @abc.abstractmethod
    def __str__(self):
        """
        Prints either '[Empty List]' or nothing.
        """
        string = ''
        if len(self) == 0:
            string += ' [Empty List]\n'
        return string

    def __len__(self):
        return len(self.items)

    def __getitem__(self, index):
        return self.items[index]

    def sort(self):
        """
        Sort items in place.
        """
        self.items.sort()

    def sorted(self):
        """
        Returns a sorted copy.
        """
        return sorted(self.items)


class PlainList(AbstractList):
    """
    is displayed like a normal list type (e.g., [1, 2, 3, 4]), but inherits
    attributes 'count', 'heading', et al....
    """

    def __init__(self, items, heading=None):
        super(PlainList, self).__init__(items)

    def __str__(self):
        string = '\n'
        if self.show_heading:
            string += self.label.upper() + ':'
        string += super(PlainList, self).__str__()
        if len(self) > 0:
            string += str(self.items)
        return string


class VerticalList(AbstractList):
    """
    Abstract parent class for ItemList and Enumeration.

    *Perhaps an indention mechanism should be worked out.
    """

    def __init__(self, items, heading=None):
        super(VerticalList, self).__init__(items)

    def __str__(self):
        string = ""
        if self.show_heading:
                string += self.label
                string += '\n' + '=' * len(self.label) + '\n'
                string += super(VerticalList, self).__str__()
        return string + '\n'


class ItemList(VerticalList):
    """
    Bulleted VerticalList.
    """
    def __init__(self, items, heading=None):
        super(ItemList, self).__init__(items)

    def __str__(self):
        bullet = '•'
        string = ' ' + super(ItemList, self).__str__()
        if len(self) > 0:
            for index in range(len(self)):
                string += '  {} {}\n'.format(bullet, self[index])
        return string


class Enumeration(VerticalList):
    """
    Numbered VerticalList.
    """
    def __init__(self, items, heading=None):
        super(Enumeration, self).__init__(items)

    def __str__(self):
        """
        *maybe this can be united with its parent method somehow
        """
        string = super(Enumeration, self).__str__()
        if len(self) > 0:
            for num in range(len(self)):
                string += '{:>2}. {}\n'.format((num + 1), self[num])
        return string
