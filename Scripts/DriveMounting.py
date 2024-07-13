import os
from pyfstab import Fstab, Entry

from Scripts import Command, ConfigWriter
from Models.Drives import Drive, DriveCollection
from Models.Configs import ConfigOptions, ServerConfig

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

def mountDrives(drives: DriveCollection, serverConfig: ServerConfig):
    ConfigWriter.SetOptions(ConfigOptions.ConfigOptions("Resources/smbConfig"))

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