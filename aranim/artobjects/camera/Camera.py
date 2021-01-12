# -*- coding: utf-8 -*-
#
# File : aranim/artobjects/camera/Camera.py
# Description :
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


# Aranim imports
from .. import ARTObject, ARTPoint, ARTSize

# Camera object
class Camera(ARTObject):
    """
    A Camera object
    """

    # region CONSTRUCTORS

    # Constructor
    def __init__(self, center: ARTPoint = None, size: ARTSize = None):
        """
        Constructor
        :param center: Center position
        :param size: Size (width, height)
        """
        # Super
        super(Camera, self).__init__(center)

        # Properties
        self._size = size
    # end __init__

    # endregion CONSTRUCTORS

# end Camera
