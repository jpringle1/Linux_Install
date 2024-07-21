import os
from pyfstab import Entry
from Enums import DriveType
from Scripts.ServerConfig import ServerConfig

class Drive:
    def __init__(
            self,
            serverConfig: ServerConfig, 
            drive: str, 
            mountPoint: str, 
            driveType: DriveType, 
            targetName: str = None) -> None:
        
        self.drive = drive
        self.mountPoint = mountPoint
        self.driveType = driveType
        self.targetName = targetName
        self.serverConfig = serverConfig
        self.fstabEntry: str = self._GetFstabEntry()

    def __repr__(self) -> str:
        return f"Drive(drive={self.drive}, mountPoint={self.mountPoint}, driveType={self.driveType}, targetName={self.targetName})"
    
    def _GetExt4Entry(self):
        self.fstabEntry = Entry(
                    self.drive,
                    "/mnt/" + self.mountPoint,
                    "ext4",
                    "defaults",
                    0,
                    1
                )
        
    def _GetCifsEntry(self):
        self.fstabEntry = Entry(
                    f'//{self.serverConfig.nasIpAddress}/{self.drive}',
                    "/mnt/" + self.mountPoint,
                    "cifs",
                    f'credentials={self.serverConfig.credentialsDirectory},uid=1000,gid=1000',
                    0,
                    0
                )
        
    def _GetIscsiEntry(self):
        self.IscsiTargetDiscovery(self.serverConfig.nasIpAddress)
        self.IscsiLogin(self.drive.targetName, self.serverConfig.nasIpAddress)

        self.fstabEntry = Entry(
                    "/dev/" + self.drive,
                    "/mnt/" + self.mountPoint,
                    "ext4",
                    "_netdev,rw",
                    0,
                    0
                )

    def _GetFstabEntry(self):
        match self.driveType:
            case DriveType.Ext4:
                self._GetExt4Entry()
            case DriveType.Cifs:
                self._GetCifsEntry()
            case DriveType.Iscsi:
                self._GetIscsiEntry()
            
    def CreateMountDirectory(self):
        dir = "/mnt/" + self.mountPoint
        if os.path.isdir(dir):  
            os.rmdir(dir)
        
        os.mkdir(dir)

    def AddFstabEntry(self):
        with open("/etc/fstab", 'a') as fstab_file:
            fstab_file.write(self.fstabEntry + '\n')