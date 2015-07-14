#!/usr/bin/python
#coding=UTF-8
"""
Helps workers predict what their net pay will be.
"""
__author__ = 'Chris Horn <hammerhorn@gmail.com>'

import argparse, datetime, sys, time

from cjh.budget import PayPeriod, WorkWeek
from cjh.shell import Cli, PlainList


def _parse_args():
    """
    Parse arguments.
    """
    def setup_template():
        """
        Prepare data structures.
        """
        global paycheck
        if args.input_file:
            paycheck = PayPeriod()
            try:
                paycheck = PayPeriod.open_p_file(args.input_file)
                Cli.print_header(paycheck.est_net_pay())
                print_title()
                print(paycheck) #pylint: disable=C0325
                time.sleep(2)
            except IOError:
                sys.exit('Failed to load {}.'.format(args.input_file))
            startdate = paycheck.start_date

        # if no input file and no start date, exit program
        elif not args.start_date:
            sys.exit(
                '\nusage: pay_calc.py [-h] [-i INFILE|-s START] [-w WAGE]\
                [-p PERCENT]\n')

        # if there is a startdate but no infile, then parse startdate
        else:
            startdate_array = args.start_date.split('/')

            # initialize pay_period object
            startdate = datetime.date(
                int(startdate_array[2]), int(startdate_array[0]),
                int(startdate_array[1]))
            if args.percent:
                p = float(args.percent)
            elif args.input_file:
                pass
            else: p = PayPeriod.withholding_wizard()
            paycheck = PayPeriod(startdate, percent=p)

            if args.wage:
                paycheck.wage = float(args.wage)

    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--input_file', type=str, help='load file')
    parser.add_argument(
        '-s', '--start_date', type=str, help='date pay period starts')
    parser.add_argument('-w', '--wage', type=float, help='dollars per hour')
    parser.add_argument('-p', '--percent', type=float, help='percent withheld')
    args = parser.parse_args()
    Cli.default_splash('== pay calc ==', 2014)
    setup_template()
    return args

def print_title(title='PAYCHECK CALCULATOR'):
    """
    Print title.
    """
    Cli.print_header()
    print('') #pylint: disable=C0325
    print(title.center(Cli.width())) #pylint: disable=C0325
    print(('=' * 25).center(Cli.width())) #pylint: disable=C0325


def view_pay_period():
    """
    View pay period.
    """
    print(paycheck) #pylint: disable=C0325
    Cli.wait()


def input_shifts():
    """
    Input shifts.
    """
    print_title('  {} — {}'.format(
        paycheck.start_date, paycheck.start_date + datetime.timedelta(14)))
    startdate = paycheck.start_date
    for i in range(14):
        day_number = (startdate.weekday() + i) % 7
        day_str = WorkWeek.weekday_name(day_number)
        print('{}/{} ({})'.format((startdate + datetime.timedelta(i)).month, (
            startdate + datetime.timedelta(i)).day, day_str))
        str1 = (paycheck.shift_dict.get(datetime.date((
            startdate + datetime.timedelta(i)).year, (
            startdate + datetime.timedelta(i)).month, (
            startdate + datetime.timedelta(i)).day)))
        if str1:
            print(str1) #pylint: disable=C0325
        try:
            paycheck.add_shift((startdate + datetime.timedelta(i)).month, (
                startdate + datetime.timedelta(i)).day)
            print_title('  {} — {}'.format(
                paycheck.start_date, paycheck.start_date + datetime.timedelta(
                14)))
            print(paycheck) #pylint: disable=C0325
        except ValueError:
            continue
        except KeyboardInterrupt:
            break
        finally:
            print('') #pylint: disable=C0325

def save_state():
    """
    Save paycheck as a pickle and json.
    """
    paycheck.save_p_file(str(paycheck.start_date))
    #paycheck.save_as_pickle(str(paycheck.start_date) + ".p")
    #paycheck.save_as_json(str(paycheck.start_date) + ".json")

def estimate_paycheck():
    if not(ARGS.percent) and paycheck.percent == None:
        sub_menu = PlainList(['continue', 'withholding wizard'])
        sel1 = SHELL.list_menu(sub_menu)
        if sel1 == 2:
            PayPeriod.withholding_wizard()
    Cli.print_header(paycheck.est_net_pay())

    # Use Cli.money()?
    print('Gross pay: $%.3g' % (paycheck.gross_pay())) #pylint: disable=C0325
    print('  Net pay: $%.3g' % (paycheck.est_net_pay())) #pylint: disable=C0325
    SHELL.wait()

#def withholding_wizard():
#    Terminal.print_header()
#    print("Withholdings Wizard")
#    print('-' * 30)
#    print('Please enter the following fields from a recent pay stub.')
#    gross = float(input('Gross pay: $'))
#    net   = float(input('  Net pay: $'))
#    paycheck.percent = 100.0 * (1.00 - net / gross)
#    print("Percent withheld: %.3g%%" % (paycheck.percent))
#    Terminal.wait()


##############
# Start Here #
##############

#percent_withheld = 33.333 # Use 'withhoding wizard' to change.

SHELL = Cli()
if __name__ == '__main__':
    ARGS = _parse_args()
    print_title(
        '  {} — {}'.format(
        paycheck.start_date, paycheck.start_date + datetime.timedelta(14)))

# Main Menu
MAIN_MENU = PlainList(['view pay period',
                        'input shifts',
                        'estimate paycheck amount',
                        '(add shift)',
                        '(edit/remove shift)',
                        'save',
                        'load pay period'])


#############
# Main Loop #
#############
if __name__ == '__main__':
    while True:
        #try:
        sel = SHELL.list_menu(MAIN_MENU)
        #sel = main_menu.input()
        print_title(
            '  {} — {}'.format(
            paycheck.start_date, paycheck.start_date + datetime.timedelta(14)))
        if sel == 1:
            view_pay_period()
        elif sel == 2:
            input_shifts()
        elif sel == 3:
            estimate_paycheck()
        elif sel == 6:
            save_state()
        elif sel == 7:
            filename = SHELL.input('file name: ')
            paycheck = PayPeriod.open_p_file(filename)
        elif sel in [4, 5]:
            print('feature not yet implemented\n') #pylint: disable=C0325
            time.sleep(1)
        else: break
        print_title(
            '  {} — {}'.format(
            paycheck.start_date, paycheck.start_date + datetime.timedelta(14)))
        #except KeyboardInterrupt: break
