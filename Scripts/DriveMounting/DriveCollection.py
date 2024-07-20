import json
from typing import List

from Scripts.DriveMounting import Drive, DriveSubprocesses

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
    
    def addFstabEntries(self):
        for drive in self.drives:
            drive.AddFstabEntry()
            self.CreateMountDirectory()

        DriveSubprocesses.systemCtlReload()
        DriveSubprocesses.mount()
