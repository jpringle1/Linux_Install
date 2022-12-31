#!/bin/bash

echo "configuring steam"
remote_link=~/.local/share/Steam/userdata/171680367/7/remote
userdata_config_link=~/.local/share/Steam/userdata/171680367/config
config_link=~/.local/share/Steam/config
compatd_link=~/.local/share/Steam/compatibilitytools.d

remote_dir=/media/ExtraSSD/Dropbox/PC_files/Projects/Tech/LiveConfigs/steam/remote
userdata_config_dir=/media/ExtraSSD/Dropbox/PC_files/Projects/Tech/LiveConfigs/steam/userdata/config
config_dir=/media/ExtraSSD/Dropbox/PC_files/Projects/Tech/LiveConfigs/steam/config
compatd_dir=/media/ExtraSSD/Dropbox/PC_files/Projects/Tech/LiveConfigs/steam/compatibilitytools.d

mkdir -p $remote_link
mkdir -p $userdata_config_link
mkdir -p $config_link
mkdir -p $compatd_link

sudo rm -R $remote_link
sudo rm -R $userdata_config_link
sudo rm -R $config_link
sudo rm -R $compatd_link

sudo ln -s $remote_dir $remote_link
sudo ln -s $userdata_config_dir $userdata_config_link
sudo ln -s $config_dir $config_link
sudo ln -s $compatd_dir $compatd_link

sudo pacman -S --noconfirm steam

