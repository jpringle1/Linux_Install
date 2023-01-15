#!/bin/bash

# solaar
# qemu
live_configs_directory=$1
echo "refreshing database"
sudo pacman -Syu --noconfirm

echo "configuring firefox"
rm -R ~/.mozilla
mkdir ~/.mozilla
sudo ln -s $live_configs_directory"/firefox" ~/.mozilla/firefox

sudo yay -S --noconfirm
