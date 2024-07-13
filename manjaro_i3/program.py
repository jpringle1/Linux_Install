import os

from Scripts import Prerequisites
from Scripts import DriveMounting
from Scripts import Packages
from Scripts import SystemLinks
from Scripts import RemoveShutdownOptions
from Scripts import FolderSyncing
from Scripts import Themes

from Models.Drives import DriveCollection
import Models.Configs as Configs
from Models.Packages import Packages
from Models.SymLinks import SymLinks
from Models.Syncs import Syncs

resourcesDir = os.getcwd() + "/Resources/"

Prerequisites.installAndConfigureGit(Configs.GitConfig(resourcesDir + "git"))

drives = DriveCollection(resourcesDir + "drives")
serverConfiguration = Configs.Server(resourcesDir + "serverConfig")
DriveMounting.mountDrives(drives, serverConfiguration)

Packages.installPackages(Packages(resourcesDir + "packages"))
SystemLinks.addAllSymlinks(SymLinks(resourcesDir + "symlinks"))
RemoveShutdownOptions.removeShutdownOptions()
Themes.applyGrubTheme()
FolderSyncing.syncKeyboardShortcuts()

# TODO:
# - Refactor KDE configurer
# - refactor grub editer
# - setup symlinks
# - setup folder syncs
# - install iscsitools before mountDrives
# - setup iscsi drive on boot (currently fstab entry bricks system)