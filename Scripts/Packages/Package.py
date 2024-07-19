from Scripts.Enums.Repository import Repository
from Scripts.Packages.PackageSubprocesses import PackageSubprocesses

class Package:
    def __init__(
            self, 
            packageName: str, 
            repository: Repository) -> None:
        
        self.packageName: str = packageName
        self.repository: Repository = repository
    
    def __repr__(self) -> str:
        return f"Package(packageName={self.packageName}, repository={self.repository})"

    def installPackage(self):
        match self.repository:
            case Repository.Zypper:
                PackageSubprocesses.zypperInstallPackage(self.packageName)
            case Repository.Flatpak:
                PackageSubprocesses.flatpakInstallPackage(self.packageName)