#!/bin/bash

BOB_MEMS_ASSETS_DIR=/home/vagrant/sites/bob/app/static/img/bob_mems

#iterate over files in doah-gpx
for filename in bob-mems/*; do
    #check if this file exists in the app's assets folder on server
    FILE_PATH_TO_CHECK="$BOB_MEMS_ASSETS_DIR/${filename##*/}" #deletes longest match of '*/' from front of $filename.

    #q flag means quiet, suppresses warnings etc.
    ssh -q Vagrant [[ -f $FILE_PATH_TO_CHECK ]] && 
    (echo "$filename already on server") ||
    (echo "$filename not found on server, copying..."; 
    scp -r -i ~/Documents/bob/.vagrant/machines/default/virtualbox/private_key $filename vagrant@10.0.0.105:$BOB_MEMS_ASSETS_DIR);
done