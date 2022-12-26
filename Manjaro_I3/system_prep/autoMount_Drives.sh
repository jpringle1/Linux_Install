# Automount ExtraSSD

# Set new location of drive
sudo mkdir /media/ExtraSSD

# backup fstab
cd /etc/fstab
sudo cp fstab fstab.backup

# append new entry to fstab
echo "UUID=264a4224-6078-4535-afd6-e56e7d8a00e8 /media/ExtraSSD   ext4   defaults 0 0" | sudo tee -a /etc/fstab
echo "UUID=e955d6bb-556d-406b-8d40-f3f0c3e5dc3d /media/Games   ext4   defaults 0 0" | sudo tee -a /etc/fstab



# reload systemctl
systemctl daemon-reload
# mount drive NOW instead of waiting for reboot
sudo mkdir /media/ExtraSSD
sudo mount UUID=264a4224-6078-4535-afd6-e56e7d8a00e8 /media/ExtraSSD

sudo mkdir /media/Games
sudo mount UUID=e955d6bb-556d-406b-8d40-f3f0c3e5dc3d /media/Games
