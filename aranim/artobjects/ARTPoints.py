# -*- coding: utf-8 -*-
#
# File : aranim/artobjects/ARTPoints.py
# Description : A set of points
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

# Aranim imports
from .ARTPoint import ARTPoint


# A set of points
class ARTPoints(object):
    """
    A set of points
    """

    # region CONSTRUCTORS

    # Constructor
    def __init__(self, points: np.array = None):
        """
        Constructor
        :param points: A numpy array of size (3, n_points)
        """
        # Initialize points
        if points is None:
            self._points = np.array([[], [], []])
        else:
            self._points = points
        # end if
    # end __init__

    # endregion CONSTRUCTORS

    # region PROPERTIES

    # Points getter
    @property
    def points(self):
        """
        Points getter
        :return: Points position
        """
        return self._points
    # end points

    # Setter points
    @points.setter
    def points(self, value):
        """
        Setter points
        :param value: New value
        """
        self._points = value
    # end points

    # region PUBLIC

    # Add a point to the set
    def add(self, p: ARTPoint) -> None:
        """
        Add a point to the set
        :param p: A point
        """
        self._points = np.concatenate(
            (
                self._points,
                np.reshape(p.point, (3, 1))
            ),
            axis=1
        )
    # end add

    # Add a point to the set
    def add(self, x: float, y: float, z: float) -> None:
        """
        Add a point to the set
        :param x: X position
        :param y: Y position
        :param z: Z position
        """
        # Concatenate to the list of points
        self._points = np.concatenate(
            (
                self._points,
                np.array([[x], [y], [z]])
            ),
            axis=1
        )
    # end add

    # Apply matrix transformation
    def apply_matrix_transform(self, trans_matrix: np.array) -> None:
        """
        Apply matrix transformation
        :param trans_matrix: A (3, 3) transformation matrix
        """
        self._points = np.matmul(trans_matrix, self._points)
    # end apply_matrix_transform

    # endregion PUBLIC

    # region OVERRIDE

    # Number of points
    def __len__(self):
        """
        Number of points
        :return: Number of points
        """
        return self._points.shape[1]
    # end __len__

    # endregion OVERRIDE

# end ARTPoints
