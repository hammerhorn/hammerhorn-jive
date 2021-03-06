#!/usr/bin/env python
#coding=UTF-8
import decimal

from cjh.kinematics import Disp, Velocity
from cjh.scalars import Scalar, Unit
from cjh.things import Thing

__author__ = 'Chris Horn <hammerhorn@gmail.com>'
__license__ = 'GPL'

SPEED_OF_LIGHT = 3e8
SPEED_OF_SOUND = 343.0  # Depends on factors like temperature, et al,
                        # if you want to complicate things.

class Wave(Thing):

    def __init__(self, spd, freq):
        super(Wave, self).__init__()
        self.freq = Scalar(freq, Unit('Hz'))
        self.speed = Velocity(spd)
        self.wlength = Disp(
            (decimal.Decimal(self.speed.mag) / decimal.Decimal(self.freq.mag)))

    def __str__(self):
        return '{}{{ c={}; f={}; λ={} }}\n'.format(self.label,\
            self.speed.to_scalar(), self.freq, self.wlength.to_scalar())


class SoundWave(Wave):

    def __init__(self, f):
        super(SoundWave, self).__init__(SPEED_OF_SOUND, f)


class EMWave(Wave):

    def __init__(self, f):
        super(EMWave, self).__init__(SPEED_OF_LIGHT, f)
        self.label = self.emr_type()

    def emr_type(self):
        """
        returns a string describing the type of radiation
        """
        wavelength = self.wlength.meters().mag
        if wavelength < 3.0e-7:
            return 'x-ray/gamma ray'
        elif wavelength < 4.0e-7:
            return 'ultraviolet ray'
        elif wavelength < 4.2e-7:
            return 'violet light'
        elif wavelength < 4.4e-7:
            return 'indigo light'
        elif wavelength < 5.0e-7:
            return 'blue light'
        elif wavelength < 5.2e-7:
            return 'cyan light'
        elif wavelength < 5.65e-7:
            return 'green light'
        elif wavelength < 5.9e-7:
            return 'yellow light'
        elif wavelength < 6.25e-7:
            return 'orange light'
        elif wavelength < 7.0e-7:
            return 'red light'
        elif wavelength < 1.4e-6:
            return 'near-infrared'
        else: return 'radio wave/microwave'
