import json
import os
import subprocess
from pyfstab import Fstab, Entry
from typing import List

from Scripts import ServerConfig
from Enums import DriveType
from Scripts.DriveMounting import Drive

class DriveCollection:
    def __init__(
            self, 
            filepath: str) -> None:
        
        jsonString = open(filepath + ".json")
        config = json.loads(jsonString)
        jsonString.close()
        
        self.drives: List[Drive] = []

        for entry in config:
            driveType = entry["driveType"]
            for drive in entry["drives"]:
                driveObj = Drive(
                    drive["drive"], 
                    drive["mountPoint"], 
                    drive[driveType],
                    drive.get("targetName"))
                self.drives.append(driveObj)

    def __repr__(self) -> str:
        return f"DriveCollection(drives={self.drives})"
    
    def addFstabEntries(self, serverConfig: ServerConfig):
        for drive in self.drives:
            match drive.driveType:
                case DriveType.DriveType.Ext4:
                    self.AddExt4Entry(drive)
                case DriveType.DriveType.Cifs:
                    self.AddCifsEntry(drive, serverConfig)
                case DriveType.DriveType.Iscsi:
                    self.AddIscsiEntry(drive, serverConfig)

            self.CreateMountDirectory(drive.mountPoint)
            self.systemCtlReload()
        
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

    def AddIscsiEntry(self, fstab: Fstab, drive: Drive, serverConfig: ServerConfig):
        self.IscsiTargetDiscovery(serverConfig.nasIpAddress)
        self.IscsiLogin(drive.targetName, serverConfig.nasIpAddress)

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

    def CreateMountDirectory(mountPoint):
        dir = "/mnt/" + mountPoint
        if os.path.isdir(dir):  
            os.rmdir(dir)
        
        os.mkdir(dir)