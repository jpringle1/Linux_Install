#!/bin/bash

# solaar
# qemu
live_configs_directory=$1
echo "refreshing database"
sudo pacman -Sy --noconfirm

echo "Remove onlyoffice"
sudo pacman -R --noconfirm onlyoffice-desktopeditors plasma-workspace-wallpapers

echo "Updating packages"
sudo pacman -Su --noconfirm


echo "configuring firefox"
rm -R ~/.mozilla
mkdir ~/.mozilla
sudo ln -s $live_configs_directory"/firefox" ~/.mozilla/firefox

echo "installing obsidian"
sudo pacman -S --noconfirm obsidian

echo "install and config virt-manager"
sudo pacman -S --noconfrim virt-manager
sudo pacman -S --noconfirm qemu-full

sudo systemctl enable libvirtd.service
sudo systemctl start libvirtd.service
sudo virsh net-autostart default
sudo virsh net-start default

sudo yay -S --noconfirm
