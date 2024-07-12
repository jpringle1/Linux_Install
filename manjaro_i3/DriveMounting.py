import os
import FileManaging
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

def getCifsMountString(drive: Models.Drive, credentials, nasIpAddress):
    remoteDrive = f'//{nasIpAddress}/{drive.drive} '
    localMount = f'/mnt/{drive.mountPoint} '
    filetype = "cifs "
    credentialsStr = f'credentials={credentials}'
    idStrings = ",uid=1000,gid=1000 0 0"

    return remoteDrive + localMount + filetype + credentialsStr + idStrings

def getIscsiMountString(drive: Models.Drive, nasIpAddress):
    Command.IscsiTargetDiscovery(nasIpAddress)
    Command.IscsiLogin(drive.targetName, nasIpAddress)
    return f'/dev/{drive.drive} /mnt/{drive.mountPoint} ext4 _netdev,rw 0 0'

def setupSmbCredentials(smbcredentials, credentialLocation):
    with open(credentialLocation, "w") as f:
        f.write(f"username={smbcredentials['username']}\n")
        f.write(f"password={smbcredentials['password']}\n")
        f.write(f"domain={smbcredentials['domain']}")

def mountDrives(drives: Models.DriveCollection, serverConfigYaml):
    serverConfig = FileManaging.importYaml(serverConfigYaml)

    setupSmbCredentials(serverConfig["smbcredentials"], serverConfig["credentialsLocation"])

    for drive in drives.ext4Drives:
        mountString = getExt4MountString(drive)
        writeToFstabAndMount(mountString, drive.mountPoint)

    for drive in drives.cifsDrives:
        mountString = getCifsMountString(drive, serverConfig["credentialsLocation"], serverConfig["nasIpAddress"])
        writeToFstabAndMount(mountString, drive.mountPoint)

    for drive in drives.iscsiDrives:
        mountString = getIscsiMountString(drive, serverConfig["nasIpAddress"])
        writeToFstabAndMount(mountString, drive.mountPoint)
        Command.systemCtlReload()
        Command.fstabMountDrives()