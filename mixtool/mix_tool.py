#!/usr/bin/env python
"""
mixture calculator for alcoholic drinks

Calculate how much of 2 different solutions you need to combine to reach
a target %ABV and volume.

 use: MixTool.py $%ABV1 $%ABV2 $TARGET_%ABV $TARGET_VOLUME

If no arguments are given, input is from stdin.  Pretty much a direct
translation of MixTool.pl

* use Decimal class?  rounding?  padding/justification?
"""
import decimal

from cjh.shell import Cli

__author__ = 'Chris Horn <hammerhorn@gmail.com>'

Cli()

# Colon should be included here, instead of in arg method.
PROMPT_LIST = [
    '%ABV of first ingredient',
    '%ABV of second ingredient',
    'Target %ABV',
    'Target volume (fl. oz.)'
]

#abv1 = float(Cli.arg(*PROMPT_LIST))
#abv2 = float(Cli.arg(*PROMPT_LIST))
#target_abv = float(Cli.arg(*PROMPT_LIST))

def main():
    """
    1) Get necessary parameters from the user.
    2) Calculate the mixture.
    3) Output the results.
    """
    abv1 = decimal.Decimal(Cli.arg(*PROMPT_LIST)) #pylint: disable=star-args
    abv2 = decimal.Decimal(Cli.arg(*PROMPT_LIST)) #pylint: disable=star-args
    target_abv = decimal.Decimal(Cli.arg(*PROMPT_LIST)) #pylint: disable=star-args

    # If it is possible to create a mixture according to the provided
    # parameters,
    # find and output the answer.
    if (target_abv >= abv1 or target_abv >= abv2) and (
            target_abv <= abv1 or target_abv <= abv2):
        target_vol = decimal.Decimal(Cli.arg(*PROMPT_LIST)) #pylint: disable=star-args

        vol1 = target_vol * (target_abv - abv2) / (abv1 - abv2)
        vol2 = target_vol - vol1
        print(
'\nYou will need {:4.3} fl. oz. of the first ingredient ({}% ABV), and'.format(
            vol1, abv1))
        print(
'\t      {:4.3} fl. oz. of the second ingredient ({}% ABV).\n'.format(
            vol2, abv2))

    # Otherwise, apologize to the illogical user.
    else: print("Sorry, that's not possible.") #pylint: disable=C0325

if __name__ == '__main__':
    main()
