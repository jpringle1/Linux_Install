import os

from Scripts.Git import Git
from Scripts.DriveMounting import DriveCollection
from Scripts.Packages import Packages
from Scripts.ServerConfig import ServerConfig
from Scripts.FolderSyncing import FolderSyncing
from Scripts import Themes
from Scripts import ConfigWriter
from Scripts.SystemLinks import SymLinks

from Models import ConfigOptions

resourcesDir = os.getcwd() + "/Resources/"
envDir = os.getcwd() + "/.env/"

git = Git(resourcesDir + "git")
git.install()
git.configure()
git.authorise(envDir + ".gittoken")

serverConfig = ServerConfig(resourcesDir + "serverConfig")
serverConfig.setupSmbConfig(resourcesDir + "smbConfig")

drives = DriveCollection(resourcesDir + "drives")
drives.addFstabEntries(serverConfig)
drives.mount()

packages = Packages(resourcesDir + "packages")
packages.refreshRepositories()
packages.installPackages()

symLinks = SymLinks(resourcesDir + "symlinks")
symLinks.createSymLinks()

configOptions = ConfigOptions(resourcesDir + "ConfigOptions")
ConfigWriter.SetOptions(configOptions)

grubTheme = Themes.Grub(resourcesDir + "grubOptions")
grubTheme.apply()
grubTheme.refreshGrub()

folderSyncing = FolderSyncing()
folderSyncing.syncKeyboardShortcuts()

# TODO:
# - Fix models not showing propeties in intellisense (DriverCollections)
# - Test everything. Shit seems broken since i moved everything into models
# - setup symlinks
# - setup folder syncs
# - install iscsitools before mountDrives
# - setup iscsi drive on boot (currently fstab entry bricks system)
# - setup integration tests maybe?