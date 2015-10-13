#/bin/bash

set -e
set -x

bower install --allow-root

if ! [ -z "$DESTINATION_UID" ] && ! [ -z "$DESTINATION_GID" ]; then
    chown -R $DESTINATION_UID:$DESTINATION_GID /build/bower_components
fi;
