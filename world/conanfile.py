from conans import ConanFile, CMake
from conan.tools.files import AutoPackager
import os

class WorldConan(ConanFile):
    name = "world"
    version = "0.1"
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False]}
    default_options = {"shared": False}
    requires = "hello/0.1"
    generators = "cmake_paths", "cmake_find_package"
    exports_sources = "project/*"

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

        _add_component("a", ["hello::a"])
        _add_component("b", ["hello::b"])


    def package(self):
        packager = AutoPackager(self)
        packager.run()

