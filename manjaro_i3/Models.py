import json
from typing import List, Optional

class Drive:
    def __init__(self, drive: str, mountPoint: str, targetName: Optional[str] = None) -> None:
        self.drive = drive
        self.mountPoint = mountPoint
        self.targetName = targetName

    def __repr__(self) -> str:
        return f"Drive(drive={self.drive}, mountPoint={self.mountPoint}, targetName={self.targetName})"

class DriveCollection:
    def __init__(self, filepath: str) -> None:
        jsonString = open(filepath)
        config = json.loads(jsonString)
        jsonString.close()
        self.ext4Drives: List[Drive] = []
        self.cifsDrives: List[Drive] = []
        self.iscsiDrives: List[Drive] = []

        for entry in config:
            driveType = entry["driveType"]
            for drive in entry["drives"]:
                if driveType.lower() == "iscsi":
                    driveObj = Drive(drive["drive"], drive["mountPoint"], drive.get("targetName"))
                    self.iscsiDrives.append(driveObj)
                else:
                    driveObj = Drive(drive["drive"], drive["mountPoint"])
                    if driveType.lower() == "ext4":
                        self.ext4Drives.append(driveObj)
                    elif driveType.lower() == "cifs":
                        self.cifsDrives.append(driveObj)

    def __repr__(self) -> str:
        return f"DriveCollection(ext4Drives={self.ext4Drives}, cifsDrives={self.cifsDrives}, iscsiDrives={self.iscsiDrives})"
    
class ServerConfig:
    def __init__(self, filepath: str) -> None:
        jsonString = open(filepath)
        config = json.loads(jsonString)
        jsonString.close()
        self.smbUsername: str = config["smbUsername"]
        self.smbPassword: str = config["smbPassword"]
        self.smbDomain: str = config["smbDomain"]
        self.nasIpAddress: str = config["nasIpAddress"]
        self.credentialsDirectory: str = config["credentialsDirectory"]
