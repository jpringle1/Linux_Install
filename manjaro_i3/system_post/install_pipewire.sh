echo "install pipewire"
sudo pacman -Rdd --noconfirm manjaro-pulse
sudo pacman -Rdd --noconfirm pulseaudio
sudo pacman -Rdd --noconfirm pulseaudio-alsa
sudo pacman -Rdd --noconfirm pulseaudio-zeroconf
sudo pacman -Rdd --noconfirm pulseaudio-bluetooth
sudo pacman -Rdd --noconfirm pulseaudio-ctl
sudo pacman -Rdd --noconfirm sof-firmware

# warning: The previous command will likely return some "cannot find package" results. Ignore and move on to next command.
sudo pacman -S --noconfirm pipewire
sudo pacman -S --noconfirm manjaro-pipewire
systemctl --user enable pipewire.socket --now
systemctl --user start pipewire.service

# reboot

