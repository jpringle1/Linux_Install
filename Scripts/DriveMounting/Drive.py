from git import Optional
from Enums import DriveType

class Drive:
    def __init__(
            self, 
            drive: str, 
            mountPoint: str, 
            driveType: DriveType, 
            targetName: Optional[str] = None) -> None:
        
        self.drive = drive
        self.mountPoint = mountPoint
        self.driveType = driveType
        self.targetName = targetName

    def __repr__(self) -> str:
        return f"Drive(drive={self.drive}, mountPoint={self.mountPoint}, driveType={self.driveType}, targetName={self.targetName})"