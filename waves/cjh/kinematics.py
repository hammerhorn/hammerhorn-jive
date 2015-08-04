#!/usr/bin/env python
#coding=UTF-8
"""
Perform addition with vectors, displacements, and velocities.
"""
import decimal, math, sys

from cjh.angles import Angle
from cjh.letterator import Letter
from cjh.scalars import Scalar, Unit

__author__ = 'Chris Horn <hammerhorn@gmail.com>'
__license__ = 'GPL'

SPEED_OF_LIGHT = 3e8

class Vector(Scalar):
    """
    Plain vector
    """
    letter_seq = Letter.caps_gen()

    def _resolve(self):
        """
        Break vector down into X and Y components.
        """
        #print 'resolving {}'.format(self.theta)
        #print 'which is {} in radians'.format(self.theta.radians)
        #print "self.theta is type {}".format(type(self.theta))

        x_mag = decimal.Decimal(self.mag) * decimal.Decimal(math.cos(
            self.theta.radians))
        y_mag = decimal.Decimal(self.mag) * decimal.Decimal(math.sin(
            self.theta.radians))
        return x_mag, y_mag

    def __init__(self, mag, th=Angle()):
        super(Vector, self).__init__(mag)
        #if th == None: self.theta = Angle()
        #else:
        self.theta = th
        self.x_mag, self.y_mag = self._resolve()
        self.label = next(self.__class__.letter_seq)

    def __repr__(self):
        return '⟶  {{{}; {}}}'.format(Scalar(self.mag, self.units), self.theta)

    def __str__(self):
        return '{:10,.5g} {} at {}'.format(self.mag, self.units, self.theta)

    def __add__(self, addend):
        x_sum = self.x_mag + addend.x_mag
        y_sum = self.y_mag + addend.y_mag
        try:
            myvector1 = Vector(
                math.sqrt(x_sum ** 2 + y_sum ** 2), Angle(math.atan(
                y_sum / x_sum), 'rad'))
        except (ZeroDivisionError, InvalidOperation) as e:
            return Vector(0, Angle())
        if x_sum < 0.0:
            myvector1.mag *= decimal.Decimal(-1.0)
        if self.theta.units.label == 'degrees':
            myvector1.theta = myvector1.theta.deg()
        return myvector1

    def __mul__(self, mul_end):
        return Vector(self.mag * mul_end, self.theta)

    def __rmul__(self, mul_end):
        return Vector(self.mag * mul_end, self.theta)

    def to_scalar(self):
        """
        Return scalar part (no angle or direction).
        """
        return Scalar(self.mag, self.units)


class Disp(Vector):
    """
    displacement vector
    """
    def __init__(self, mag=0.0, th=Angle(), u='m'):
        super(Disp, self).__init__(mag, th)
        self.label = "disp_{}".format(self.label)
        self.units = Unit(u)

    def __add__(self, addend):
        # if units of Angle are different, change both to degrees
        if self.theta.units != addend.theta.units:
            self.theta = self.theta.degrees()
            addend.theta = addend.theta.degrees()

        # if units of Disp are different, change both to meters
        if self.units != addend.units:
            self = self.meters()
            addend = addend.meters()

        # if self.theta.units == addend.theta.units and :
        x_sum = self.x_mag + addend.x_mag
        y_sum = self.y_mag + addend.y_mag

        try:
            myvector1 = Disp(math.sqrt(x_sum ** 2 + y_sum ** 2), th=Angle(
                math.atan(y_sum / x_sum), 'rad'), u=self.units.abbrev)
        except ZeroDivisionError:
            return Disp(0.0, self.units.abbrev, Angle(90))

        if x_sum < decimal.Decimal(0.0):
            myvector1.mag *= decimal.Decimal(-1.0)
        if self.theta.units.label == 'degrees':
            myvector1.theta = myvector1.theta.deg()
        return myvector1

    def __div__(self, divisor):
        pass

    def __mul__(self, mul_end):
        """This will need to be improved"""
        return Disp(self.mag * mul_end, self.theta, self.units.abbrev)


    def __mul__(self, mul_end):
        return Vector(self.mag * mul_end, self.theta)

    def __rmul__(self, mul_end):
        """This will need to be improved"""
        return Disp(self.mag * mul_end, self.units.abbrev, self.theta)

    def meters(self):
        """
        returns Disp object in meters
        """
        if self.units.label == 'feet':
            return Disp(.3048 * self.mag, 'm', self.theta)
        elif self.units.label == 'meters':
            return self
        elif self.units.label == 'inches' or\
            self.units.label == 'miles':
            return (self.feet()).meters()
        elif self.units.label == 'centimeters':
            return Disp(self.mag / 100.0, 'm', self.theta)
        else:
            sys.exit("Sorry, I don't know how to convert from {}.".format(
                self.units.label))

    def feet(self):
        if self.units.label == 'meters':
            return Disp(self.mag / .3048, 'ft.', self.theta)
        elif self.units.label == 'feet':
            return self
        elif self.units.label == 'inches':
            return Disp(self.mag / 12.0, 'ft.', self.theta)
        elif self.units.label == 'miles':
            return Disp(self.mag * 5280.0, 'ft.', self.theta)
        else:
            sys.exit("Sorry, I don't know how to convert from {}.".format(\
                self.units.label))


    def inches(self):
        inches = self.feet() * 12
        inches.units = Unit('in.')
        return inches

    def miles(self):
        return Disp(self.feet().mag / 5280.0, 'mi.', self.theta)


class Velocity(Vector):
    def __init__(self, mag=0.0, u='m/s', th=Angle(0.0, 'deg')):
        super(Velocity, self).__init__(mag, th)
        self.units = Unit(u)
        if (self.mps()).mag > SPEED_OF_LIGHT:
            self.mag = SPEED_OF_LIGHT
            self.units = Unit('m/s')

    def __add__(self, addend):
        sum_ = Velocity((self.mps().mag + addend.mps().mag) / (
            1 + self.mps().mag * addend.mps().mag / (
            SPEED_OF_LIGHT)**2), 'm/s')
        if self.units.abbrev == 'mph':
            sum_ = sum_.mph()
        return sum_

    def __mul__(self, other):
        total = Velocity()
        for _ in range(other):
            total += self
        return total

    def mph(self):
        if self.units.abbrev == 'mph':
            return self
        elif self.units.abbrev == 'm/s':
            return Velocity(self.mag * 2.2369363, 'mph', self.theta)
        else:
            sys.exit("Sorry, I don't know how to convert from {}.".format(
                self.units.label))

    def mps(self):
        if self.units.abbrev == 'm/s':
            return self
        elif self.units.abbrev == 'mph':
            return Velocity(self.mag / 2.2369363, 'm/s', self.theta)
        else: sys.exit("Sorry, I don't know how to convert from {}.".format(
                self.units.label))
                
