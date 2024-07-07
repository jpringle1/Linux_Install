import yaml, os
from pathlib import Path
from shutil import copyfile

cwd = os.getcwd()

class FileManaging:
    @staticmethod
    def importYaml(fileName, directory):
        with open(cwd + directory + fileName + ".yaml", 'r') as stream:
            return yaml.safe_load(stream)

class DriveMounting:
    @staticmethod
    def writeToFstabAndMount(mountString, mountPoint):
        with open("/etc/fstab", "a") as fstab:
            fstab.write(mountString + "\n")
        os.rmdir(f'/mnt/{mountPoint}')
        os.mkdir(f'/mnt/{mountPoint}')

    @staticmethod
    def getExt4MountString(drive, mountPoint):
        return f'UUID={drive}    /mnt/{mountPoint}    ext4    defaults    0    1'

    @staticmethod
    def getCifsMountString(drive, mountPoint, serverConfig):
        return f'//{serverConfig["serverIp"]}/{drive} /mnt/{mountPoint} cifs credentials={serverConfig["credentials"]},uid=1000,gid=1000 0 0'

    @staticmethod
    def getIscsiMountString(drive, mountPoint, serverConfig):
        os.popen(f'sudo iscsiadm --mode node --targetname {serverConfig["targetName"]} --portal {serverConfig["serverIp"]} --login && sudo mkfs.ext4 /dev/{mountPoint}')
        return f'/dev/{drive} /mnt/{mountPoint} ext4 _netdev,rw 0 0'
    
    @classmethod
    def mountDrives(cls, drivesYaml):
        drives = FileManaging.importYaml(drivesYaml)
        
        copyfile(cwd + "/driveMounting/.smbcredentials", "/home/joep/.smbcredentials")

        for drive in drives["ext4"]:
            mountString = cls.getExt4MountString(drive["drive"], drive["mountpoint"])
            cls.writeToFstabAndMount(mountString, drive["mountpoint"])

        for drive in drives["cifs"]:
            mountString = cls.getCifsMountString(drive["drive"], drive["mountpoint"])
            cls.writeToFstabAndMount(mountString, drive["mountpoint"])

        for drive in drives["iscsi"]:
            mountString = cls.getIscsiMountString(drive["drive"], drive["mountpoint"])
            cls.writeToFstabAndMount(mountString, drive["mountpoint"])
        
        os.popen("systemctl daemon-reload && sudo mount -a")



class Packages:

class SystemLinks:

class FolderSyncing:

class UserInterface:

class Configurations: