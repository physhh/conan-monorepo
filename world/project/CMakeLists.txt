cmake_minimum_required(VERSION 3.20)

project(world)

include(${CMAKE_BINARY_DIR}/conan_paths.cmake)

find_package(hello REQUIRED)

add_library(world-a 
  "a/include/world/a.h"
  "a/src/a.cpp"
)
target_include_directories(world-a 
  PUBLIC "a/include"
)
target_link_libraries(world-a 
  PUBLIC hello::a
)

add_library(world-b 
  "b/include/world/b.h"
  "b/src/b.cpp"
)
target_include_directories(world-b
  PUBLIC "b/include"
)
target_link_libraries(world-b 
  PUBLIC hello::b
)