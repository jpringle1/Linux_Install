import os
import FileManaging
import subprocess

def addRepository():
    print("")

def refreshRepositories():
    subprocess.run(["systemctl", "daemon-reload"], check=True)
    subprocess.run(["sudo", "zypper", "-y", "ref"], check=True)


def installZypperPackage(package):
    subprocess.run(["sudo", "zypper", "-y", "in", package], check=True)

def installFlatpakPackage(package):
    subprocess.run(["flatpak", "-y", "install", package], check=True)

def installPackages(packagesYamlFile):
    packages = FileManaging.importYaml(packagesYamlFile)
    addRepository()
    refreshRepositories()
    for package in packages["zypper"]:
        installZypperPackage(package)
    for package in packages["flatpak"]:
        installFlatpakPackage(package)