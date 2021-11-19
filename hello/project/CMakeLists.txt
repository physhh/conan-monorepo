cmake_minimum_required(VERSION 3.20)

project(hello)

include(${CMAKE_BINARY_DIR}/conan_paths.cmake)

add_library(hello-a 
  "a/include/hello/a.h"
  "a/src/a.cpp"
)
target_include_directories(hello-a 
  PUBLIC "a/include"
)

add_library(hello-b 
  "b/include/hello/b.h"
  "b/src/b.cpp"
)
target_include_directories(hello-b
  PUBLIC "b/include"
)