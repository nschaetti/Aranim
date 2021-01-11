# -*- coding: utf-8 -*-
#
# File : examples/cairo/example.py
# Description : Example of basic Cairo code
# Date : 11th of January, 2021
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
import math
import cairo


# Image width
IMG_WIDTH, IMG_HEIGHT = 800, 800

# Cairo surface
surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, IMG_WIDTH, IMG_HEIGHT)

# Context
ctx = cairo.Context(surface)

# Draw a rectangle
ctx.set_line_width(1)
ctx.set_source_rgba(1.0, 0.0, 0.0, 1.0)
ctx.rectangle(0.0, 0.0, 400, 400)
ctx.stroke()

# Draw an arc
ctx.arc(400, 400, 50, 0.0, math.pi)
ctx.set_source_rgba(0.0, 1.0, 0.0, 1.0)
ctx.set_line_width(2)
ctx.stroke()

# Draw path
ctx.move_to(200, 200)
ctx.line_to(250, 225)
ctx.rel_line_to(50, -25)
ctx.arc(250, 250, 250 * math.sqrt(2), -0.25 * math.pi, 0.25 * math.pi)
ctx.rel_curve_to(-25, -12.5, -25, 12.5, -5, 0)
ctx.close_path()
ctx.set_line_width(4)
ctx.set_source_rgb(0.0, 0.0, 1.0)
ctx.stroke()

# Pattern
radpat = cairo.RadialGradient(250, 250, 100, 500, 500, 0.5)
radpat.add_color_stop_rgb(0, 1.0, 0.8, 0.8)
radpat.add_color_stop_rgb(1, 0.9, 0.0, 0.0)

# Create squares
for i in range(1, 10):
    for j in range(1, 10):
        ctx.rectangle()

# Write to PNG
surface.write_to_png("example.png")
