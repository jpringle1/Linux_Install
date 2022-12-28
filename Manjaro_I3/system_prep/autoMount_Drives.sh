#!/bin/bash

extraUUID="264a4224-6078-4535-afd6-e56e7d8a00e8"
extraLabel="ExtraSSD"
gamesUUID="e955d6bb-556d-406b-8d40-f3f0c3e5dc3d"
gamesLabel="Games"

sudo mkdir /media/$extraLabel
sudo mkdir /media/$gamesLabel

# backup fstab
fstab_dir=/etc/fstab
cd $fstab_dir
sudo cp fstab fstab.backup

# append new entry to fstab
echo "UUID=$extraUUID /media/$extraLabel   ext4   defaults 0 0" | sudo tee -a $fstab_dir
echo "UUID=$gamesUUID /media/$gamesLabel   ext4   defaults 0 0" | sudo tee -a $fstab_dir

# reload systemctl
systemctl daemon-reload
# mount drive NOW instead of waiting for reboot

sudo mount UUID=$extraUUID /media/$extraLabels
sudo mount UUID=$gamesUUID /media/$gamesLabel
