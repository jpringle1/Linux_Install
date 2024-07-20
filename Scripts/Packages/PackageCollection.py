from typing import List

from Scripts.Git.GitSubprocesses import GitSubprocesses
from Scripts.Models.RepositorySet import RepositorySet
from Scripts.Packages.Package import Package

class PackageCollection:
    def __init__(self, repoSetList: List[RepositorySet]) -> None:
        self.packages: List[Package] = []

        for repoSet in repoSetList:
            for package in repoSet.packages:
                packageObj = Package(package, repoSet.repository)
                self.packages.append(packageObj)

    def installPackages(self):
        for package in self.packages:
            package.installPackage()

    def refreshRepositories(self):
        GitSubprocesses.refreshRepositories()

    def __getitem__(self, index: int) -> Package:
        return self.packages[index]
    
    def __len__(self) -> int:
        return len(self.packages)

    def __str__(self):
        return f"Packages({self.packages})"