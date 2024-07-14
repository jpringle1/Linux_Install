import os

from Scripts import Prerequisites
from Scripts.DriveMounting import DriveCollection
from Scripts.Packages import Packages
from Scripts import SystemLinks
from Scripts import FolderSyncing
from Scripts import Themes
from Scripts import ConfigWriter

from Models.Configs import ConfigOptions, GitConfig, ServerConfig
from Models.SymLinks import SymLinks
from Models.Syncs import Syncs

resourcesDir = os.getcwd() + "/Resources/"

Prerequisites.installAndConfigureGit(GitConfig(resourcesDir + "git"))

serverConfig = ServerConfig(resourcesDir + "serverConfig")

drives = DriveCollection(resourcesDir + "drives")
drives.setupSmbConfig(resourcesDir + "smbConfig")
drives.addFstabEntries(serverConfig)
drives.mount()

packages = Packages(resourcesDir + "packages")
packages.refreshRepositories()
packages.installPackages()

SystemLinks.addAllSymlinks(SymLinks(resourcesDir + "symlinks"))
ConfigWriter.SetOptions(ConfigOptions(resourcesDir + "ConfigOptions"))
Themes.applyGrubTheme(ConfigOptions(resourcesDir + "grubOptions"))
FolderSyncing.syncKeyboardShortcuts()

# TODO:
# - Fix models not showing propeties in intellisense (DriverCollections)
# - Test everything. Shit seems broken since i moved everything into models
# - setup symlinks
# - setup folder syncs
# - install iscsitools before mountDrives
# - setup iscsi drive on boot (currently fstab entry bricks system)
# - setup integration tests maybe?