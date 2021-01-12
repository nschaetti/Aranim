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


# Base scene
class Scene(object):
    """
    Base scene
    """

    # region CONSTRUCTORS

    # Constructor
    def __init__(self, name):
        """
        Constructor
        :param name: Scene name
        """
        # Properties
        self._name = name
        self._objects = list()
    # end __init__

    # endregion CONSTRUCTORS

    # region PUBLIC

    # Add an object to the scene
    def add(self, o):
        """
        Add an object to the scene
        :param o: Object to be added
        """
        self._objects.append(o)
    # end add

    # endregion PUBLIC

# end Scene
