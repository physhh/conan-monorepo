from conans import ConanFile, CMake
from conan.tools.files import AutoPackager
import os

class HelloConan(ConanFile):
    name = "hello"
    version = "0.1"
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False]}
    default_options = {"shared": False}
    generators = "cmake"
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

        # Build and source infos
        self.cpp.source.components["a"].includedirs = ["a/include"]
        self.cpp.build.components["a"].libdirs = ["lib"]

        self.cpp.source.components["b"].includedirs = ["b/include"]
        self.cpp.build.components["b"].libdirs = ["lib"]

        # Package infos
        self.cpp.package.components["a"].includedirs = ["include/a"]
        self.cpp.package.components["a"].libs = ["hello-a"]
        self.cpp.package.components["a"].libdirs = ["lib"]
        
        self.cpp.package.components["b"].includedirs = ["include/b"]
        self.cpp.package.components["b"].libs = ["hello-b"]
        self.cpp.package.components["b"].libdirs = ["lib"]


    def package(self):
        packager = AutoPackager(self)
        packager.run()

