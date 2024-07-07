import os
import FileManaging

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
    def getCifsMountString(drive, mountPoint, nasIpAddress):
        return f'//{nasIpAddress["serverIp"]}/{drive} /mnt/{mountPoint} cifs credentials={nasIpAddress["credentials"]},uid=1000,gid=1000 0 0'

    @staticmethod
    def getIscsiMountString(drive, mountPoint, nasIpAddress):
        os.popen(f'sudo iscsiadm --mode node --targetname {nasIpAddress["targetName"]} --portal {nasIpAddress["serverIp"]} --login && sudo mkfs.ext4 /dev/{mountPoint}')
        return f'/dev/{drive} /mnt/{mountPoint} ext4 _netdev,rw 0 0'
    
    @staticmethod
    def setupSmbCredentials(smbcredentials):
        f = open(smbcredentials["location"], "w")
        f.write(f"username={smbcredentials["username"]}\n")
        f.write(f"password={smbcredentials["password"]}\n")
        f.write(f"domain={smbcredentials["domain"]}")
        f.close()

    @classmethod
    def mountDrives(cls, drivesYaml, serverConfig):
        drives = FileManaging.importYaml(drivesYaml)
        serverConfig = FileManaging.importYaml(serverConfig)

        cls.setupSmbCredentials(serverConfig["smbcredentials"])

        for drive in drives["ext4"]:
            mountString = cls.getExt4MountString(drive["drive"], drive["mountpoint"])
            cls.writeToFstabAndMount(mountString, drive["mountpoint"])

        for drive in drives["cifs"]:
            mountString = cls.getCifsMountString(drive["drive"], drive["mountpoint"], serverConfig["nasIpAddress"])
            cls.writeToFstabAndMount(mountString, drive["mountpoint"])

        for drive in drives["iscsi"]:
            mountString = cls.getIscsiMountString(drive["drive"], drive["mountpoint"], serverConfig["nasIpAddress"])
            cls.writeToFstabAndMount(mountString, drive["mountpoint"])
        
        os.popen("systemctl daemon-reload && sudo mount -a")