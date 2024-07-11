import os
import Prerequisites
import DriveMounting
import Packages
import SystemLinks
import RemoveShutdownOptions
import Themes

resourcesDir = os.getcwd() + "/resources/"


Prerequisites.installAndConfigureGit(resourcesDir + "git")
DriveMounting.mountDrives(resourcesDir + "drives", resourcesDir + "serverConfig")
Packages.installPackages(resourcesDir + "packages")
SystemLinks.addAllSymlinks(resourcesDir + "symlinks")
RemoveShutdownOptions.removeShutdownOptions()
Themes.applyGrubTheme()

# TODO: 
# - install iscsitools before mountDrives
# - setup iscsi drive on boot (currently fstab entry bricks system)
# - setup symlinks
# - setup folder syncs
# - refactor bash scripts to python (kde, key_bindings, removeShutdownOptions)
# - use models