cmake_minimum_required(VERSION 2.8.3)
project(door_control)

## Find catkin macros and libraries
find_package(catkin)

include_directories(${catkin_INCLUDE_DIRS})

catkin_package()

if(CATKIN_ENABLE_TESTING)
  find_package(roslaunch REQUIRED)
  roslaunch_add_file_check(launch)
endif()

install(DIRECTORY config launch
  DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}
)
