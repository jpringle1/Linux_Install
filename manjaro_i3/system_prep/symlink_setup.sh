#!/bin/bash

#setup symlinks in home directory to link Downloads, Documents, pictures and desktop to dropbox contents

#dropbox_directory=$1"/PC_files"

echo "creating dropbox link"
sudo rm -R ~/Dropbox
ln -s $1"/PC_files" ~/Dropbox

echo "creating media links"
sudo rm -R ~/Pictures
sudo ln -s $1"/PC_files/Media" ~/Pictures
sudo rm -R ~/Documents
sudo ln -s $1"/PC_files/Documents" ~/Documents
sudo rm -R ~/Downloads
sudo ln -s $1"/PC_files/Downloads" ~/Downloads
sudo rm -R ~/Desktop
sudo ln -s $1"/PC_files/Desktop" ~/Desktop

echo "finished symlink_setup"
