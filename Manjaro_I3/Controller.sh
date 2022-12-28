#!/bin/bash

dropbox_main_dir=/media/ExtraSSD/Dropbox


echo "Commencing system_prep scripts"
cd system_prep
directory=pwd
echo pwd

echo "executing systemGeneral"
./systemGeneral.sh
echo "executing autoMount_Drives"
#./autoMount_Drives.sh
echo "executing symLink_setup"
./symLink_setup.sh

cd ..
echo "Commencing programs scripts"
cd programs
directory=pwd
echo "Directory: $pwd"
echo "executing Flatpak installs"
./flatpak_installs.sh
echo "executing pacman installs"
./pacman_installs.sh
echo "executing yay installs"
./yay_installs.sh

echo "Commencing system_post scripts"
cd ..
cd system_post
directory=pwd
echo "Directory: $pwd"
./key_bindings.sh
./install_pipewire.sh
./setup_autostart.sh
./shortcut_setup.sh
./timeshift_setup.sh






