#!/bin/bash

cd build_static && sudo docker build -t build_static .
./build_webapp.sh
sudo docker build -t minecraft .
