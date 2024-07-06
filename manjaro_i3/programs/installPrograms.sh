#!/bin/bash

echo "refreshing database"
sudo dpkg --add-architecture i386 # setup architecture for steam
sudo apt-add-repository contrib non-free-firmware # add community repo
sudo apt -y update && sudo apt -y upgrade # update and upgrade repos and packages
sudo apt -y install gh #install github cli
sudo apt install -y python3 python3-git #install python
git config --global user.email "joe.pringle@proton.me"
git config --global user.name "Joe Pringle"
gh auth login --with-token < myGithubToken.txt #setup github cli
sudo apt -y install flatpak #install flatpak
flatpak remote-add --if-not-exists flathub https://flathub.org/repo/flathub.flatpakrepo # add flathub repo to flatpak

python installPrograms.py #install programs
