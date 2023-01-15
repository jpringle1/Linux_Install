#!/bin/bash

sudo rm -R /var/lib/bluetooth
sudo ln -s $1"/bluetooth" /var/lib/bluetooth
