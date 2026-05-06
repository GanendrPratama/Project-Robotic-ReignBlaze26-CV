cmake_minimum_required(VERSION 3.0.2)
project(vision_obstacle_pkg)

find_package(catkin REQUIRED COMPONENTS
  rospy
  std_msgs
  message_generation
  sensor_msgs
  cv_bridge
)

add_message_files(
  FILES
  ObjectDistance.msg
)

generate_messages(
  DEPENDENCIES
  std_msgs
)

catkin_package(
  DEFAULT_INCLUDES
#  INCLUDE_DIRS include
#  LIBRARIES vision_obstacle_pkg
  CATKIN_DEPENDS rospy std_msgs message_runtime sensor_msgs cv_bridge
#  DEPENDS system_lib
)

catkin_install_python(PROGRAMS
  scripts/camera_rs_node.py
  scripts/object_detect_node.py
  scripts/sensor_fusion_node.py
  scripts/utils.py
  DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
)
