#!/bin/bash


#setup symlinks in home directory to link Downloads, Documents, pictures and desktop to dropbox contents

# TODO for each folder, if doesn't already exist in ExtraSSD, create and show warning

dropbox_link_dir=~/Dropbox
pc_files_dir=/"PC files"

ln -s $dropbox_link_dir $dropbox_main_dir

sudo rm -R ~/Pictures && sudo ln -s $dropbox_main_dir$pc_files_dir/Pictures ~/Pictures
sudo rm -R ~/Documents && sudo ln -s $dropbox_main_dir$pc_files_dir/Documents ~/Documents
sudo rm -R ~/Downloads && sudo ln -s $dropbox_main_dir$pc_files_dir/Downloads ~/Downloads
sudo rm -R ~/Desktop && sudo ln -s $dropbox_main_dir$pc_files_dir/Desktop ~/Desktop


