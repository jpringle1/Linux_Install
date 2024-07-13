import Command
from models import Packages

def addRepository():
    print("")

def installPackages(packages: Packages):
    addRepository()
    Command.refreshRepositories()
    for package in packages.zypper:
        Command.zypperInstallPackage(package)
    for package in packages.flatpak:
        Command.flatpakInstallPackage(package)