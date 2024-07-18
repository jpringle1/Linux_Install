import subprocess
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
                Subprocesses.zypperInstallPackage(self.packageName)
            case Repository.Flatpak:
                Subprocesses.flatpakInstallPackage(self.packageName)
                
class Packages:
    def __init__(self, json_data: List[dict]) -> None:
        self.packages: List[Package] = []

        for entry in json_data:
            repository = entry["repository"]
            for package in entry["packages"]:
                packageObj = Package(package, repository)
                self.packages.append(packageObj)

    def installPackages(self):
        for package in self.packages:
            package.installPackage()

    def refreshRepositories(self):
        Subprocesses.refreshRepositories()

    def __getitem__(self, index: int) -> Package:
        return self.packages[index]

    def __len__(self) -> int:
        return len(self.packages)

    def __str__(self):
        return f"Packages({self.packages})"

class Subprocesses:
    def zypperInstallPackage(self, packageName):
        subprocess.run(["sudo", "zypper", "in", "-y", packageName], check=True)

    def flatpakInstallPackage(self, packageName):
        subprocess.run(["flatpak", "-y", "install", packageName], check=True)

    def refreshRepositories(self):
        subprocess.run(["sudo", "zypper", "--gpg-auto-import-keys", "ref"], check=True)