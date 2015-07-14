#!/usr/bin/env python
"""
Calculate the area and unit price of a circular pizza.
"""
import argparse
import decimal

from cjh.cli import Cli
from cjh.config import Config
from cjh.geometry import Circle
from cjh.kinematics import Disp
from cjh.scalars import Unit

__author__ = 'Chris Horn <hammerhorn@gmail.com>'
__license__ = 'GPL'


##################
##  PROCEDURES  ##
##################
def _parse_args():
    """
    Parse arguments.
    """
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        '-m', '--metric', help='use centimeters instead of inches',
        action='store_true')
    parser.add_argument(
        '-d', '--diameter', type=float, help='diameter; inches by default')
    parser.add_argument(
        '-p', '--price', type=float,
        help='price in dollars for one whole pizza')
    parser.add_argument('--nox', action='store_true')
    parser.add_argument('-s', '--shell', type=str)
    if __name__ == '__main__':
        args = parser.parse_args()
    else:
        args = None
    return args


def print_welcome():
    """
    if neither diameter nor price are known, print description
    Docstring is duplicated because android is not detecting it properly.
    """
    if ARGS is None or ARGS.diameter is None and ARGS.price is None:

        greeting = """
        Calculate the area and unit price of a circular pizza."""
        SHELL.welcome('Pizza Price Tool', greeting)


def set_linear_units():
    """
    Gets unit abbrev from command line or stdin and returns as a str.
    """
    if ARGS is not None and ARGS.metric is True:
        abbrev = 'cm'
    else:
        abbrev = 'in.'
    return abbrev


def set_diameter(abbrev):
    """
    Gets diameter from args or stdin and return as a <cjh.kinematics.Disp>.
    """
    if ARGS is not None and ARGS.diameter is not None:
        diameter = decimal.Decimal(ARGS.diameter)
    else:
        if ARGS is not None and ARGS.metric is True:
            prompt = 'centimeters'
        else:
            prompt = 'inches'
        print('')  # pylint: disable=C0325
        diameter = decimal.Decimal(SHELL.input('{}? '.format(prompt)))
    diameter = Disp(diameter, u=abbrev)
    return diameter


def make_circle(diameter):
    """
    Takes <cjh.kinematics.Disp> diameter as argument, returns
    <cjh.geometry.Circle> circle
    """
    radius = diameter.mag / decimal.Decimal(2.0)
    pizza = Circle(radius)
    return pizza


def _set_area_units(pizza):
    """
    Takes 1 arg <cjh.geometry.Circle>, returns type <cjh.geometry.Circle>
    """
    if ARGS is not None and ARGS.metric is True:
        pizza.area.units = Unit('cm^2')
    else:
        pizza.area.units = Unit('sq. in.')
    return pizza


def set_price():
    """
    Gets price from command line or stdin
    """
    if ARGS is not None and ARGS.price is not None:
        price = decimal.Decimal(ARGS.price)
    else:
        price = decimal.Decimal(SHELL.input('price? $'))
    return price


def output_results(pizza, price):
    """
    Output area and unit price
    """
    results = 'Area of the pizza is {}\n'.format(pizza.area)
    results += 'The unit price of the pizza is ${}/{}'.format(
        round(price / pizza.area.mag, 2), pizza.area.units.abbrev)
    if SHELL.interface in ['zenity']:
        results = results.replace('$', r'\$')
    SHELL.message(results)
    print('')

############
##  DATA  ##
############
ARGS = _parse_args()
CONFIG = Config()
if ARGS is not None and ARGS.nox is True:
    SHELL = Cli()
elif ARGS is not None and ARGS.shell is not None:
    SHELL = CONFIG.launch_selected_shell(ARGS.shell)
else:
    SHELL = CONFIG.start_user_profile()
ABBREV = set_linear_units()


############
##  MAIN  ##
############
def main():
    """
    Print welcome message then get pizza size and price and output area
    and unit price.
    """
    Cli.print_header()
    print_welcome()

    while True:
        diameter = set_diameter(ABBREV)
        pizza = make_circle(diameter)
        pizza = _set_area_units(pizza)
        price = set_price()
        output_results(pizza, price)

if __name__ == '__main__':
    main()
