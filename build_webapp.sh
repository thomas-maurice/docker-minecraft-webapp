#!/bin/bash

rm -rf webapp_build
cp -r webapp webapp_build
cd webapp_build && rm -rf .git *.sqlite3
find -name "*.pyc" -delete
../build_static/build_static.sh
rm -rf bower_components node_modules
