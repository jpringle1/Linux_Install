#!/bin/bash

steam_live_config_dir=$1"/steam"
echo "steam_live_config_dir = $steam_live_config_dir"
steam_dir="/home/joep/.local/share/Steam"
userdata_dir="/userdata/171680367"

directory_store=(
    "/config"
    "/compatibilitytools.d"
    "$userdata_dir/config"
    "$userdata_dir/7/remote"
)

echo "directory_store = $directory_store"

for item in ${directory_store[@]}
do
    store_link=$steam_dir$item
    store_source=$steam_live_config_dir$item
    mkdir -p $store_link
    echo "remove "$store_link
    sudo rm -R $store_link
    echo "create link in $store_source pointing to $store_link"
    sudo ln -s $store_source $store_link
done


