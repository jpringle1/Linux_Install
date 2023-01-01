#!/bin/bash
config_dir="configs"
config_store=$dropbox_directory"/PC_files/Projects/Tech/LiveConfigs"

echo "commencing configurations"
echo "configuring dropbox"
echo "configuring obsidian"
flatpak install -y --noninteractive md.obsidian.Obsidian/x86_64/stable #obsidian
flatpak install -y --noninteractive com.dropbox.Client/x86_64/stable #dropbox
# latte
# system monitor
