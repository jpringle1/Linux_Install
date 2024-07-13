import os
import pyfstab

from Scripts import Prerequisites
from Scripts import DriveMounting
from Scripts import Packages
from Scripts import SystemLinks
from Scripts import FolderSyncing
from Scripts import Themes
from Scripts import ConfigWriter

from Models.Drives import DriveCollection
from Models.Configs import ConfigOptions, GitConfig, ServerConfig
from Models.Packages import Packages
from Models.SymLinks import SymLinks
from Models.Syncs import Syncs

resourcesDir = os.getcwd() + "/Resources/"

Prerequisites.installAndConfigureGit(GitConfig(resourcesDir + "git"))

DriveMounting.mountDrives(
    DriveCollection(resourcesDir + "drives"), 
    ServerConfig(resourcesDir + "serverConfig")
)

Packages.installPackages(Packages(resourcesDir + "packages"))
SystemLinks.addAllSymlinks(SymLinks(resourcesDir + "symlinks"))
ConfigWriter.SetOptions(ConfigOptions(resourcesDir + "ConfigOptions"))
Themes.applyGrubTheme(ConfigOptions(resourcesDir + "grubOptions"))
FolderSyncing.syncKeyboardShortcuts()

# TODO:
# - Fix models not showing propeties in intellisense (DriverCollections)
# - Test everything. Shit seems broken since i moved everything into models
# - refactor grub editer
# - setup symlinks
# - setup folder syncs
# - install iscsitools before mountDrives
# - setup iscsi drive on boot (currently fstab entry bricks system)