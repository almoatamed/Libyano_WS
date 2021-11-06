cmake_minimum_required(VERSION 3.0.2)
project(global)

find_package(catkin REQUIRED COMPONENTS
  roscpp
  rospy
)


###################################
## catkin specific configuration ##
###################################
catkin_package(
)

###########
## Build ##
###########
include_directories(
# include
  ${catkin_INCLUDE_DIRS}
)

#############
## Install ##
#############

catkin_install_python(PROGRAMS
  scripts/backend.py
  scripts/interface.py
  DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
)
