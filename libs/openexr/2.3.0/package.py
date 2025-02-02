# Taken from OSS-Pipeline form https://github.com/OSS-Pipeline/rez-openexr

name = "openexr"

version = "2.3.0"

authors = [
    "Industrial Light & Magic"
]

description = \
    """
    OpenEXR is a high dynamic-range (HDR) image file format for use in computer imaging applications.
    """

requires = [
    "cmake-3+",
    "gcc-6+",
    "ilmbase-{version}".format(version=str(version)),
    "zlib-1.2+"
]

variants = [
    ["platform-linux"]
]

tools = [
    "exrenvmap",
    "exrheader",
    "exrmakepreview",
    "exrmaketiled",
    "exrmultipart",
    "exrmultiview",
    "exrstdattr"
]

build_system = "cmake"

uuid = "openexr-{version}".format(version=str(version))

def commands():
    env.PATH.prepend("{root}/bin")
    env.LD_LIBRARY_PATH.prepend("{root}/lib")
    env.PKG_CONFIG_PATH.prepend("{root}/lib/pkgconfig")

    # Helper environment variables.
    env.OPENEXR_BINARY_PATH.set("{root}/bin")
    env.OPENEXR_INCLUDE_PATH.set("{root}/include")
    env.OPENEXR_LIBRARY_PATH.set("{root}/lib")
