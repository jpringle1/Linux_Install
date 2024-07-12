import FileManaging
import subprocess
import Command

def addRepository():
    print("")

def installPackages(packagesYamlFile):
    packages = FileManaging.importYaml(packagesYamlFile)
    addRepository()
    Command.refreshRepositories()
    for package in packages["zypper"]:
        Command.zypperInstallPackage(package)
    for package in packages["flatpak"]:
        Command.flatpakInstallPackage(package)