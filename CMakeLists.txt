cmake_minimum_required(VERSION 3.1)
project(jvrc_description VERSION 1.0.4)

find_package(catkin)

catkin_package()

install(DIRECTORY meshes urdf
    DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}
)
