# Changelog

All notable changes to this project will be documented in this file.

## [1.1.0] - 2022/05/23

### Added

- Build file to use the model in Bazel projects
- Illustration to the README
- Link to the mjbots quad chassis
- Python distribution of the model

### Changed

- Relicense the project to Apache 2.0
- Turn IMU 180 degrees around the base yaw axis

### Fixed

- Cleaned dangling Bazel reference to ``//tools/lint``
- Links to Printables.com
- Project name for CMake

## [1.0.0] - 2022/03/17

Initial robot description.

### Added

- Mesh files for the legs, wheel tire and mjbots parts
- ROS build and package files
- Robot description (kinematics, inertias, collisions) in URDF
- Scripts to compute box and cylinder inertias
