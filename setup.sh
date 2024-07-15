#!/bin/bash

sudo zypper addrepo https://cli.github.com/packages/rpm/gh-cli.repo
sudo zypper ref
sudo zypper in -y gh
source .venv/bin/activate
sudo python3 program.py