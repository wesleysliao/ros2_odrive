cmake_minimum_required(VERSION 3.5)

project(ros2_odrive_msgs)

if(NOT WIN32)
  set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -std=c++14 -Wall -Wextra")
endif()

find_package(ament_cmake REQUIRED)
# find the ROS message code generators
 find_package(rosidl_default_generators REQUIRED)

# declare the message files to generate code for
 set(msg_files
   "msg/ODriveAxisState.msg"
   "msg/ODriveControlMode.msg"
   "msg/ODriveEncoderMode.msg"
   "msg/ODriveErrorAxis.msg"
   "msg/ODriveErrorController.msg"
   "msg/ODriveErrorEncoder.msg"
   "msg/ODriveErrorMotor.msg"
   "msg/ODriveMotorType.msg"
 )

# declare the service files to generate code for
 set(srv_files
 )

 rosidl_generate_interfaces(${PROJECT_NAME}
   ${msg_files}
   ${srv_files}
 )

 ament_export_dependencies(rosidl_default_runtime)

ament_package()
