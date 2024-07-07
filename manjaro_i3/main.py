import os
import Prerequisites
import DriveMounting
import Packages
import SystemLinks

resourcesDir = os.getcwd() + "/resources"

Prerequisites.installAndConfigureGit("git", "gitConfig", "myGithubToken.txt")
DriveMounting.mountDrives("drives", "drives")
Packages.installPackages("packages")
SystemLinks.addAllSymlinks("symlinks")

os.popen(f'sh {resourcesDir}/userInterface/kde.sh')
os.popen(f'sh {resourcesDir}/userInterface/removeShutdownOptions.sh')
os.popen(f'sh {resourcesDir}/configurations/key_bindings.sh')