import os
from pyfstab import Fstab, Entry

from Scripts import Command
from Models.Drives import Drive, DriveCollection
from Models.Configs import ServerConfig

def CreateMountDirectory(mountPoint):
    dir = "/mnt/" + mountPoint
    if os.path.isdir(dir):  
        os.rmdir(dir)
    
    os.mkdir(dir)

def AddExt4Entry(fstab: Fstab, drive: Drive):
    fstab.entries.append(
        Entry(
            drive.drive,
            "/mnt/" + drive.mountPoint,
            "ext4",
            "defaults",
            0,
            1
        )
    )

def AddCifsEntry(fstab: Fstab, drive: Drive, serverConfig: ServerConfig):
    fstab.entries.append(
        Entry(
            f'//{serverConfig.nasIpAddress}/{drive.drive}',
            "/mnt/" + {drive.mountPoint},
            "cifs",
            f'credentials={serverConfig.credentialsDirectory},uid=1000,gid=1000',
            0,
            0
        )
    )

def getIscsiMountString(fstab: Fstab, drive: Drive, serverConfig: ServerConfig):
    Command.IscsiTargetDiscovery(serverConfig.nasIpAddress)
    Command.IscsiLogin(drive.targetName, serverConfig.nasIpAddress)

    fstab.entries.append(
        Entry(
            "/dev/" + {drive.drive},
            "/mnt/" + {drive.mountPoint},
            "ext4",
            "_netdev,rw",
            0,
            0
        )
    )

def setupSmbCredentials(config: ServerConfig):
    with open(config.credentialsDirectory, "w") as f:
        f.write(f"username={config.smbUsername}\n")
        f.write(f"password={config.smbPassword}\n")
        f.write(f"domain={config.smbDomain}")

def mountDrives(drives: DriveCollection, serverConfig: ServerConfig):
    setupSmbCredentials(serverConfig)

    for drive in drives.ext4:
        AddExt4Entry(drive)
        CreateMountDirectory(drive.mountPoint)

    for drive in drives.cifs:
        AddCifsEntry(drive, serverConfig)
        CreateMountDirectory(drive.mountPoint)

    for drive in drives.iscsi:
        getIscsiMountString(drive, serverConfig)
        CreateMountDirectory(drive.mountPoint)
        Command.systemCtlReload()
    
    Command.fstabMountDrives()