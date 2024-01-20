#!/usr/bin/env python
import yaml, os
from shutil import copyfile

namespace = "/mnt/LinuxSetup/Linux_Install/manjaro_i3/driveMounting/"

with open(namespace + "drives.yaml", 'r') as stream:
    drives = yaml.safe_load(stream)

with open(namespace + "serverConfig.yaml", 'r') as stream:
    config = yaml.safe_load(stream)

copyfile(namespace + ".smbcredentials", "/home/joep/.smbcredentials")

for drive in drives:
    if drive["type"] == "cifs":
        newMount = f'//{config["serverIp"]}/{drive["drive"]} /mnt/{drive["mountPoint"]} cifs credentials={config["credentials"]},uid=1000,gid=1000 0 0'
    elif drive["type"] == "ext4":
        newMount = f'UUID={drive["drive"]}    /mnt/{drive["mountPoint"]}    ext4    defaults    0    1'

    with open("/etc/fstab", "a") as fstab:
        fstab.write(newMount+"\n")
    os.mkdir(f'/mnt/{drive["mountPoint"]}')
    
bashCommands = [
    "sudo apt install cifs-utils",
    "systemctl daemon-reload",
    "mount -a"
    ]

for command in bashCommands:
    commandExecution = os.popen(command)
    print(commandExecution.read())
    print(commandExecution.close())
