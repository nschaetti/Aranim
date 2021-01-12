# -*- coding: utf-8 -*-
#
# File : aranim/artobjects/geometry/Rectangle.py
# Description : Simple rectangle object
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
from .. import ARTObject

# Rectangle object
class Rectangle(ARTObject):
    """
    Rectangle object
    """

    # region CONSTRUCTORS

    # Constructor
    def __init__(self, center, size):
        """
        Constructor
        :param center: Center point (ARTPoint)
        :param size: Rectangle size (ARTSize)
        """
        # Super
        super(Rectangle, self).__init__(center)

        # Properties
        self._size = size
    # end __init__

    # endregion CONSTRUCTORS

# end Rectangle
