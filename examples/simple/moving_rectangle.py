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
import numpy as np
import aranim
import aranim.rendering
from aranim.artobjects.camera import Camera
from aranim.artobjects import ARTPoint, ARTSize
from aranim.scenes import Scene
import aranim.artobjects.geometry as argeo

# Create a renderer with Cairo
renderer = aranim.rendering.CairoRenderer(resolution=(800, 600), fps=60)

# A new scene
main_scene = Scene("main")

# Add a camera on the whole screen
main_scene.camera = Camera(ARTPoint(np.array([0, 0])), ARTSize(np.array([8, 6])))

# Add a rectangle
main_scene.add_object(argeo.Rectangle())


