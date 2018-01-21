import os
from conans import ConanFile, CMake, tools


class HAPIConan(ConanFile):
    name = "hapi"
    version = "1.4-beta"
    url = "https://github.com/ulricheck/conan-hapi.git"

    short_paths = True
    settings = "os", "compiler", "build_type", "arch"
    generators = "cmake"
    exports = "FindHAPI.cmake"
    options = {"shared": [True, False]}
    default_options = "shared=True"

    requires = (
        "h3dutil/1.4-beta@camposs/stable",
        )

    # exports = "*"
    def requirements(self):
        if self.settings.os == "Windows":
            self.requires("h3dapi_windows_dependencies/[>=2.3]@camposs/stable")

    def imports(self):
        #needed to replace the existing findXXX.cmake scripts from H3D common modules
        self.copy("FindH3DUtil.cmake", src="cmake", dst="source/build/localModules", root_package="h3dutil")

    def source(self):
        repo_url = "https://www.h3dapi.org:8090/HAPI/trunk/"
        self.run("svn checkout %s source" % repo_url)
        tools.replace_in_file("source/build/CMakeLists.txt", "project( HAPI )", '''project( HAPI )
include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup()
MESSAGE(STATUS "Using External Root: $ENV{H3D_EXTERNAL_ROOT}")
''')
       
    def build(self):
        cmake = CMake(self)
        cmake.definitions["BUILD_SHARED_LIBS"] = self.options.shared
        cmake.configure(source_dir=os.path.join("source", "build"))
        cmake.build()
        cmake.install()

    def package(self):
        self.copy(pattern='*.h' , dst="include", src="source/include", keep_path=True)
        self.copy(pattern='FindHAPI.cmake' , dst="cmake", keep_path=False)

    def package_info(self):
        if self.settings.arch == "x86":
            libfolder = "lib32"
        else:
            libfolder = "lib64"

        self.cpp_info.libs = tools.collect_libs(self, folder=libfolder)
