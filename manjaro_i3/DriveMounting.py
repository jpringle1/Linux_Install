import os
import FileManaging
import Command

def writeToFstabAndMount(mountString, mountPoint):
    with open("/etc/fstab", "a") as fstab:
        fstab.write(mountString + "\n")

    if os.path.isdir("/mnt/" + mountPoint):  
        os.rmdir(f'/mnt/{mountPoint}')
    
    os.mkdir(f'/mnt/{mountPoint}')

def getExt4MountString(drive, mountPoint):
    fstabOptions = [
        "UUID=" + drive,
        "/mnt/" + mountPoint,
        "ext4",
        "defaults",
        "0",
        "1"
    ]

    fstabEntry = '   '.join(fstabOptions)

    return fstabEntry

def getCifsMountString(drive, mountPoint, credentials, nasIpAddress):
    remoteDrive = f'//{nasIpAddress}/{drive} '
    localMount = f'/mnt/{mountPoint} '
    filetype = "cifs "
    credentialsStr = f'credentials={credentials}'
    idStrings = ",uid=1000,gid=1000 0 0"

    return remoteDrive + localMount + filetype + credentialsStr + idStrings

def getIscsiMountString(drive, mountPoint, nasIpAddress, targetName):
    Command.IscsiTargetDiscovery(nasIpAddress)
    Command.IscsiLogin(targetName, nasIpAddress)
    return f'/dev/{drive} /mnt/{mountPoint} ext4 _netdev,rw 0 0'

def setupSmbCredentials(smbcredentials, credentialLocation):
    with open(credentialLocation, "w") as f:
        f.write(f"username={smbcredentials['username']}\n")
        f.write(f"password={smbcredentials['password']}\n")
        f.write(f"domain={smbcredentials['domain']}")

def mountDrives(drivesYaml, serverConfigYaml):
    drives = FileManaging.importYaml(drivesYaml)
    serverConfig = FileManaging.importYaml(serverConfigYaml)

    setupSmbCredentials(serverConfig["smbcredentials"], serverConfig["credentialsLocation"])

    for drive in drives["ext4"]:
        mountString = getExt4MountString(drive["drive"], drive["mountPoint"])
        writeToFstabAndMount(mountString, drive["mountPoint"])

    for drive in drives["cifs"]:
        mountString = getCifsMountString(drive["drive"], drive["mountPoint"], serverConfig["credentialsLocation"], serverConfig["nasIpAddress"])
        writeToFstabAndMount(mountString, drive["mountPoint"])

    for drive in drives["iscsi"]:
        mountString = getIscsiMountString(drive["drive"], drive["mountPoint"], serverConfig["nasIpAddress"], drive["targetName"])
        writeToFstabAndMount(mountString, drive["mountPoint"])
        Command.systemCtlReload()
        Command.fstabMountDrives()