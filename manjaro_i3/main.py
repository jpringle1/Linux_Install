import os
import Prerequisites
import DriveMounting
import Packages
import SystemLinks

resourcesDir = os.getcwd() + "/resources/"

Prerequisites.installAndConfigureGit(resourcesDir + "git")
DriveMounting.mountDrives(resourcesDir + "drives", resourcesDir + "serverConfig")
Packages.installPackages(resourcesDir + "packages")
SystemLinks.addAllSymlinks(resourcesDir + "symlinks")