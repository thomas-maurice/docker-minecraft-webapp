#!/bin/bash

VOLUME=/home/minecraft/volume
RUNTIME=/home/minecraft/runtime

function log_info() {
    echo -e "\e[1;94m[`date +%Y-%m-%d:%H:%M:%S`]\e[0m $@"
}
function log_success() {
    echo -e "\e[1;32m[`date +%Y-%m-%d:%H:%M:%S`]\e[0m $@"
}
function log_error() {
    echo -e "\e[1;31m[`date +%Y-%m-%d:%H:%M:%S`]\e[0m $@"
}
function log_warning() {
    echo -e "\e[1;93m[`date +%Y-%m-%d:%H:%M:%S`]\e[0m $@"
}

log_info "Generating server.properties"

cat $VOLUME/config/server.properties > $VOLUME/config/server.properties.generated
cat $VOLUME/config/server.properties.variable >> $VOLUME/config/server.properties.generated


echo "`openssl rand -base64 42`" > $VOLUME/config/rcon_password
echo "rcon.password=`cat $VOLUME/config/rcon_password`" >> $VOLUME/config/server.properties.generated

cat $VOLUME/config/server.properties.generated

log_success "Done."
