import Command
from Models import Packages

def addRepository():
    print("")

def installPackages(packages: Packages):
    addRepository()
    Command.refreshRepositories()
    for package in packages.zypper:
        Command.zypperInstallPackage(package)
    for package in packages.flatpak:
        Command.flatpakInstallPackage(package)