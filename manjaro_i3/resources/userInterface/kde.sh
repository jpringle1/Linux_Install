#!/bin/bash
# KDE
git clone https://github.com/catppuccin/grub.git && cd grub
sudo mkdir /usr/share/grub/themes
sudo cp -r src/* /usr/share/grub/themes/
newThemeSetting='GRUB_THEME="/usr/share/grub/themes/catppuccin-frappe-grub-theme/theme.txt"'
echo $newThemeSetting | sudo tee -a /etc/default/grub
newResolutionSetting="GRUB_GFXMODE=5120x1440"
echo $newResolutionSetting | sudo tee -a /etc/default/grub
sudo grub-mkconfig -o /boot/grub/grub.cfg