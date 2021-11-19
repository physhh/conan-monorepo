cmake_minimum_required(VERSION 3.0)

project(WorkspaceProject)

set(CMAKE_PREFIX_PATH "${CMAKE_CURRENT_LIST_DIR}/configs;${CMAKE_PREFIX_PATH}")

add_subdirectory("../hello/project" "${CMAKE_BINARY_DIR}/hello")
add_subdirectory("../world/project" "${CMAKE_BINARY_DIR}/world")
