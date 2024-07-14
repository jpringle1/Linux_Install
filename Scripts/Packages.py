import subprocess
import json
from typing import List
from enum import Enum

class Repository(Enum):
    Zypper = 1,
    Flatpak = 2

class Package:
    def __init__(
            self, 
            packageName: str, 
            repository: Repository) -> None:
        
        self.packageName: str = packageName
        self.repository: str = repository
    
    def __repr__(self) -> str:
        return f"Package(packageName={self.packageName}, repository={self.repository})"

class Packages:
    def __init__(
            self, 
            filepath: str) -> None:
        
        jsonString = open(filepath)
        packages = json.loads(jsonString)
        jsonString.close()

        self.packages: List[Package] = []

        for entry in packages:
            repository = entry["repository"]
            for package in entry:
                packageObj = Package(package, repository)
                self.packages.append(packageObj)

    def installPackages(self):
        for package in self.packages:
            match package.repository:
                case Repository.Repository.Zypper:
                    self.zypperInstallPackage(package)
                case Repository.Repository.Flatpak:
                    self.flatpakInstallPackage(package)

    def refreshRepositories():
        subprocess.run(["sudo", "zypper", "--gpg-auto-import-keys" ,"ref"], check=True)

    def zypperInstallPackage(package):
        subprocess.run(["sudo", "zypper", "in", "-y", package], check=True)

    def flatpakInstallPackage(package):
        subprocess.run(["flatpak", "-y", "install", package], check=True)
