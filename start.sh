#!/bin/bash

world=$1

if [ -z "$world" ]; then
    echo "$0 <worldname>"
    exit 1
fi;

if ! [ -d /home/minecraft/$world ]; then
    sudo mkdir -p /home/minecraft/$world
    sudo chown -R 4242:4242 /home/minecraft/$world
fi;

sudo docker run\
    --net host\
    -v /home/minecraft/$world:/home/minecraft/volume\
    -it minecraft
