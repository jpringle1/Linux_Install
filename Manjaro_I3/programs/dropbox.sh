#!/bin/bash

#install dropbox daemon
cd ~ && wget -O - "https://www.dropbox.com/download?plat=lnx.x86_64" | tar xzf -

#run daemon on startup
sudo cp resources/dropboxd_desktop_entry ~/.config/autostart/dropboxd.desktop

#add dropbox cli script to path or something
