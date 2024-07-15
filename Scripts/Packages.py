import subprocess
import json
from typing import List
from enum import Enum

class Repository(Enum):
    Zypper = 1
    Flatpak = 2

class Package:
    def __init__(
            self, 
            packageName: str, 
            repository: str) -> None:
        
        self.packageName: str = packageName
        self.repository: Repository = Repository[repository]
    
    def __repr__(self) -> str:
        return f"Package(packageName={self.packageName}, repository={self.repository})"
    
    def installPackage(self):
        match self.repository:
            case Repository.Zypper:
                self.zypperInstallPackage(self.packageName)
            case Repository.Flatpak:
                self.flatpakInstallPackage(self.packageName)

    def zypperInstallPackage(self, packageName):
        subprocess.run(["sudo", "zypper", "in", "-y", packageName], check=True)

    def flatpakInstallPackage(self, packageName):
        subprocess.run(["flatpak", "-y", "install", packageName], check=True)
                
class Packages:
    def __init__(
            self, 
            filepath: str) -> None:
        
        with open(filepath, 'r') as file:
            packageLoad = json.load(file)

        self.packages: List[Package] = []

        for entry in packageLoad:
            repository = entry["repository"]
            for package in entry["packages"]:
                packageObj = Package(package, repository)
                self.packages.append(packageObj)

    def installPackages(self):
        for package in self.packages:
            package.installPackage()

    def refreshRepositories(self):
        subprocess.run(["sudo", "zypper", "--gpg-auto-import-keys" ,"ref"], check=True)
