#!/bin/bash
#remove shutdown options
insertText="offerShutdown=false"
var=$(grep -n "\[General\]" ksmserverrc | cut -f1 -d:)
var=$((var+1))
sed -i "${var}i ${insertText}" ~/.config/ksmserverrc

# Remove autologout

insertText="Autolock=false"
var=$(grep -n "\[Daemon\]" kscreenlockerrc | cut -f1 -d:)
var=$((var+1))
sed -i "${var}i ${insertText}" ~/.config/kscreenlockerrc

# KDE
git clone https://github.com/catppuccin/grub.git && cd grub
sudo mkdir /usr/share/grub/themes
sudo cp -r src/* /usr/share/grub/themes/
newThemeSetting='GRUB_THEME="/usr/share/grub/themes/catppuccin-frappe-grub-theme/theme.txt"'
echo $newThemeSetting | sudo tee -a /etc/default/grub
newResolutionSetting="GRUB_GFXMODE=5120x1440"
echo $newResolutionSetting | sudo tee -a /etc/default/grub
sudo grub-mkconfig -o /boot/grub/grub.cfg

# GRUB
# Splash Screen
# Login Screen
# Konsole