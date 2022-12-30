#!/bin/bash

# solaar
# qemu

echo "refreshing database"
sudo pacman -Syu --noconfirm

echo "configuring firefox"
mkdir ~/.mozilla
sudo rm -R ~/.mozilla/firefox
sudo ln -s /media/ExtraSSD/Dropbox/PC_files/Projects/Tech/LiveConfigs/firefox ~/.mozilla/firefox

