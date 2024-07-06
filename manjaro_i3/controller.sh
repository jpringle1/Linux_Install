#!/bin/bash

# controller_directory=$(pwd)

su - #TODO: make so the next lines run automatically after entering root user
sudo usermod -aG sudo joep
su joep

sudo apt install pip
sudo apt install python3-yaml

sudo python3 controller.py
