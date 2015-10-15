#!/bin/bash

# Copyright (C) 2015 Thomas Maurice <thomas@maurice.fr>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

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
