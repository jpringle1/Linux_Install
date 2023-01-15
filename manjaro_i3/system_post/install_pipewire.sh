echo "install pipewire"
sudo pacman -Rdd --noconfirm manjaro-pulse pulseaudio pulseaudio-alsa pulseaudio-equalizer pulseaudio-jack pulseaudio-lirc pulseaudio-rtp pulseaudio-zeroconf pulseaudio-bluetooth pulseaudio-ctl sof-firmware

# warning: The previous command will likely return some "cannot find package" results. Ignore and move on to next command.

sudo pacman -S --noconfirm manjaro-pipewire
systemctl --user enable pipewire.socket --now
systemctl --user start pipewire.service

# reboot

