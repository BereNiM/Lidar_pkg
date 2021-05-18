cmake_minimum_required(VERSION 3.0.2)
project(lidar_description)

find_package(catkin REQUIRED COMPONENTS
  joint_state_publisher
  robot_state_publisher
)

catkin_package(

)

include_directories(
# include
  ${catkin_INCLUDE_DIRS}
)
