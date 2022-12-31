#!/bin/bash

echo "configuring steam"
remote_link=~/.local/share/Steam/userdata/171680367/7/remote
config_shared_link=~/.local/share/Steam/userdata/171680367/config
config_link=~/.local/share/Steam/config
compatd_link=~/.local/share/Steam/compatibilitytools.d


mkdir -p $remote_link
mkdir -p $config_shared_link
mkdir -p $config_link


config_dir=/media/ExtraSSD/Dropbox/PC_files/Projects/Tech/LiveConfigs/steam/config.vdf
config_link=~/.local/share/Steam/config/config.vdf

libraryfolders_dir=/media/ExtraSSD/Dropbox/PC_files/Projects/Tech/LiveConfigs/steam/libraryfolders.vdf
libraryfolders_link=~/.local/share/Steam/config/libraryfolders.vdf

localconfig_dir=/media/ExtraSSD/Dropbox/PC_files/Projects/Tech/LiveConfigs/steam/localconfig.vdf
localconfig_link=~/.local/share/Steam/userdata/171680367/config/localconfig.vdf

sharedconfig_dir=/media/ExtraSSD/Dropbox/PC_files/Projects/Tech/LiveConfigs/steam/sharedconfig.vdf
sharedconfig_link=~/.local/share/Steam/userdata/171680367/7/remote/sharedconfig.vdf

compatd_source=/media/ExtraSSD/Dropbox/PC_files/Projects/Tech/LiveConfigs/steam/compatibilitytools.d

sudo rm -R $config_link
sudo ln -s $config_dir $config_link
sudo rm -R $libraryfolders_link
sudo ln -s $libraryfolders_dir $libraryfolders_link
sudo rm -R $localconfig_link
sudo ln -s $localconfig_dir $localconfig_link
sudo rm -R $sharedconfig_link
sudo ln -s $sharedconfig_dir $sharedconfig_link
sudo rm -R $compatd_link
sudo ln -s $compatd_source $compatd_link

sudo pacman -S --noconfirm steam

