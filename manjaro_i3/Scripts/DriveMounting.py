import os
import Command
from Models.Drives import Drive, DriveCollection
from Models.Configs import ServerConfig

def writeToFstabAndMount(mountString, mountPoint):
    with open("/etc/fstab", "a") as fstab:
        fstab.write(mountString + "\n")

    dir = "/mnt/" + mountPoint
    if os.path.isdir(dir):  
        os.rmdir(dir)
    
    os.mkdir(dir)

def getExt4MountString(drive: Drive):
    fstabOptions = [
        "UUID=" + drive.drive,
        "/mnt/" + drive.mountPoint,
        "ext4",
        "defaults",
        "0",
        "1"
    ]

    fstabEntry = '   '.join(fstabOptions)

    return fstabEntry

def getCifsMountString(drive: Drive, serverConfig: ServerConfig):
    remoteDrive = f'//{serverConfig.nasIpAddress}/{drive.drive} '
    localMount = f'/mnt/{drive.mountPoint} '
    filetype = "cifs "
    credentialsStr = f'credentials={serverConfig.credentialsDirectory}'
    idStrings = ",uid=1000,gid=1000 0 0"

    return remoteDrive + localMount + filetype + credentialsStr + idStrings

def getIscsiMountString(drive: Drive, serverConfig: ServerConfig):
    Command.IscsiTargetDiscovery(serverConfig.nasIpAddress)
    Command.IscsiLogin(drive.targetName, serverConfig.nasIpAddress)
    return f'/dev/{drive.drive} /mnt/{drive.mountPoint} ext4 _netdev,rw 0 0'

def setupSmbCredentials(config:ServerConfig):
    with open(config.credentialsDirectory, "w") as f:
        f.write(f"username={config.smbUsername}\n")
        f.write(f"password={config.smbPassword}\n")
        f.write(f"domain={config.smbDomain}")

def mountDrives(drives: DriveCollection, serverConfig: ServerConfig):
    setupSmbCredentials(serverConfig)

    for drive in drives.ext4Drives:
        mountString = getExt4MountString(drive)
        writeToFstabAndMount(mountString, drive.mountPoint)

    for drive in drives.cifsDrives:
        mountString = getCifsMountString(drive, serverConfig)
        writeToFstabAndMount(mountString, drive.mountPoint)

    for drive in drives.iscsiDrives:
        mountString = getIscsiMountString(drive, serverConfig)
        writeToFstabAndMount(mountString, drive.mountPoint)
        Command.systemCtlReload()
        Command.fstabMountDrives()