#!/bin/bash


dropbox_directory="/media/ExtraSSD/Dropbox"
controller_directory=$(pwd)
live_configs_directory=$dropbox_directory"/PC_files/Projects/Tech/LiveConfigs"
cd $controller_directory
cd programs

./steam_configure.sh $live_configs_directory
