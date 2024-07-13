from typing import Optional

class Drive:
    def __init__(self, drive: str, mountPoint: str, targetName: Optional[str] = None) -> None:
        self.drive = drive
        self.mountPoint = mountPoint
        self.targetName = targetName

    def __repr__(self) -> str:
        return f"Drive(drive={self.drive}, mountPoint={self.mountPoint}, targetName={self.targetName})"