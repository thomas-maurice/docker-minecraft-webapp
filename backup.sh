#!/bin/bash

set -x

VOLUME=/home/minecraft/volume
BACKUPDIR=$VOLUME/backups
BAK=`date +%Y-%m-%d-%Hh%Mm%Ss`

cd $VOLUME

tar zcvf $BACKUPDIR/${BAK}_world.tgz world
tar zcvf $BACKUPDIR/${BAK}_config.tgz config
