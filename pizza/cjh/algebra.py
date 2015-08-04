#!/usr/bin/env python
"""
Classes for monomial and polynomial arithmetic and evaluation.
(* Output options like LaTeX, HTML?)
"""
import decimal, traceback

from cjh import cli
from cjh.letterator import Letter
from cjh.lists import PlainList
from cjh.scalars import Minusable
from cjh.things import Thing

__author__ = 'Chris Horn <hammerhorn@gmail.com>'
__license__ = 'GPL'

class Term(Thing, Minusable):
    """
    Term is a monomial expression of form coef(x)^exp.
    """

    def __init__(self, coef=0.0, exp=0.0):
        super(Term, self).__init__()
        self.coef = decimal.Decimal(coef)
        self.exp = decimal.Decimal(exp)

    def __repr__(self):
        string = ""
        if self.coef != 1.0 or self.exp == 0.0:
            if self.coef == -1.0:
                string += '-'
                if self.exp == 0:
                    string += '1'
            else: string += '{:g}'.format(self.coef)
        if self.coef != 0.0 and self.exp != 0.0:
            string += 'x'
            if self.exp != 1.0:
                string += '^{:g}'.format(float(self.exp))
        return string

    def __abs__(self):
        return Term(abs(self.coef), self.exp)

    def __add__(self, other):
        term_list = [self, other]
        try:
            return Polynom(term_list)
        except AttributeError:
            return Polynom([self, Term(other, 0)])

    def __radd__(self, other):
        return self + other

    def __mul__(self, other):
        try:
            product = Term((self.coef * other.coef), (self.exp + other.exp))
        except AttributeError:
            product = Term((self.coef * decimal.Decimal(other)), (self.exp))
        return product

    def __div__(self, other):
        try:
            quotient = Term((self.coef / other.coef), (self.exp - other.exp))
        except AttributeError:
            quotient = Term((self.coef / other), (self.exp))
        return quotient

    def __pow__(self, other):
        return Term(
            self.coef ** decimal.Decimal(other), self.exp * decimal.Decimal(
            other))

    def __eq__(self, other):
        try:                   # if other is a Term
            if self.coef == other.coef and self.exp == other.exp:
                value = True
            else: value = False
        except AttributeError: # if other is a float
            if self.coef == other and self.exp == 1:
                value = True
            else: value = False
        return value

    def __gt__(self, other):
        if (self.exp > other.exp or
            self.exp == other.exp and self.coef > other.coef):
            return True
        else: return False

    def __ge__(self, other):
        if self > other or self == other:
            return True
        else: return False

    def __lt__(self, other):
        if self < other:
            return True
        else: return False

    def __le__(self, other):
        if self <= other:
            return True
        else: return False

    def __call__(self, x_val):
        """
        self(x) == self.eval(x)
        """
        return round(self.eval(x_val), 4)

    def eval(self, x_val):
        """
        self.eval(x) == self.__call__(x)
        """
        if self.exp == 0:
            return self.coef
        else: return self.coef * decimal.Decimal(x_val) ** self.exp


class Polynom(Thing, Minusable):
    """
    Polynom is a polynomial, composed of the sum of monomial Terms.
    """

    letter_maker = Letter.lower_gen(start_letter='f')

    def __init__(self, term_list=[Term()]):
        """
        term_list is of type Term[]
        """
        super(Polynom, self).__init__()
        self.dict = {}
        self.list_ = []

        for term in term_list:
            exp = term.exp

            # add to dictionary
            if exp in self.dict.keys():
                self.dict[exp] += term.coef
            else: self.dict[exp] = term.coef

        try:
            exps = self.dict.keys()
            exps.sort()
            exps = exps[::-1]

            for exp in exps:
                self.list_.append(Term(self.dict[exp], exp))
        except KeyError:
            pass
        self.letter = next(self.__class__.letter_maker)

    def __repr__(self):
        string = '{}(x) = '.format(self.letter)
        if len(self) == 0  or (len(self) == 1 and self.list_[0].coef == 0.0):
            string += '0'
        else:
            string += str(self.list_[0])
            for item in range(1, len(self)):
                if self.list_[item].coef > 0:
                    string += ' + {}'.format(self.list_[item])
                else:
                    string += ' - {}'.format(abs(self.list_[item]))
        return string

    def __add__(self, other):
        sum_ = Polynom(self.list_)

        # Create dictionary representing sum
        # if addend is Polynom
        try:
            for term in other.list_:
                if term.exp in sum_.dict.keys():
                    sum_.dict[term.exp] += term.coef
                else: sum_.dict[term.exp] = other.coef #?
        except AttributeError:

            # if addend is Term
            try:
                if other.exp in sum_.dict.keys():
                    sum_.dict[other.exp] += other.coef
                else: sum_.dict[other.exp] = other.coef
            except AttributeError:

                # otherwise, addend is int or float
                if 0 in sum_.dict.keys():
                    sum_.dict[0] += decimal.Decimal(other)
                    sum_.dict[0] = round(sum_.dict[0], 4)
                else: sum_.dict[0] = other

        # Convert dict of numbers to list of Terms
        sum_.list_ = []
        for exp in range(int(max(sum_.dict.keys())), -1, -1):
            try:
                if sum_.dict[exp] == 0.0:
                    del sum_.dict[exp]
                else: sum_.list_.append(Term(sum_.dict[exp], exp))
            except KeyError:
                pass
        return sum_

    def __radd__(self, other):
        return self + other

    def __mul__(self, other):
        poly = Polynom()

        # if other is a number
        # use of float here might result in loss of precision
        poly.dict = {coef_:(decimal.Decimal(other) * self.dict[coef_])
            for coef_ in self.dict.keys()}

        # Convert dict of numbers to list of Terms
        poly.list_ = []
        for exp in range(int(max(poly.dict.keys())), -1, -1):
            try:
                if poly.dict[exp] == 0.0:
                    del poly.dict[exp]
                else: poly.list_.append(Term(poly.dict[exp], exp))
            except KeyError:
#               print(traceback.format_exc()) #pylint: disable=C0325
                pass
        return poly

    def __pow__(self, other):
        poly = Polynom()
        # if other is a number
        poly.dict = {(coef_ * other):self.dict[coef_]\
            for coef_ in self.dict.keys()}

        # Convert dict of numbers to list of Terms
        poly.list_ = []
        for exp in range(int(max(poly.dict.keys())), -1, -1):
            try:
                if poly.dict[exp] == 0.0:
                    del poly.dict[exp]
                else: poly.list_.append(Term(poly.dict[exp], exp))
            except KeyError:
                print(traceback.format_exc()) #pylint: disable=C0325
        return poly

    def __iter__(self):
        """
        Returns a listiterator object of Terms contained.
        """
        return iter(self.list_)

    def __len__(self):
        #perhaps length of f(x) = 0 should be 0
        list_ = [term for term in self.list_ if term.coef != 0.0]
        return len(list_)

    def __getitem__(self, power):
        """
        The index is the exponent.  Returns a zero if there is nothing
        in that "slot".
        """
        try:
            value = float(self.dict[power])
        except KeyError:
            value = 0.0
        return value
        #return self.list_[power]

    def wizard(self, page_txt_obj=None, sh_class=cli.Cli):
        """
        Interactively populates the Polynomial.
        """
        self.list_ = []
        menu2 = PlainList(['add monomial term', 'DONE'])
        menu2.label = 'Polynomial Wizard'
        while True:
            sel2 = cli.Cli.make_page(
                'Polynomial', page_txt_obj, lambda: sh_class.list_menu(menu2))
            if sel2 == 1:

                # Add monomial term
                print('') #pylint: disable=C0325
                coef_str = ''
                while len(coef_str) == 0:
                    coef_str = sh_class.input('coefficient?')
                coef = float(coef_str)
                pow_str = ''
                while len(pow_str) == 0:
                    pow_str = sh_class.input('power?')
                pow_ = float(pow_str)
                self.list_.append(Term(coef, pow_))
                menu2.label = str(self)
                self.dict.clear()
                for index in range(len(self)):
                    exponent = self.list_[index].exp
                    if exponent in self.dict.keys():
                        self.dict[exponent] += self.list_[index].coef
                    else: self.dict[exponent] = self.list_[index].coef
            elif sel2 == 2:
                break

    def eval(self, x_val):
        """
        Evaluate the Polynom for a particular value.
        """
        sum1 = decimal.Decimal(0.0)
        for index in range(len(self)):
            sum1 += self.list_[index].eval(x_val)
        return sum1

    def __call__(self, x_val):
        """
        Rounded version of self.eval()
        """
        return round(self.eval(x_val), 4)
