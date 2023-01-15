#!/bin/bash

#install dropbox daemon
saved_location=$(pwd)

cd ~ && wget -O - "https://www.dropbox.com/download?plat=lnx.x86_64" | tar xzf -

cd $saved_location
#autostart dropbox daemon
sudo cp dropboxd ~/.config/autostart/dropboxd

#run dropbox
./dropboxd &

#add dropbox cli script to path or something
