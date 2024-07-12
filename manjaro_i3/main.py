import os
import Prerequisites
import DriveMounting
import Packages
import SystemLinks
import RemoveShutdownOptions
import Themes
import FolderSyncing

resourcesDir = os.getcwd() + "/resources/"

Prerequisites.installAndConfigureGit(resourcesDir + "git")
DriveMounting.mountDrives(resourcesDir + "drives", resourcesDir + "serverConfig")
Packages.installPackages(resourcesDir + "packages")
SystemLinks.addAllSymlinks(resourcesDir + "symlinks")
RemoveShutdownOptions.removeShutdownOptions()
Themes.applyGrubTheme()
FolderSyncing.syncKeyboardShortcuts()

# TODO: 
# - setup symlinks
# - setup folder syncs
# - use models
# - install iscsitools before mountDrives
# - setup iscsi drive on boot (currently fstab entry bricks system)