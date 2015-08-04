#!/usr/bin/python

import itertools
import random
#import sys


class ShufXRange(object):
    def __init__(self, *args):
        if len(args) == 1:
            self.min = 0
            self.max = args[0]
        else:
            self.min = args[0]
            self.max = args[1]

        self.int_tuple = tuple(range(self.min, self.max))
        self.shuffle()
        self.row_cycle = iter(self)

    def __len__(self):
        return len(self.int_tuple)

    def __getitem__(self, index):
        return self.int_tuple[index]

    # def __list__(self):
    #     return self.int_list

    def __iter__(self):
        return itertools.cycle(list(self.int_tuple))

        #return self.int_list
    #def __iter__(self):
    #    return iter(self.int_list)
#
    #def __next__(self):
    #    return next(self.row_cycle)
#
    #def next(self):
    #    #int_list = list(self.int_tuple)
    #    if not int_list:
    #        raise StopIteration
    #    return int_list.pop(0)
#
    #def __next__(self):
    #    for n in iter(self):
    #        yield n
#
     #def __iter__(self):
     #    for n in iter(self.int_list):
     #        yield n

    def __str__(self):
        result = ''
        for i in self.int_tuple:
            result += str(i)
            if i <= len(self):
                result += ' '
        return result

    #def __next__(self):
    #    while True:
    #        yield next(iter(int_list))
        # except StopIteration:

    def shuffle(self):
        last_index = self.max - 1
        int_list = list(self.int_tuple)
        for i in range(last_index):
            last_index = last_index - i
            j = random.randint(0, i + 1)
            int_list[i], int_list[j] = int_list[j], int_list[i]
        self.int_tuple = tuple(int_list)
        return self


class ShufRange(object):
    def __init__(self, min, max):
        self.shuf_obj = ShufXRange(min, max)
        self.iterer = iter(self.shuf_obj)

    def __str__(self):
        return str(self.shuf_obj)

    def __iter__(self):
        return self.iterer
