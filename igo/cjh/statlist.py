#!/usr/bin/env python

import collections
import numpy as np

import cjh.cli as cli

__author__ = 'Chris Horn'
__license__ = 'GPL'

class StatList(object):
    """
    A list of values on which you can perform: mean, median, mode,
    use [indices], and print an ascii histogram.  Mode and index
    should work with a list that includes strings, but the other
    functions all require a numerical value.
    """

    def __init__(self, list_=[]):
        self.items = np.array(list_)
        self.items.sort()

    def __getitem__(self, index):
        return self.items[index]

    def __len__(self):
        return self.items.size

    def __max__(self):
        return max(self.items)

    def __min__(self):
        return min(self.items)

    @property
    def mean(self):
        return self.items.mean()

    @property
    def median(self):
        self.items.sort()
        if self.items.size % 2 == 1:
            return self.items[(self.items.size - 1) // 2]
        else:
            middle_two = StatList(
                self.items[(self.items.size // 2 - 1):
				    (self.items.size // 2 + 1)])
            return middle_two.mean

    @property
    def mode(self):
        return collections.Counter(self.items).most_common(1)[0][0]

    #@property
    #def mode(self):
    #    """
    #    Not sure if this is mathematically 'correct'
    #
    #    but it is a workalike to qalc
    #    """
    #    hi_count = 1
    #    candidate = self[0]
    #    for index in range(len(self)):
    #        if self.items.count(self[index]) > hi_count:
    #            hi_count = self.items.count(self[index])
    #            candidate = self[index]
    #    return candidate

    def histogram(self):
        print('') #pylint: disable=C0325
        cli.write('%3s:' % self.items[0])
        for i in range(len(self)):
            cli.write('[*]')
            #try:
            if self[i] != self[i + 1]:
                cli.write('\n%3s:' % self[i + 1])
            #except:
            #    pass
        print('\n') #pylint: disable=C0325
