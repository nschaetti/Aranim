# -*- coding: utf-8 -*-
#
# File : aranim/rendering/CairoRenderer.py
# Description : Rendering with Cairo
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
import cairo
import numpy as np

# Aranim imports
from .Renderer import Renderer
from aranim.artobjects.camera import Camera
from aranim.artobjects.ARTPoint import ARTPoint


# Rendering with Cairo
class CairoRenderer(Renderer):
    """
    A renderer which uses Cairo
    """

    # Default parameters
    PARAMS = {
        'resolution': (1080, 720)
    }

    # region CONSTRUCTORS

    # Constructor
    def __init__(self, cairo_surface: cairo.Surface=None, cairo_format: cairo.Format=cairo.FORMAT_ARGB32, **kwargs) -> None:
        """
        Constructor
        :param cairo_surface: A Cairo surface to use or None
        :param kwargs:
        """
        # Super
        super(CairoRenderer, self).__init__(**kwargs)

        # Cairo surface
        if cairo_surface is None:
            self._surface = cairo.ImageSurface(
                cairo_format,
                self.get_param('resolution')[0],
                self.get_param('resolution')[1]
            )
        else:
            self._surface = cairo_surface
        # end if

        # Initialize context
        self._context = cairo.Context(self._surface)

        # Properties
        self._cameras = list()
    # end __init__

    # endregion CONSTRUCTORS

    # region PUBLIC

    # Add a camera to the renderer
    def add(self, cam: Camera, pos: ARTPoint) -> None:
        """
        Add a camera to the renderer
        :param cam: The camera to be added
        :param pos: The position of the camera on the screen
        """
        self._cameras.append((cam, pos))
    # end add

    # endregion PUBLIC

    # region OVERRIDE

    # Render the animation at time t
    def render(self, t: int=0.0) -> np.array:
        """
        Render animation at time t
        :param t:
        :return:
        """
        pass
    # end render

    # endregion OVERRIDE

# end CairoRenderer
