import os
import Prerequisites
import DriveMounting
import Packages
import SystemLinks
import RemoveShutdownOptions
import Themes
import FolderSyncing
from models.Drives import DriveCollection
from models.Configs import ServerConfig, GitConfig
from models import Packages
from models.SymLinks import SymLinks
from models.Syncs import Syncs

resourcesDir = os.getcwd() + "/resources/"

Prerequisites.installAndConfigureGit(GitConfig(resourcesDir + "git"))

drives = DriveCollection(resourcesDir + "drives")
serverConfiguration = ServerConfig(resourcesDir + "serverConfig")
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