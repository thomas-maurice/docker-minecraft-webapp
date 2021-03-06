#!/bin/bash

set -x

UID=`id -u 2>>/dev/null`
GID=`id -g 2>>/dev/null`

sudo docker run -v `pwd`:/build \
    -e DESTINATION_UID=$UID \
    -e DESTINATION_GID=$GID \
    -it build_static
