# -*- coding: utf-8 -*-
#
# File : aranim/artobjects/ARTPoint.py
# Description : A simple point
# Date : 12th of January, 2021
#
# This file is part of Aranim.  Aranim is free software: you can
# redistribute it and/or modify it under the terms of the GNU General Public
# License as published by the Free Software Foundation, version 2.
#
# This program is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
# FOR A PARTICULAR PURPOSE.  See the GNU General Public License for more
# details.
#
# You should have received a copy of the GNU General Public License along with
# this program; if not, write to the Free Software Foundation, Inc., 51
# Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.
#
# Copyright Nils Schaetti, University of Neuchâtel <nils.schaetti@unine.ch>
# University of Geneva <nils.schaetti@unige.ch>

# Imports
import numpy as np


# Base Artanim point
class ARTPoint(object):
    """
    Base Artanim point
    """

    # region CONSTRUCTORS

    # Constructor
    def __init__(self, point: np.array):
        """
        Constructor
        :param point: 3D vector as Numpy array
        """
        # Properties
        self._point = point
    # end __init__

    # endregion CONSTRUCTORS

    # region PROPERTIES

    # X getter
    @property
    def x(self):
        """
        X getter
        :return: X position
        """
        return self._point[0]
    # end x

    # Setter X
    @x.setter
    def x(self, value):
        """
        Setter X
        :param value: New value
        """
        self._point[0] = value
    # end x

    # Y getter
    @property
    def y(self):
        """
        Y getter
        :return: Y position
        """
        return self._point[1]
    # end y

    # Setter Y
    @y.setter
    def y(self, value):
        """
        Setter Y
        :param value: New value
        """
        self._point[1] = value
    # end y

    # Z getter
    @property
    def z(self):
        """
        Z getter
        :return: Z position
        """
        return self._point[2]
    # end z

    # Setter Z
    @z.setter
    def z(self, value):
        """
        Setter Z
        :param value: New value
        """
        self._point[2] = value
    # end z

    # Point getter
    @property
    def point(self):
        """
        Point getter
        :return: Point position
        """
        return self._point
    # end point

    # Setter point
    @point.setter
    def point(self, value):
        """
        Setter point
        :param value: New value
        """
        self._point = value
    # end point

    # endregion PROPERTIES

# end ARTObject


# ARTSize
class ARTSize(ARTPoint):
    """
    A size
    """
    pass
# end ARTSize
