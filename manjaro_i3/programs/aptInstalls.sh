#!/bin/bash

echo "refreshing database"
sudo apt update
sudo apt upgrade

echo "installing flatpak"
sudo apt install flatpak
flatpak remote-add --if-not-exists flathub https://flathub.org/repo/flathub.flatpakrepo