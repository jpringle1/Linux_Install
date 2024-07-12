import os
import Prerequisites
import DriveMounting
import Packages
import SystemLinks
import RemoveShutdownOptions
import Themes
import FolderSyncing
from Models import DriveCollection, ServerConfig

resourcesDir = os.getcwd() + "/resources/"

Prerequisites.installAndConfigureGit(resourcesDir + "git")

drives = DriveCollection(resourcesDir + "drives")
serverConfiguration = ServerConfig(resourcesDir + "serverConfig")
DriveMounting.mountDrives(drives, serverConfiguration)

Packages.installPackages(resourcesDir + "packages")
SystemLinks.addAllSymlinks(resourcesDir + "symlinks")
RemoveShutdownOptions.removeShutdownOptions()
Themes.applyGrubTheme()
FolderSyncing.syncKeyboardShortcuts()

# TODO: 
# - use models
# - setup symlinks
# - setup folder syncs
# - install iscsitools before mountDrives
# - setup iscsi drive on boot (currently fstab entry bricks system)