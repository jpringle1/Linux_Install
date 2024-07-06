#!/usr/bin/env python
import yaml, os
from shutil import copyfile

namespace = "/mnt/LinuxSetup/Linux_Install/manjaro_i3/driveMounting/"

def writeToFstabAndMount(newMount, mountPoint):
    with open("/etc/fstab", "a") as fstab:
        fstab.write(newMount+"\n")
    os.rmdir(f'/mnt/{mountPoint}')
    os.mkdir(f'/mnt/{mountPoint}')

def importYaml(filename):
    with open(namespace + filename + ".yaml", 'r') as stream:
        return yaml.safe_load(stream)

drives = importYaml("drives")
config = importYaml("serverConfig")

copyfile(namespace + ".smbcredentials", "/home/joep/.smbcredentials")

for drive in drives["ext4Drives"]:
    newMount = f'UUID={drive["drive"]}    /mnt/{drive["mountPoint"]}    ext4    defaults    0    1'
    writeToFstabAndMount(newMount, drive["mountPoint"])

for drive in drives["cifsDrives"]:
    newMount = f'//{config["serverIp"]}/{drive["drive"]} /mnt/{drive["mountPoint"]} cifs credentials={config["credentials"]},uid=1000,gid=1000 0 0'
    writeToFstabAndMount(newMount, drive["mountPoint"])

for drive in drives["iscsi"]:
    os.popen(f'sudo iscsiadm --mode node --targetname {config["targetName"]} --portal {config["serverIp"]} --login && sudo mkfs.ext4 /dev/{drive["mountPoint"]}')
    newMount = f'/dev/{drive["drive"]} /mnt/{drive["mountPoint"]} ext4 _netdev,rw 0 0'
    writeToFstabAndMount(newMount, drive["mountPoint"])
    
os.popen("systemctl daemon-reload && sudo mount -a")
