#!/bin/bash

# solaar
# qemu
live_configs_directory=$1
echo "refreshing database"
sudo pacman -Sy --noconfirm

echo "Updating packages"
sudo pacman -Su --noconfirm

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
