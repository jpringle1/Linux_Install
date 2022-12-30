#!/bin/bash
config_dir=/configs
config_store=/media/ExtraSSD/Dropbox/PC_files/Projects/Tech/LiveConfigs



echo "commencing configurations"
cd $config_dir
config_source_dir=/PC_files/Projects/Tech/LiveConfigs
echo "configuring dropbox"




echo "configuring obsidian"


flatpak install -y --noninteractive md.obsidian.Obsidian/x86_64/stable #obsidian
flatpak install -y --noninteractive com.dropbox.Client/x86_64/stable #dropbox


# latte
# system monitor
