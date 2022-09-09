name = "pyilmbase"

version = "2.3.0"

authors = [
    "Industrial Light & Magic"
]

description = \
    """
    Python bindings for IlmBase.
    """

requires = [
    "boost-1.61+",
    "cmake-3+",
    "gcc-6+",
    "ilmbase-{version}".format(version=str(version)),
    "numpy-1.12.1",
]

variants = [
    ["platform-linux", "python-2.7"]
    #  ["platform-linux", "python-3.6"]
]

build_system = "cmake"

uuid = "pyilmbase-{version}".format(version=str(version))

def commands():
    env.LD_LIBRARY_PATH.prepend("{root}/lib")
    env.PYTHONPATH.prepend("{root}/lib/python" + str(env.REZ_PYTHON_MAJOR_VERSION) + "." + str(env.REZ_PYTHON_MINOR_VERSION) + "/site-packages")

    # Helper environment variables.
    env.PYILMBASE_INCLUDE_PATH.set("{root}/include")
    env.PYILMBASE_LIBRARY_PATH.set("{root}/lib")
