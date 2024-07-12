import os
import Command
import Models

def writeToFstabAndMount(mountString, mountPoint):
    with open("/etc/fstab", "a") as fstab:
        fstab.write(mountString + "\n")

    dir = "/mnt/" + mountPoint
    if os.path.isdir(dir):  
        os.rmdir(dir)
    
    os.mkdir(dir)

def getExt4MountString(drive: Models.Drive):
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

def getCifsMountString(drive: Models.Drive, serverConfig: Models.ServerConfig):
    remoteDrive = f'//{serverConfig.nasIpAddress}/{drive.drive} '
    localMount = f'/mnt/{drive.mountPoint} '
    filetype = "cifs "
    credentialsStr = f'credentials={serverConfig.credentialsDirectory}'
    idStrings = ",uid=1000,gid=1000 0 0"

    return remoteDrive + localMount + filetype + credentialsStr + idStrings

def getIscsiMountString(drive: Models.Drive, serverConfig: Models.ServerConfig):
    Command.IscsiTargetDiscovery(serverConfig.nasIpAddress)
    Command.IscsiLogin(drive.targetName, serverConfig.nasIpAddress)
    return f'/dev/{drive.drive} /mnt/{drive.mountPoint} ext4 _netdev,rw 0 0'

def setupSmbCredentials(config: Models.ServerConfig):
    with open(config.credentialsDirectory, "w") as f:
        f.write(f"username={config.smbUsername}\n")
        f.write(f"password={config.smbPassword}\n")
        f.write(f"domain={config.smbDomain}")

def mountDrives(drives: Models.DriveCollection, serverConfig: Models.ServerConfig):
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