#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Copyright (c) 2022 Stéphane Caron.
#
# This file is part of upkie_description.
#
# upkie_description is free software: you can redistribute it and/or modify it
# under the terms of the GNU General Public License as published by the Free
# Software Foundation, either version 3 of the License, or (at your option) any
# later version.
#
# upkie_description is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or
# FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more
# details.
#
# You should have received a copy of the GNU General Public License along with
# upkie_description. If not, see <http://www.gnu.org/licenses/>.

"""
Compute the inertia matrix of a cylinder and print it as URDF.

Source:
    https://en.wikipedia.org/wiki/List_of_moments_of_inertia#List_of_3D_inertia_tensors
"""

import argparse
import sys


def parse_command_line_arguments():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("mass", type=float, help="total mass in [kg]")
    parser.add_argument(
        "radius", type=float, help="radius in [m] in the xy-plane"
    )
    parser.add_argument(
        "length", type=float, help="length in [m] along the z-axis"
    )
    return parser.parse_args()


if __name__ == "__main__":
    args = parse_command_line_arguments()
    mass, radius, length = args.mass, args.radius, args.length
    ixx = mass / 12.0 * (3 * radius ** 2 + length ** 2)
    iyy = mass / 12.0 * (3 * radius ** 2 + length ** 2)
    izz = mass / 2.0 * radius ** 2
    print(f'<cylinder radius="{radius}" length="{length}" />')
    print(f'<mass value="{mass}" />')
    print(f"\n<!-- {' '.join(sys.argv)} -->")
    print(
        f'<inertia ixx="{ixx}" ixy="0" ixz="0" '
        f'iyx="0" iyy="{iyy}" iyz="0" '
        f'izx="0" izy="0" izz="{izz}" />'
    )
