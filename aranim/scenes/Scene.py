# -*- coding: utf-8 -*-
#
# File : aranim/scenes/Scene.py
# Description : Base scene
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
from aranim.artobjects import ARTObject
from aranim.artobjects.camera import Camera
from aranim.artobjects.ARTPoint import ARTPoint


# Base scene
class Scene(ARTParamObject):
    """
    Base scene
    """

    # region CONSTRUCTORS

    # Constructor
    def __init__(self, name, **kwargs):
        """
        Constructor
        :param name: Scene name
        """
        # Super call
        super(Scene, self).__init__(**kwargs)

        # Properties
        self._name = name
        self._objects = list()
        self._camera = None
    # end __init__

    # endregion CONSTRUCTORS

    # region PROPERTIES

    # Get the current camera
    @property
    def camera(self) -> Camera:
        """
        Get the current camera
        :return: Current camera
        """
        return self._camera
    # end camera

    # Set current camera
    @camera.setter
    def camera(self, cam: Camera) -> None:
        """
        Set current camera
        :param cam: New current camera
        """
        self._camera = cam
    # end camera

    # endregion PROPERTIES

    # region PUBLIC

    # Add an object to the scene
    def add_object(self, o: ARTObject) -> None:
        """
        Add an object to the scene
        :param o: Object to be added
        """
        self._objects.append(o)
    # end add_object

    # Remove object
    def remove_object(self, o: ARTObject) -> None:
        """
        Remove object
        :param o: Object to be removed
        """
        self._objects.remove(o)
    # end remove_object

    # endregion PUBLIC

# end Scene
