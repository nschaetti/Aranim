# -*- coding: utf-8 -*-
#
# File : aranim/ARTParamObject.py
# Description : Base class for parameterizable objects
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


# Base param class
class ARTParamObject(object):
    """
    Base class for parameterizable objects
    """

    # Default parameters
    PARAMS = {}

    # region CONSTRUCTORS

    # Constructor
    def __init__(self, **kwargs):
        """
        Constructor
        :param kwargs: Parameters
        """
        # Initialize parameters
        self._params = self.__class__.PARAMS

        # Set given parameters
        for param_key, param_value in kwargs.items():
            self._params[param_key] = param_value
        # end for
    # end __init__

    # endregion CONSTRUCTORS

    # region PUBLIC

    # Get parameter
    def get_param(self, param_key: str):
        """
        Get parameter
        :param param_key: Parameter name
        :return: Parameter value
        """
        if param_key in self._params:
            return self._params[param_key]
        else:
            return None
        # end if
    # end get_param

    # Set parameter value
    def set_param(self, param_key: str, param_value):
        """
        Set parameter value
        :param param_key: Parameter key
        :param param_value: New parameter value
        """
        self._params[param_key] = param_value
    # end set_param

    # endregion PUBLIC

# end ARTParamObject
