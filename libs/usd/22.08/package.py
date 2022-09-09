name = "usd"

version = "22.08"

authors = [
    "Pixar"
]

description = \
    """
    Universal Scene Description (USD) is an efficient, scalable system for authoring, reading, and streaming
    time-sampled scene description for interchange between graphics applications.
    """

requires = [
    "platform-linux",
    "boost-1.61+<1.80",
    "cmake-3+<3.20",
    "gcc-6.0+",
    "glew-2+",
    "ilmbase-2.2+<2.4",
    "jinja2-2+",
    "ocio-1.0.9+",
    "openexr-2.2+<2.4",
    "oiio-1.7.14+",
    "opensubdiv-3.3+",
    "ptex-2.1+",
    "pyopengl-3+",
    "pyside2-5.12+",
    "tbb-2017.U6+",
]

variants = [
    ["python-2.7"]
]

tools = [
    "sdfdump",
    "sdffilter",
    "testusdview",
    "usdcat",
    "usdchecker",
    "usddiff",
    "usddumpcrate",
    "usdedit",
    "usdGenSchema",
    "usdrecord",
    "usdresolve",
    "usdstitch",
    "usdstitchclips",
    "usdtree",
    "usdview",
    "usdzip"
]

build_system = "cmake"

uuid = "usd-{version}".format(version=str(version))

def commands():
    env.PATH.prepend("{root}/bin")
    env.LD_LIBRARY_PATH.prepend("{root}/lib")
    env.PYTHONPATH.prepend("{root}/lib/python")
    env.CMAKE_MODULE_PATH.prepend("{root}")

    # Helper environment variables.
    env.USD_BINARY_PATH.set("{root}/bin")
    env.USD_INCLUDE_PATH.set("{root}/include")
    env.USD_LIBRARY_PATH.set("{root}/lib")

    env.PXR_USD_LOCATION.set("{root}")
