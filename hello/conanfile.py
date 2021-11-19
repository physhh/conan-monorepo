from conans import ConanFile, CMake
from conan.tools.files import AutoPackager
import os

class HelloConan(ConanFile):
    name = "hello"
    version = "0.1"
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False]}
    default_options = {"shared": False}
    generators = "cmake_paths", "cmake_find_package"
    exports_sources = "project/*"
    requires = ["fmt/8.0.1"]

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()

    def layout(self):
        build_type = str(self.settings.build_type).lower()

        self.folders.source = "project"
        self.folders.build = "build/{}".format(build_type)
        self.folders.generators = os.path.join(self.folders.build, "conan")

        def _add_component(component_name, requires):
            self.cpp.source.components[component_name].includedirs = ["{}/include".format(component_name)]
            self.cpp.build.components[component_name].libdirs = ["."]
            
            self.cpp.package.components[component_name].includedirs = ["include/{}".format(component_name)]
            self.cpp.package.components[component_name].libs = ["{}-{}".format(self.name, component_name)]
            self.cpp.package.components[component_name].libdirs = ["lib"]
            self.cpp.package.components[component_name].requires = requires

        _add_component("a", [])
        _add_component("b", ["fmt::fmt"])


    def package(self):
        packager = AutoPackager(self)
        packager.run()

