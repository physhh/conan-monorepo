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
        
        self.cpp.source.includedirs = [
            "a/include",
            "b/include",
        ]

        self.cpp.build.libdirs = ["lib"]
        self.cpp.build.bindirs = ["bin"]

        self.cpp.package.libs = ["hello-a", "hello-b"]
        self.cpp.package.includedirs = [
            "include/a",
            "include/b",
        ]


    def package(self):
        packager = AutoPackager(self)
        packager.run()

    def package_info(self):
        self.cpp_info.libs = ["hello"]
