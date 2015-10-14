#/bin/bash

set -e
set -x

addgroup -g $DESTINATION_GID build
adduser -S -G build -s /bin/bash -h /home/build -u $DESTINATION_UID build

echo '{"interactive": false}' > /home/build/.bowerrc
su -c "npm install" build
su -c "bower install" build
su -c "grunt" build
