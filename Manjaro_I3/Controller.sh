#!/bin/bash

dropbox_directory="/media/ExtraSSD/Dropbox"
controller_directory=$(pwd)
live_configs_directory=$dropbox_directory"/PC_files/Projects/Tech/LiveConfigs"

echo "Commencing system_prep scripts"
cd system_prep
echo "executing systemGeneral"
./system_ui.sh
echo "executing autoMount_Drives"
#./automount_drives.sh
echo "executing symLink_setup"
./symlink_setup.sh $dropbox_directory

cd $controller_directory

echo "Commencing programs scripts"
cd programs
echo "executing Flatpak installs"
./flatpak_installs.sh
echo "executing pacman installs"
./pacman_installs.sh $live_configs_directory

./steam_configure.sh $live_configs_directory
echo "executing yay installs"
./yay_installs.sh

cd $controller_directory
echo "Commencing system_post scripts"
cd system_post
./key_bindings.sh $live_configs_directory
./install_pipewire.sh
./autostart_programs.sh
./timeshift.sh
