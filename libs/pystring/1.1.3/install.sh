#!/usr/bin/bash

# Will exit the Bash script the moment any command will itself exit with a non-zero status, thus an error.
set -e

BUILD_PATH=$1
PYSTRING_VERSION=${REZ_BUILD_PROJECT_VERSION}

# We print the arguments passed to the Bash script.
echo -e "\n"
echo -e "==============="
echo -e "=== INSTALL ==="
echo -e "==============="
echo -e "\n"

echo -e "[INSTALL][ARGS] BUILD PATH: ${BUILD_PATH}"
echo -e "[INSTALL][ARGS] PYSTRING VERSION: ${PYSTRING_VERSION}"

# We check if the arguments variables we need are correctly set.
# If not, we abort the process.
if [[ -z ${BUILD_PATH} || -z ${PYSTRING_VERSION} ]]; then
    echo -e "\n"
    echo -e "[INSTALL][ARGS] One or more of the argument variables are empty. Aborting..."
    echo -e "\n"

    exit 1
fi

# We install pystring.
echo -e "\n"
echo -e "[INSTALL] Installing pystring-${PYSTRING_VERSION}..."
echo -e "\n"

cd ${BUILD_PATH}

make \
    -j${REZ_BUILD_THREAD_COUNT} \
    install

echo -e "\n"
echo -e "[INSTALL] Finished installing pystring-${PYSTRING_VERSION}!"
echo -e "\n"
