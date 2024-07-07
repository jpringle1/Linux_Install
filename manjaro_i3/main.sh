#!/bin/bash

sudo zypper addrepo https://cli.github.com/packages/rpm/gh-cli.repo
sudo zypper ref
sudo zypper in -y gh
sudo zypper in -y python311-PyYAML
sudo python3 main.py