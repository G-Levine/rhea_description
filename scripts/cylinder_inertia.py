#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Copyright 2022 Stéphane Caron
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

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
