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
URDF description for the Upkie wheeled biped.
"""

import os

__version__ = "1.1.1"

# Path to upkie_description
path = os.path.dirname(os.path.realpath(__file__))

# Path to the meshes folder
meshes_path = os.path.join(path, "meshes")

# Path to the robot's URDF
urdf_path = os.path.join(path, "urdf", "upkie.urdf")

__all__ = [
    "meshes_path",
    "path",
    "urdf_path",
]
