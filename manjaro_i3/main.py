import os
import Prerequisites
import DriveMounting
import Packages
import SystemLinks

resourcesDir = os.getcwd() + "/resources"

Prerequisites.installAndConfigureGit("git")
DriveMounting.mountDrives("drives", "drives")
Packages.installPackages("packages")
SystemLinks.addAllSymlinks("symlinks")

os.popen(f'sh {resourcesDir}/userInterfaceScripts/kde.sh')
os.popen(f'sh {resourcesDir}/userInterfaceScripts/removeShutdownOptions.sh')
os.popen(f'sh {resourcesDir}/configurations/key_bindings.sh')