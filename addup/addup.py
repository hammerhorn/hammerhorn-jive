#!/usr/bin/env python
"""
Sum of a list

Find the sum of a user-input list of numbers.  It would be good to time
each subroutine to see which is the fastest.
"""
import decimal
import math
import sys

try:
    import numpy
    NUMPY_AVAILABLE = True
except ImportError:
    NUMPY_AVAILABLE = False


def numpy_method(nlist):
    """
    Find sum using the numpy module.
    """
    if NUMPY_AVAILABLE is not True:
        total = 'Not available.'
    else:
        total = numpy.array(nlist, float).sum()
    print("numpy: {}".format(total))  # pylint: disable=C0325


def math_method(nlist):
    """
    Calculate using the math module from the standard library.
    """
    total = math.fsum(nlist)
    print('math.fsum(): {}'.format(total))  # pylint: disable=C0325


def native_method(nlist):
    """
    Calculate using the native sum() function.
    """
    total = sum(nlist)
    print('sum(): {}'.format(total))  # pylint: disable=C0325


def main():
    """
    Get a list a numbers from the user, and sum them up three ways.
    """
    input_str = sys.stdin.read().strip()
    str_list = input_str.split()
    num_list = [decimal.Decimal(i) for i in str_list]
    print('')  # pylint: disable=C0325

    # Find the sum.
    numpy_method(num_list)
    math_method(num_list)
    native_method(num_list)

if __name__ == '__main__':
    main()
