#!/bin/bash

set -x

UID=`id -u`
GID=`id -g`

sudo docker run -v `pwd`:/build \
    -e DESTINATION_UID=$UID \
    -e DESTINATION_GID=$GID \
    -it build_static
