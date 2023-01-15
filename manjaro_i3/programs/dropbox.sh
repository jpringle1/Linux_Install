#!/bin/bash

#install dropbox daemon
cd ~ && wget -O - "https://www.dropbox.com/download?plat=lnx.x86_64" | tar xzf -

#autostart dropbox daemon
sudo cp resources/dropboxd ~/.config/autostart/dropboxd
#run dropbox
cd resources
./dropboxd
cd ..

#add dropbox cli script to path or something
