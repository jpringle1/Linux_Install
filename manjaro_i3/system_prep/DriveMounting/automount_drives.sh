#!/bin/bash

extraUUID="264a4224-6078-4535-afd6-e56e7d8a00e8"
extraLabel="ExtraSSD"
gamesUUID="e955d6bb-556d-406b-8d40-f3f0c3e5dc3d"
gamesLabel="Games"

sudo mkdir -p "/media/"$extraLabel
sudo mkdir -p "/media/"$gamesLabel

# backup fstab

cd /etc
sudo cp fstab fstab.backup

# append new entry to fstab
echo "UUID=$extraUUID /media/$extraLabel   ext4   defaults 0 0" | sudo tee -a /etc/fstab
echo "UUID=$gamesUUID /media/$gamesLabel   ext4   defaults 0 0" | sudo tee -a /etc/fstab

# reload systemctl
systemctl daemon-reload

# mount drive NOW instead of waiting for reboot

sudo mount UUID=$extraUUID /media/$extraLabel
sudo mount UUID=$gamesUUID /media/$gamesLabel



echo "finished"
