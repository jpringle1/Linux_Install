from typing import List

from Models.DriveSet import DriveSet
from Scripts.DriveMounting import Drive, DriveSubprocesses

class DriveCollection:
    def __init__(
            self, 
            driveSets: List[DriveSet]) -> None:
        
        self.drives: List[Drive] = []

        for driveSet in driveSets:
            for driveModel in driveSet.drives:
                driveObj = Drive(
                    driveModel.drive, 
                    driveModel.mountPoint, 
                    driveSet.driveType,
                    driveModel.targetName)
                self.drives.append(driveObj)

    def __repr__(self) -> str:
        return f"DriveCollection(drives={self.drives})"
    
    def addFstabEntries(self):
        for drive in self.drives:
            drive.AddFstabEntry()
            self.CreateMountDirectory()

        DriveSubprocesses.systemCtlReload()
        DriveSubprocesses.mount()
