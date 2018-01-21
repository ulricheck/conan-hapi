#=============================================================================
# Copyright 2001-2011 Kitware, Inc.
#
# Distributed under the OSI-approved BSD License (the "License");
# see accompanying file Copyright.txt for details.
#
# This software is distributed WITHOUT ANY WARRANTY; without even the
# implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
# See the License for more information.
#=============================================================================
# (To distribute this file outside of CMake, substitute the full
#  License text for the above reference.)

find_path(HAPI_INCLUDE_DIR NAMES HAPI/HAPI.h PATHS ${CONAN_INCLUDE_DIRS_HAPI})
find_library(HAPI_LIBRARY NAMES ${CONAN_LIBS_HAPI} PATHS ${CONAN_LIB_DIRS_HAPI})

MESSAGE("** HAPI ALREADY FOUND BY CONAN!")
SET(HAPI_FOUND TRUE)
MESSAGE("** FOUND HAPI:  ${HAPI_LIBRARY}")
MESSAGE("** FOUND HAPI INCLUDE:  ${HAPI_INCLUDE_DIR}")

set(HAPI_INCLUDE_DIRS ${HAPI_INCLUDE_DIR})
set(HAPI_LIBRARIES ${HAPI_LIBRARY})

mark_as_advanced(HAPI_LIBRARY HAPI_INCLUDE_DIR)