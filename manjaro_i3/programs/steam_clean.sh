#!/bin/bash

sudo rm -R ~/.local/share/Steam
sudo rm -R ~/.steam
sudo rm -R ~/.steampath
sudo rm -R ~/.steampid
sudo pacman -R steam --noconfirm
