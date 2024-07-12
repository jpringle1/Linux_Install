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

class Packages:
    def __init__(self, filepath: str) -> None:
        jsonString = open(filepath)
        packages = json.loads(jsonString)
        jsonString.close()
        self.zypper: List[str] = packages["zypper"]
        self.flatpak: List[str] = packages["flatpak"]

class GitConfig:
    def __init__(self, filepath: str) -> None:
        jsonString = open(filepath)
        credentials = json.loads(jsonString)
        jsonString.close()
        self.email: str = credentials["email"]
        self.name: str = credentials["name"]

class SymLink:
    def __init__(self, sourceName: str, destinationName: str) -> None:
        self.sourceName = sourceName
        self.destinationName = destinationName

    def __repr__(self) -> str:
        return f"SymLink(sourceName={self.sourceName}, destinationName={self.destinationName})"

class Directories:
    def __init__(self, sourceDirectory: str, destinationDirectory: str, links: List[SymLink]) -> None:
        self.sourceDirectory = sourceDirectory
        self.destinationDirectory = destinationDirectory
        self.links: List[SymLink] = links

    def __repr__(self) -> str:
        return f"Directories(sourceDirectory={self.sourceDirectory}, destinationDirectory={self.destinationDirectory}, links={self.links})"

class SymLinks:
    def __init__(self, filepath: str) -> None:
        with open(filepath, 'r') as file:
            symLinks = json.load(file)
        
        self.directories: List[Directories] = []
        
        for directory in symLinks:
            links = [SymLink(link["sourceName"], link["destinationName"]) for link in directory["links"]]
            directoryObj = Directories(
                directory["sourceDirectory"], 
                directory["destinationDirectory"], 
                links
            )
            self.directories.append(directoryObj)

    def __repr__(self) -> str:
        return f"SymLinks(directories={self.directories})"
    
    def __getitem__(self, index) -> Directories:
        return self.directories[index]
    

class Sync:
    def __init__(self, program: str, local: str, remote: str) -> None:
        self.program = program
        self.local = local
        self.remote = remote

    def __repr__(self) -> str:
        return f"Sync(program={self.program}, local={self.local}, remote={self.remote})"

class Syncs:
    def __init__(self, filepath: str) -> None:
        with open(filepath, 'r') as file:
            syncs = json.load(file)
        self.syncs: List[Sync] = []
        
        for sync in syncs:
            syncObj = Directories(
                sync["program"], 
                sync["local"], 
                sync["remote"]
            )
            self.syncs.append(syncObj)

    def __repr__(self) -> str:
        return f"Syncs(syncs={self.syncs})"
    
    def __getitem__(self, index) -> Sync:
        return self.syncs[index]    
