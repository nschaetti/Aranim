# -*- coding: utf-8 -*-
#
# File : aranim/artobjects/ARTObject.py
# Description : Base Artanim object
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
from aranim import ARTParamObject
from .ARTPoint import ARTPoint
from .ARTPoints import ARTPoints


# Base Artanim object
class ARTObject(ARTParamObject):
    """
    Base Artanim object
    """

    # region CONSTRUCTORS

    # Constructor
    def __init__(self, center: ARTPoint, points: ARTPoints = None, **kwargs):
        """
        Constructor
        :param center: Center point
        """
        # Super call
        super(ARTObject, self).__init__(**kwargs)

        # Properties
        self._center = center

        # Initialize points
        if points is None:
            self._points = ARTPoints()
        else:
            self._points = points
        # end if
        self._points = ARTPoints() if points is None else points
    # end __init__

    # endregion CONSTRUCTORS

    # region PROPERTIES

    # Center getter
    @property
    def center(self):
        """
        Center getter
        :return: Center position
        """
        return self._center

    # end center

    # Setter center
    @center.setter
    def center(self, value):
        """
        Setter center
        :param value: New value
        """
        self._center = value
    # end center

    # endregion PROPERTIES

# end ARTObject
