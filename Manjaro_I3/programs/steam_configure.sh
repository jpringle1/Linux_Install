#!/bin/bash

steam_dir="~/.local/share/Steam"
userdata_dir="/userdata/171680367"
steam_live_config_dir=$live_configs_directory"/steam"

echo "configuring steam"
dir_1="/7/remote"
dir_2="/config"
dir_3="/config"
dir_4="/compatibilitytools.d"

dir_1_target=$steam_dir$userdata_dir$dir_1
dir_2_target=$steam_dir$userdata_dir$dir_2
dir_3_target=$steam_dir$dir_3
dir_4_target=$steam_dir$dir_4

dir_1_source=$steam_live_config_dir$dir_1
dir_2_source=$steam_live_config_dir$dir_2
dir_3_source=$steam_live_config_dir$dir_3
dir_4_source=$steam_live_config_dir$dir_4

mkdir -p $dir_1_target
mkdir -p $dir_2_target
mkdir -p $dir_3_target
mkdir -p $dir_4_target

sudo rm -R $dir_1_target
sudo rm -R $dir_2_target
sudo rm -R $dir_3_target
sudo rm -R $dir_4_target

sudo ln -s $dir_1_source $dir_1_target
sudo ln -s $dir_2_source $dir_2_target
sudo ln -s $dir_3_source $dir_3_target
sudo ln -s $dir_4_source $dir_4_target

sudo pacman -S --noconfirm steam
