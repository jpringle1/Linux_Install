#!/bin/bash

controller_directory=$(pwd)

echo "Commencing system_prep scripts"
cd system_prep
echo "executing git_setup"
./git_setup.sh
echo "executing systemGeneral"
./system_ui.sh
echo "executing autoMount_Drives"
./automount_drives.sh
echo "executing symLink_setup"
./symlink_setup.sh $dropbox_directory

cd $controller_directory

echo "Commencing programs scripts"
cd programs
echo "executing Flatpak installs"
./flatpak_installs.sh
echo "executing steam_configure"
./steam_configure.sh $live_configs_directory
echo "executing pacman installs"
./pacman_installs.sh $live_configs_directory
echo "executing dropbox install"
./dropbox.sh

echo "executing yay installs"
./yay_installs.sh

cd $controller_directory
echo "Commencing system_post scripts"
cd system_post
./key_bindings.sh $live_configs_directory
./install_pipewire.sh
./autostart_programs.sh
./timeshift.sh
