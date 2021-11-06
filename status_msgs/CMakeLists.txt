cmake_minimum_required(VERSION 3.0.2)
project(status_msgs)

find_package(catkin REQUIRED COMPONENTS
  roscpp
  rospy
  message_generation
  std_msgs
)

add_message_files(
  FILES

  string_msg.msg
  vector.msg
  color_msg.msg
  quaternion.msg

  bmp280_chip.msg
  bno055_chip.msg
  imu_msg.msg

  power_msg.msg

  pixelgrid_msg.msg
  led_ring_msg.msg

  controllers_msg.msg
  
  sensors_msg.msg

  servo_msg.msg

  cash_reader_msg.msg
  cash_reader_counters_msg.msg
  cash_reader_channel_msg.msg

  axis_msg.msg
  driver_system_msg.msg
  driver_msg.msg
  encoder_msg.msg
  motor_msg.msg
  axis_msg.msg

  goal_monitor_msg.msg
  
  status.msg


)

generate_messages(
  DEPENDENCIES
  std_msgs
)

catkin_package(
#  INCLUDE_DIRS include
#  LIBRARIES mcu_msgs
 CATKIN_DEPENDS roscpp rospy std_msgs message_runtime
#  DEPENDS system_lib
)

include_directories(
# include
  ${catkin_INCLUDE_DIRS}
)
