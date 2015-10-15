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

log_info "Ensuring directories..."
for directory in world backups config logs; do
    if ! [ -d $VOLUME/$directory ]; then
        log_warning "No directory $VOLUME/$directory"
        mkdir -v $VOLUME/$directory;
        chown minecraft:minecraft $VOLUME/$directory;
        log_success "Created and modded $VOLUME/$directory"
    fi;
done;

if ! [ -f $VOLUME/config/server.properties ]; then
    log_warning "No $VOLUME/config/server.properties, adding default"
    cp $RUNTIME/server.properties.default $VOLUME/config/server.properties
    chown minecraft:minecraft $VOLUME/config/server.properties
    log_info "Ensured default server.properties"
fi;

if ! [ -f $VOLUME/config/server.properties.variable ]; then
    log_warning "No $VOLUME/config/server.properties.variable, adding default"
    cp $RUNTIME/server.properties.variable.default $VOLUME/config/server.properties.variable
    chown minecraft:minecraft $VOLUME/config/server.properties.variable
    log_info "Ensured default server.properties.variable"
fi;

log_info "Creating symlinks..."
ln -vs $VOLUME/world $RUNTIME/world

for file in banned-ips.json \
            banned-players.json \
            ops.json \
            usercache.json \
            whitelist.json; do
    if ! [ -f $VOLUME/config/$file ]; then
        log_info "Initializing empty $file"
        echo "[]" > $VOLUME/config/$file;
        chown minecraft:minecraft $VOLUME/config/$file
    fi;
    ln -vs $VOLUME/config/$file $RUNTIME/$file
done;

/generate_server_properties.sh

ln -vs $VOLUME/config/server.properties.generated $RUNTIME/server.properties

chown minecraft:minecraft $VOLUME/config/server.properties.generated

log_info "Ensuring Webapp database..."

ln -vs /home/minecraft/volume/config/db.sqlite3 /home/minecraft/webapp/db.sqlite3

if ! [ -f /home/minecraft/volume/config/db.sqlite3 ]; then
    log_warning "The webapp seems uninitialized"
    cd /home/minecraft/webapp
    su -c "python manage.py syncdb --noinput" minecraft
    echo "from django.contrib.auth.models import User; User.objects.create_superuser('admin', 'admin@example.com', 'admin')" |\
        python ./manage.py shell
    log_success "Database initialized !"
else
    log_info "Syncing database"
    cd /home/minecraft/webapp
    su -c "python manage.py syncdb --noinput" minecraft
    log_success "Done"
fi;

crond &

/usr/sbin/sshd

/usr/bin/supervisord -n -c /etc/supervisor/supervisord.conf

su -c "/backup.sh" minecraft
