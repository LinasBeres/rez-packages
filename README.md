Overview
========

This is a repository of package installers. Each directory contains a rez
project that you can build (using `rez-build`) or release (using `rez-release`).
Doing so will build or release the associated software (gcc, boost etc) as a
rez package.

Please note that this project repository is for reference only. You should copy
them into your own repo - at that point you can set the correct versions, put a
requirement on your operating system of choice, and so on.

## Setup

Firstly please set these environmental variables:
```
export REZ_REPO_PAYLOAD_DIR=<path/to/tars>
export REZ_TMP_PATH=<path/to/tmp>
export REZ_BUILD_THREAD_COUNT=<buildThreadCount>
```

Clone rez and cd there:
```
git clone git@github.com:AcademySoftwareFoundation/rez.git <dir/to/rez>
cd <dir/to/rez>
```

Checkout to HEAD or required tag:
```
git checkout tags/<tag>
```

Install rez (system wide or locally):
```
python ./install.py <path/to/rez/install>
```

Add rez install bin to path:
```
export PATH=<path/to/rez/install>/bin/rez${PATH:+:${PATH}}
```

Quickstart rez:
```
rez-bind --quickstart
```

And there you go, you are free to use this repo.

