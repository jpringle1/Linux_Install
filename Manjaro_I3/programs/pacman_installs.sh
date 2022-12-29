#!/bin/bash

# solaar
# qemu

echo "refreshing database"
sudo pacman -Syu --noconfirm

echo "configuring firefox"
mkdir ~/.mozilla
sudo rm -R ~/.mozilla/firefox
sudo ln -s /media/ExtraSSD/Dropbox/"PC files"/Projects/Tech/LiveConfigs/firefox ~/.mozilla/firefox

echo "configuring steam"
sudo rm -R ~/.steam
sudo ln -s /media/ExtraSSD/Dropbox/"PC files"/Projects/Tech/LiveConfigs/steam/.steam ~/.steam
mkdir ~/.local
mkdir ~/.local/share
sudo ln -s /media/ExtraSSD/Dropbox/"PC files"/Projects/Tech/LiveConfigs/steam/.local/share/Steam ~/.local/share/Steam

sudo pacman -S --noconfirm steam
