# -*- coding: utf-8 -*-
#
# File : aranim/rendering/Renderer.py
# Description : Base renderer object
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
from .. import ARTParamObject
from aranim.artobjects.camera import Camera
from aranim.artobjects.ARTPoint import ARTPoint


# Renderer base class
class Renderer(ARTParamObject):
    """
    Renderer base class
    """

    # region CONSTRUCTORS

    # Constructor
    def __init__(self, **kwargs):
        """
        Constructor
        :param kwargs: Arguments
        """
        # Super
        super(Renderer, self).__init__(**kwargs)

        # List of cameras
        self._cameras = list()
    # end __init__

    # endregion CONSTRUCTORS

    # region PUBLIC

    # Add a camera to the renderer
    def add_camera(self, cam: Camera, pos: ARTPoint) -> None:
        """
        Add a camera to the renderer
        :param cam: The camera to be added
        :param pos: The position of the camera on the screen
        """
        self._cameras.append((cam, pos))
    # end add_camera

    # endregion PUBLIC

    # region TO_IMPLEMENT

    # Render the animation at time t
    def render(self, t: int=0.0) -> np.array:
        """
        Render the animation at time t
        :param t: Time position
        :return: Image an a numpy array
        """
        raise Exception("render method must be implemented")
    # end render

    # endregion TO_IMPLEMENT

# end Renderer
