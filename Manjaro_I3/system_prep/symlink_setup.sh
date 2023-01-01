#!/bin/bash

#setup symlinks in home directory to link Downloads, Documents, pictures and desktop to dropbox contents

link_dir="~/Dropbox/PC_files"
media_parent_dir="~/Dropbox/PC_files"

echo "creating dropbox link"
ln -s $dropbox_directory ~/Dropbox

echo "creating media links"
sudo rm -R ~/Pictures
sudo ln -s $media_parent_dir"/Pictures" ~/Pictures
sudo rm -R ~/Documents
sudo ln -s $media_parent_dir"/Documents" ~/Documents
sudo rm -R ~/Downloads
sudo ln -s $media_parent_dir"/Downloads" ~/Downloads
sudo rm -R ~/Desktop
sudo ln -s $media_parent_dir"/Desktop" ~/Desktop

echo "finished symlink_setup"
