#!/bin/bash
dropbox_main_dir=/media/ExtraSSD/Dropbox

#setup symlinks in home directory to link Downloads, Documents, pictures and desktop to dropbox contents

# TODO for each folder, if doesn't already exist in ExtraSSD, create and show warning

link_dir=~/Dropbox/"PC files"


ln -s $dropbox_main_dir ~/Dropbox

sudo rm -R ~/Pictures
sudo ln -s ~/Dropbox/"PC files"/Pictures ~/Pictures
sudo rm -R ~/Documents
sudo ln -s ~/Dropbox/"PC files"/Documents ~/Documents
sudo rm -R ~/Downloads
sudo ln -s ~/Dropbox/"PC files"/Downloads ~/Downloads
sudo rm -R ~/Desktop
sudo ln -s ~/Dropbox/"PC files"/Desktop ~/Desktop


