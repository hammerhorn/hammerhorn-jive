#!/usr/bin/env python

import decimal, math, sys  # , timeit

# Make command-line arguemtns work
try:
    import numpy
    numpy_available = True
except ImportError:
    numpy_available = False

def numpy_method():
    global num_list, total1, numpy_available
    if numpy_available is not True:
        total1 = 'Not available.'
    else:
        total1 = numpy.array(num_list, float).sum()
    
def math_method():
    global num_list, total2
    total2 = math.fsum(num_list)

def native_method():
    global num_list, total3
    total3 = sum(num_list)

input_str = sys.stdin.read().strip()
str_list = input_str.split()
num_list = [decimal.Decimal(i) for i in str_list]

print('')

numpy_method()
print("numpy: {}".format(total1))

math_method()
print('math.fsum(): {}'.format(total2))

native_method()
print('sum(): {}'.format(total3))
