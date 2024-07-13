import json
from Models.Drives.Drive import Drive
from typing import List

class DriveCollection:
    def __init__(self, filepath: str) -> None:
        jsonString = open(filepath)
        config = json.loads(jsonString)
        jsonString.close()
        self.ext4: List[Drive] = []
        self.cifs: List[Drive] = []
        self.iscsi: List[Drive] = []

        for entry in config:
            driveType = entry["driveType"]
            for drive in entry["drives"]:
                if driveType.lower() == "iscsi":
                    driveObj = Drive(drive["drive"], drive["mountPoint"], drive.get("targetName"))
                    self.iscsi.append(driveObj)
                else:
                    driveObj = Drive(drive["drive"], drive["mountPoint"])
                    if driveType.lower() == "ext4":
                        self.ext4.append(driveObj)
                    elif driveType.lower() == "cifs":
                        self.cifs.append(driveObj)

    def __repr__(self) -> str:
        return f"DriveCollection(ext4={self.ext4}, cifs={self.cifs}, iscsi={self.iscsi})"