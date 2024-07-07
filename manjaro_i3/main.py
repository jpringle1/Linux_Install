import os
import Prerequisites
import DriveMounting
import Packages
import SystemLinks

resourcesDir = os.getcwd() + "/resources/"

Prerequisites.installAndConfigureGit(resourcesDir + "git")
DriveMounting.mountDrives(resourcesDir, "drives")
Packages.installPackages(resourcesDir + "packages")
SystemLinks.addAllSymlinks(resourcesDir + "symlinks")

os.popen(f'sh {resourcesDir}scripts/kde.sh')
os.popen(f'sh {resourcesDir}scripts/removeShutdownOptions.sh')
os.popen(f'sh {resourcesDir}scripts/key_bindings.sh')