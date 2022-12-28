#!/bin/bash

# solaar
# qemu

echo "configuring firefox"
config_name=firefox
link_dir_name=.mozilla
full_link_dir=~/$link_dir_name/$config_name
sudo rm -R $full_link_dir && sudo ln -s $dropbox_main_dir$config_source_dir/$config_name $full_link_dir

echo "configuring steam"
link_dir_name=.steam
full_link_dir=~/$link_dir_name

sudo rm -R $full_link_dir && sudo ln -s $dropbox_main_dir$config_source_dir/$config_name $full_link_dir

sudo pacman -S --noconfirm steam
